"""Rebuild a project's regulatory corpus from its published federal sources.

Reads `sources.json`, downloads each upstream document, excerpts it to the
sections named in the manifest, and emits one PDF and one plain-text file per
document id. The PDFs are what the ingestion pipeline cracks with Document
Intelligence; the text files exist so a diff shows when an upstream source has
changed under you.

    python fetch_corpus.py             # rebuild everything, then verify
    python fetch_corpus.py CFR-1904    # rebuild one document, skip verification

A full rebuild ends with a verification pass over the extracted text: every
topic declared out-of-corpus must have zero occurrences and every near-miss
topic must have at least one, because a refusal test written against a topic
that turns out to be present tests the wrong thing. Distractor terms are
counted and reported for transcription into MANIFEST.md.

This file is identical across every project in the cohort. Everything that
varies between corpora lives in `sources.json`.

Upstream downloads are cached in `.cache/` so repeated runs do not re-hit the
source agencies. Delete `.cache/` to force a fresh pull.

Requires: requests, pypdf, reportlab.
"""

from __future__ import annotations

import json
import re
import sys
import textwrap
import xml.etree.ElementTree as ET
from datetime import date
from html import unescape
from pathlib import Path

import requests
from pypdf import PdfReader, PdfWriter
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer

ROOT = Path(__file__).parent
CACHE = ROOT / ".cache"
PDF_OUT = ROOT / "pdf"
TXT_OUT = ROOT / "text"

TIMEOUT = 180

# Monospace keeps tabular regulatory text column-aligned. Every corpus carries at
# least one document whose tables are the reason it is in the corpus at all, and
# those tables are only usable if the columns survive into the cracked PDF.
STYLES = getSampleStyleSheet()
BODY = ParagraphStyle(
    "body", parent=STYLES["BodyText"], fontSize=9.5, leading=13, alignment=TA_LEFT, spaceAfter=6
)
HEAD = ParagraphStyle(
    "head", parent=STYLES["Heading2"], fontSize=12, leading=15, spaceBefore=14, spaceAfter=8
)
TITLE = ParagraphStyle("title", parent=STYLES["Title"], fontSize=15, leading=19, spaceAfter=14)
MONO = ParagraphStyle("mono", parent=STYLES["Code"], fontSize=7.6, leading=9.2, spaceAfter=8)


def log(msg: str) -> None:
    print(msg, flush=True)


def download(url: str, cache_name: str, user_agent: str) -> bytes:
    """Fetch a URL, caching the raw bytes under .cache/."""
    CACHE.mkdir(exist_ok=True)
    dest = CACHE / cache_name
    if dest.exists():
        return dest.read_bytes()
    log(f"    downloading {url}")
    r = requests.get(url, timeout=TIMEOUT, headers={"User-Agent": user_agent})
    r.raise_for_status()
    dest.write_bytes(r.content)
    return r.content


def esc(s: str) -> str:
    """Escape the three characters reportlab's mini-HTML parser cares about."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_pdf(dest: Path, title: str, blocks: list[tuple[str, str]], author: str, footer: str) -> int:
    """Render (kind, text) blocks to a PDF. Kinds: title, head, body, mono, break."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(dest),
        pagesize=LETTER,
        leftMargin=0.85 * inch,
        rightMargin=0.85 * inch,
        topMargin=0.85 * inch,
        bottomMargin=0.85 * inch,
        title=title,
        author=author,
        # Suppress the embedded creation timestamp and document id. Without this
        # every rebuild rewrites every byte of every PDF, so the committed corpus
        # shows a full-file diff whenever anyone runs the script.
        invariant=1,
    )
    flow = []
    for kind, text in blocks:
        if kind == "break":
            flow.append(PageBreak())
        elif kind == "title":
            flow.append(Paragraph(esc(text), TITLE))
        elif kind == "head":
            flow.append(Paragraph(esc(text), HEAD))
        elif kind == "mono":
            flow.append(Preformatted(text, MONO))
        else:
            flow.append(Paragraph(esc(text), BODY))
    flow.append(Spacer(1, 18))
    flow.append(Paragraph(esc(footer), BODY))
    doc.build(flow)
    return len(PdfReader(str(dest)).pages)


# --------------------------------------------------------------------------
# eCFR
# --------------------------------------------------------------------------

PARA_TAGS = {"P", "FP", "FP-1", "FP-2", "EXTRACT"}


# Characters that fit one line of the monospace style inside the page margins.
TABLE_WIDTH = 108
MIN_COL = 6


def allocate_columns(natural: list[int], typical: list[int], total: int) -> list[int]:
    """Divide `total` characters between columns.

    Columns that all fit keep their natural width. Otherwise each column gets a
    share proportional to its *typical* cell rather than its longest one: a
    single footnote-laden cell would otherwise take most of the line and push
    the real data columns so narrow that values wrap mid-token, which is how a
    CAS number ends up split across two lines.
    """
    gaps = 2 * (len(natural) - 1)
    budget = max(total - gaps, MIN_COL * len(natural))
    if sum(natural) <= budget:
        return natural
    floors = [min(MIN_COL, n) for n in natural]
    spare = budget - sum(floors)
    over = [max(min(t, n) - f, 0) for t, n, f in zip(typical, natural, floors)]
    pool = sum(over) or 1
    widths = [f + int(spare * o / pool) for f, o in zip(floors, over)]
    # Hand any rounding remainder to the column with the most left to say.
    slack = [n - w for n, w in zip(natural, widths)]
    widths[slack.index(max(slack))] += budget - sum(widths)
    return widths


def render_table(el: ET.Element) -> str | None:
    """Flatten an eCFR HTML table into fixed-width rows, wrapping long cells.

    Regulatory tables that map one quantity onto another - voltages onto approach
    distances, container sizes onto residue thresholds, waste quantities onto
    generator categories - are only readable after cracking if the columns stay
    aligned. Cells that do not fit are wrapped onto continuation lines within
    their own column rather than cut off, because the truncated tail is often the
    part that decides the answer: a generator category column clipped to "Large
    quantity generat" and "Very small quantity ge" no longer distinguishes them.
    """
    rows: list[list[str]] = []
    for tr in el.iter():
        if tr.tag.upper() != "TR":
            continue
        cells = [
            " ".join("".join(c.itertext()).split())
            for c in tr
            if c.tag.upper() in {"TD", "TH"}
        ]
        if any(cells):
            rows.append(cells)
    if not rows:
        return None
    ncols = max(len(r) for r in rows)
    natural = [max((len(r[i]) if i < len(r) else 0) for r in rows) for i in range(ncols)]
    typical = []
    for i in range(ncols):
        seen = sorted(len(r[i]) for r in rows if i < len(r) and r[i])
        typical.append(seen[int(len(seen) * 0.75)] if seen else 0)
    cols = allocate_columns(natural, typical, TABLE_WIDTH)

    lines: list[str] = []
    wrapped_any = any(n > c for n, c in zip(natural, cols))
    for r in rows:
        cells = [
            textwrap.wrap(r[i], cols[i]) or [""] if i < len(r) and r[i] else [""]
            for i in range(ncols)
        ]
        height = max(len(c) for c in cells)
        for line in range(height):
            parts = [
                (cells[i][line] if line < len(cells[i]) else "").ljust(cols[i])
                for i in range(ncols)
            ]
            lines.append("  ".join(parts).rstrip())
        # Multi-line rows run together without a separator; single-line ones do not.
        if wrapped_any and height > 1:
            lines.append("")
    return "\n".join(lines)


def ecfr_node_text(node: ET.Element) -> list[tuple[str, str]]:
    """Walk an eCFR section node into renderable blocks, in document order."""
    blocks: list[tuple[str, str]] = []
    consumed: set[int] = set()
    for el in node.iter():
        if id(el) in consumed:
            continue
        tag = el.tag.upper()
        if tag == "HEAD":
            t = " ".join("".join(el.itertext()).split())
            if t:
                blocks.append(("head", t))
        elif tag == "TABLE":
            caption = el.find("CAPTION")
            if caption is not None:
                cap = " ".join("".join(caption.itertext()).split())
                if cap:
                    blocks.append(("head", cap))
            table = render_table(el)
            if table:
                blocks.append(("mono", table))
            consumed.update(id(d) for d in el.iter())
        elif tag in PARA_TAGS:
            t = " ".join("".join(el.itertext()).split())
            if t:
                blocks.append(("body", t))
            consumed.update(id(d) for d in el.iter())
    return blocks


def build_ecfr(spec: dict, issue_date: str, user_agent: str) -> tuple[list[tuple[str, str]], list[str]]:
    url = spec["url"].format(issue_date=issue_date)
    raw = download(url, f"{spec['doc_id']}.xml", user_agent)
    root = ET.fromstring(raw)

    # eCFR marks sections as DIV8 TYPE="SECTION" N="1904.4".
    found: dict[str, ET.Element] = {}
    for div in root.iter():
        if div.tag.upper().startswith("DIV") and div.get("TYPE", "").upper() == "SECTION":
            n = (div.get("N") or "").strip().rstrip(".")
            if n:
                found[n] = div

    blocks: list[tuple[str, str]] = [("title", spec["title"])]
    got: list[str] = []

    if spec.get("keep_paragraphs"):
        # Some sections are enormous and only one lettered paragraph is wanted;
        # keep that paragraph plus any tables inside it.
        node = found.get(spec["sections"][0])
        if node is None:
            log(f"    !! section {spec['sections'][0]} not found in XML")
            return blocks, got
        all_blocks = ecfr_node_text(node)
        wanted = sorted(spec["keep_paragraphs"])
        start = re.compile(r"^\((" + "|".join(wanted) + r")\)")
        # Only the next top-level letter closes the run. Sub-paragraph markers
        # (i), (v) and (x) are roman numerals, not letters, so a generic
        # "any single lowercase letter" stop pattern truncates after one line.
        stop = re.compile(r"^\(" + chr(ord(wanted[-1]) + 1) + r"\)")
        keeping = False
        kept: list[tuple[str, str]] = []
        for kind, text in all_blocks:
            if kind == "body" and start.match(text):
                keeping = True
            elif keeping and kind == "body" and stop.match(text):
                break
            if keeping:
                kept.append((kind, text))
        if kept:
            blocks.append(("head", spec["keep_paragraphs_label"]))
            blocks.extend(kept)
            got.append(f"{spec['sections'][0]}({wanted[-1]})")
            tables = sum(1 for k, _ in kept if k == "mono")
            if tables:
                got.append(f"{tables} {spec.get('table_label', 'table(s)')}")
    else:
        for i, sec in enumerate(spec["sections"]):
            node = found.get(sec)
            if node is None:
                log(f"    !! section {sec} not found in XML")
                continue
            if i:
                blocks.append(("break", ""))
            blocks.extend(ecfr_node_text(node))
            got.append(sec)

    return blocks, got


# --------------------------------------------------------------------------
# Page-range excerpts from an upstream PDF
# --------------------------------------------------------------------------

def build_pdf_pages(spec: dict, user_agent: str) -> tuple[Path, list[str], int]:
    """Assemble one document from page ranges of one or more upstream PDFs.

    An excerpt may name its own `url` and `source`, so a document that an agency
    publishes in pieces - a form on one page and its instructions on another -
    still lands as a single corpus document. Excerpts that name neither fall back
    to the document's own url and the cache name `<doc_id>-source.pdf`.
    """
    writer = PdfWriter()
    readers: dict[str, PdfReader] = {}
    got: list[str] = []
    for ex in spec["excerpts"]:
        name = ex.get("source", "source")
        if name not in readers:
            url = ex.get("url", spec.get("url"))
            raw = download(url, f"{spec['doc_id']}-{name}.pdf", user_agent)
            src = CACHE / f"{spec['doc_id']}-{name}.pdf"
            src.write_bytes(raw)
            readers[name] = PdfReader(str(src))
        reader = readers[name]
        lo, hi = ex["pdf_pages"]
        for p in range(lo, hi + 1):
            if 1 <= p <= len(reader.pages):
                writer.add_page(reader.pages[p - 1])
        got.append(f"{ex['section_path']} (pp. {ex['printed_pages']})")
    dest = PDF_OUT / f"{spec['doc_id']}.pdf"
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("wb") as fh:
        writer.write(fh)
    return dest, got, len(writer.pages)


# --------------------------------------------------------------------------
# HTML pages - interpretation letters, opinion letters, agency handbooks
# --------------------------------------------------------------------------

TAG = re.compile(r"<[^>]+>")
SCRIPT = re.compile(r"<(script|style|nav|header|footer)\b.*?</\1>", re.S | re.I)
# Agencies separate the page name from the site name with either character.
TITLE_SPLIT = re.compile(r"\s*(?:\||::)\s*")

ENTITIES = {
    "&nbsp;": " ",
    "&amp;": "&",
    "&quot;": '"',
    "&#039;": "'",
    "&rsquo;": "'",
    "&ldquo;": '"',
    "&rdquo;": '"',
    "&sect;": "§",
}


def cache_name(prefix: str, label: str) -> str:
    """Name the cache file from the item's label rather than its slug.

    Slugs are URL paths: they nest, so a raw slug names a directory that does
    not exist, and flattening one can exceed the Windows path limit. Labels are
    short, unique within a document, and readable in a `.cache/` listing.
    """
    return f"{prefix}-{re.sub(r'[^A-Za-z0-9._-]+', '-', label).strip('-')[:60]}.html"


def page_text(
    html: str,
    selectors: list[str],
    start: str | None,
    stop: str | None,
    floor: int,
    title_segment: int,
) -> tuple[str, list[str]]:
    """Pull the substantive body out of an agency HTML page.

    `selectors` are class or id fragments tried in order to find the content
    region; the first that matches wins. Agencies key the content region on
    either attribute, and picking the wrong region yields a document made
    entirely of sidebar furniture. `start` drops everything up to and including
    the first paragraph containing that marker, and `stop` truncates at the
    first paragraph containing its own; between them they cut the standing
    preamble and trailer that surround the substantive text on every page of a
    given site. `floor` drops paragraphs shorter than that many characters -
    navigation crumbs, button labels and table-of-contents entries all fall
    under it.

    `title_segment` selects which delimited part of <title> is the page's own
    name. Agencies disagree on the order: some write "Page name | Agency" and
    others "Agency :: Page name", so guessing produces a document whose every
    heading is the agency's name.
    """
    title_m = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    if title_m:
        # Titles carry entities the body-level table below never sees.
        flat = unescape(TAG.sub("", title_m.group(1)))
        parts = [p.strip() for p in TITLE_SPLIT.split(flat) if p.strip()]
        title = parts[title_segment] if parts else "Untitled"
    else:
        title = "Untitled"

    body = SCRIPT.sub(" ", html)
    for sel in selectors:
        m = re.search(
            rf'<div[^>]*(?:class|id)="[^"]*{re.escape(sel)}[^"]*"[^>]*>(.*)', body, re.S | re.I
        )
        if m:
            body = m.group(1)
            break
    body = re.sub(r"<br\s*/?>", "\n", body, flags=re.I)
    body = re.sub(r"</(p|div|li|h\d)>", "\n\n", body, flags=re.I)
    body = TAG.sub(" ", body)
    for entity, char in ENTITIES.items():
        body = body.replace(entity, char)
    paras = [" ".join(p.split()) for p in body.split("\n\n")]
    paras = [p for p in paras if len(p) > floor]
    if start:
        begin = next((i for i, p in enumerate(paras) if start.upper() in p.upper()), -1)
        paras = paras[begin + 1 :]
    if stop:
        cut = next((i for i, p in enumerate(paras) if stop.upper() in p.upper()), len(paras))
        paras = paras[:cut]
    return title, paras


def build_html_pages(spec: dict, user_agent: str) -> tuple[list[tuple[str, str]], list[str]]:
    blocks: list[tuple[str, str]] = [("title", spec["title"])]
    got: list[str] = []
    selectors = spec.get("content_selectors", [])
    start = spec.get("boilerplate_start")
    stop = spec.get("boilerplate_stop")
    floor = spec.get("min_paragraph_chars", 45)
    prefix = spec.get("cache_prefix", spec["doc_id"])
    title_segment = spec.get("title_segment", 0)
    for i, item in enumerate(spec["items"]):
        url = spec["url_template"].format(slug=item["slug"])
        html = download(url, cache_name(prefix, item["label"]), user_agent).decode("utf-8", "replace")
        title, paras = page_text(html, selectors, start, stop, floor, title_segment)
        if i:
            blocks.append(("break", ""))
        blocks.append(("head", f"{item['label']} - {title}"))
        blocks.append(("body", f"Source: {url}"))
        blocks.extend(("body", p) for p in paras)
        got.append(f"{item['label']} {title}")
        log(f"    page {item['label']}: {len(paras)} paragraphs")
    return blocks, got


# --------------------------------------------------------------------------

def pdf_to_text(path: Path) -> str:
    reader = PdfReader(str(path))
    out = []
    for i, page in enumerate(reader.pages, 1):
        out.append(f"\n--- page {i} ---\n")
        out.append(page.extract_text() or "")
    return "".join(out)


def blocks_to_text(blocks: list[tuple[str, str]]) -> str:
    out = []
    for kind, text in blocks:
        if kind == "break":
            out.append("\n" + "-" * 70 + "\n")
        elif kind == "title":
            out.append(f"\n{text}\n{'=' * len(text)}\n")
        elif kind == "head":
            out.append(f"\n{text}\n{'-' * len(text)}\n")
        elif kind == "mono":
            out.append(text + "\n")
        else:
            out.append(textwrap.fill(text, 92) + "\n")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Verification
# --------------------------------------------------------------------------

def verify(checks: dict) -> int:
    """Check the declared distractor, out-of-corpus and near-miss topic lists.

    A refusal test written against a topic that is actually present tests the
    opposite of what it claims to, and a near-miss test written against a topic
    that is absent can never fail. Both mistakes are invisible in review and
    both are cheap to catch here.
    """
    # Collapse whitespace before counting. Body text is wrapped at 92 characters
    # and table cells wrap inside their columns, so a multi-word phrase is
    # routinely split by a newline. Counting the raw text would report a topic
    # as absent because it straddles a line break, and an out-of-corpus check
    # that passes for that reason is worse than no check at all.
    corpus = {
        p.name: " ".join(p.read_text(encoding="utf-8").split()).lower()
        for p in sorted(TXT_OUT.glob("*.txt"))
    }

    def hits(term: str) -> dict[str, int]:
        t = term.lower()
        return {name: text.count(t) for name, text in corpus.items() if t in text}

    failures = 0

    if checks.get("distractors"):
        log("")
        log("  Distractors (transcribe these counts into MANIFEST.md)")
        for term in checks["distractors"]:
            found = hits(term)
            total = sum(found.values())
            where = ", ".join(f"{n.removesuffix('.txt')} {c}" for n, c in sorted(found.items()))
            log(f"    {term:<28} {total:>4}   {where or '(absent)'}")
            if not total:
                log(f"    !! distractor '{term}' does not appear in the corpus")
                failures += 1

    if checks.get("out_of_corpus"):
        log("")
        log("  Out-of-corpus topics (must be absent)")
        for term in checks["out_of_corpus"]:
            found = hits(term)
            if found:
                where = ", ".join(f"{n.removesuffix('.txt')} {c}" for n, c in sorted(found.items()))
                log(f"    !! '{term}' IS PRESENT - {where}")
                failures += 1
        log(f"    {len(checks['out_of_corpus'])} topics checked")

    if checks.get("near_miss"):
        log("")
        log("  Near-miss topics (must be present)")
        for term in checks["near_miss"]:
            found = hits(term)
            if not found:
                log(f"    !! '{term}' IS ABSENT - a near-miss test against it can never fail")
                failures += 1
        log(f"    {len(checks['near_miss'])} topics checked")

    log("")
    if failures:
        log(f"  VERIFICATION FAILED - {failures} problem(s). Fix sources.json or MANIFEST.md.")
    else:
        log("  Verification passed.")
    return failures


def main() -> int:
    spec_file = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    issue_date = spec_file["ecfr_issue_date"]
    author = spec_file["author"]
    footer = spec_file["footer"]
    user_agent = f"Mozilla/5.0 ({spec_file['project']} curriculum corpus build)"
    only = set(sys.argv[1:])

    PDF_OUT.mkdir(exist_ok=True)
    TXT_OUT.mkdir(exist_ok=True)

    summary: list[tuple[str, int, list[str]]] = []

    for spec in spec_file["documents"]:
        doc_id = spec["doc_id"]
        if only and doc_id not in only:
            continue
        log(f"[{doc_id}] {spec['title'][:66]}")

        if spec["kind"] == "pdf_pages":
            dest, got, pages = build_pdf_pages(spec, user_agent)
            (TXT_OUT / f"{doc_id}.txt").write_text(pdf_to_text(dest), encoding="utf-8")
        else:
            if spec["kind"] == "ecfr":
                blocks, got = build_ecfr(spec, issue_date, user_agent)
            else:
                blocks, got = build_html_pages(spec, user_agent)
            dest = PDF_OUT / f"{doc_id}.pdf"
            pages = render_pdf(dest, spec["title"], blocks, author, footer)
            (TXT_OUT / f"{doc_id}.txt").write_text(blocks_to_text(blocks), encoding="utf-8")

        log(f"    -> {dest.relative_to(ROOT)}  {pages} pages")
        for g in got:
            log(f"       + {g}")
        summary.append((doc_id, pages, got))

    log("")
    log("=" * 70)
    total = sum(p for _, p, _ in summary)
    for doc_id, pages, got in summary:
        log(f"  {doc_id:12} {pages:>3} pages   {len(got)} excerpt(s)")
    log(f"  {'TOTAL':12} {total:>3} pages")
    log(f"  retrieved {date.today().isoformat()} | eCFR issue date {issue_date}")

    # A filtered run leaves the other documents' text stale, so the topic lists
    # would be checked against a corpus that is only partly this run's output.
    if only:
        log("")
        log("  Partial build - verification skipped. Run without arguments to verify.")
        return 0

    return 1 if verify(spec_file.get("verification", {})) else 0


if __name__ == "__main__":
    raise SystemExit(main())
