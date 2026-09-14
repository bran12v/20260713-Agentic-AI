"""Extract the helpdesk-relevant chapters of each manual into `text/<model>.md`.

    python extract_text.py            # rebuild every model file
    python extract_text.py 5521       # rebuild the models whose slug matches

The markdown is what the corpus actually indexes. A PDF is a container; chunking
and retrieval operate on text, and committing the text means the team has usable
corpus content without running a 150 MB download first, and a diff shows when a
vendor revises a manual.

**Teardown chapters are excluded on purpose.** "Removing and installing
components" is 79 KB of screw sizes in the Latitude 5521 alone and answers
nothing a user asks. The full PDF stays available through fetch_manuals.py for
anyone who needs it.

Requires: pypdf.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from pypdf import PdfReader

HERE = Path(__file__).parent
OUT = HERE / "text"

# Chapters that answer a helpdesk question. Matched case-insensitively against
# top-level bookmarks.
KEEP = (
    "troubleshooting",
    "system setup",
    "bios setup",
    "specifications",
    "components",
    "drivers and downloads",
    "software",
    "backing up",
    "hp pc hardware diagnostics",
    "computer setup",
    "product description",
    "views of",
    "set up your",
)

# Chapters that are teardown. Checked first — "major components of your
# computer" matches KEEP's "components" but is a parts diagram, not guidance.
DROP = (
    "removing and installing",
    "removal and replacement",
    "illustrated parts catalog",
    "major components",
    "disassembly",
    "screw list",
    "recommended tools",
)


def top_level_chapters(reader: PdfReader) -> list[tuple[str, int, int]]:
    """(title, first_page, end_page) for each top-level bookmark, in page order."""
    tops: list[tuple[str, int]] = []

    def walk(items, depth=0):
        for item in items:
            if isinstance(item, list):
                walk(item, depth + 1)
                continue
            if depth == 0:
                try:
                    tops.append((str(item.title).strip(), reader.get_destination_page_number(item)))
                except Exception:  # noqa: BLE001 — a malformed bookmark is not fatal
                    pass

    try:
        walk(reader.outline)
    except Exception:  # noqa: BLE001
        return []

    tops.sort(key=lambda x: x[1])
    out = []
    for i, (title, page) in enumerate(tops):
        end = tops[i + 1][1] if i + 1 < len(tops) else len(reader.pages)
        out.append((title, page, end))
    return out


def wanted(title: str) -> bool:
    low = title.lower()
    if any(d in low for d in DROP):
        return False
    return any(k in low for k in KEEP)


def clean(text: str) -> str:
    """Tidy PDF text without destroying structure.

    Page furniture and hyphenation survive extraction and make chunks noisy, so
    both go. Blank-line structure is kept because the chunker splits on it.
    """
    text = text.replace("­", "")           # soft hyphens
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)  # words broken across lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    # Page numbers are deliberately NOT stripped. A bare number on its own line
    # is also what a diagnostic LED blink code looks like once a table has been
    # extracted — Dell's "2,8  Power rail failure" renders as "2" and "8" on
    # separate lines. Removing page numbers deleted the single most useful table
    # in the corpus, so the noise stays and the codes survive.
    return text.strip()


def extract(doc: dict) -> str:
    """The body of one document: selected chapters, or all of it when small."""
    path = HERE / doc["file"]
    reader = PdfReader(str(path))
    chapters = [c for c in top_level_chapters(reader) if wanted(c[0])]

    # Spec sheets, guidebooks and the Apple info sheets have no useful outline
    # and are short enough to take whole. The title goes in the heading because
    # a model with two such documents would otherwise produce two identical
    # "Full document" headings, and a citation has to name one of them.
    if not chapters:
        body = "\n".join((p.extract_text() or "") for p in reader.pages)
        return (
            f"## {doc['title']}\n\n_Complete document, {len(reader.pages)} pages_\n\n"
            + clean(body)
            + "\n"
        )

    parts = []
    for title, start, end in chapters:
        body = "\n".join((p.extract_text() or "") for p in reader.pages[start:end])
        body = clean(body)
        if len(body) < 200:
            continue
        parts.append(
            f"## {title}\n\n_{doc['title']}, pages {start + 1}–{end}_\n\n{body}\n"
        )
    return "\n".join(parts)


DEPTH_RANK = {"full": 4, "partial": 3, "pointers": 2, "none": 1}


def header(model: str, docs: list[dict], extra_depth: str | None = None) -> str:
    lines = [f"# {model}", ""]
    lines.append("| | |")
    lines.append("|---|---|")
    regs = sorted({d["regulatory_model"] for d in docs if d.get("regulatory_model")})
    if regs:
        lines.append(f"| Regulatory model | {', '.join(regs)} |")
    # extra_depth lets a non-PDF section raise the model's depth: the MacBook Pro
    # Info sheets troubleshoot nothing, but the article index below them does
    # route a symptom somewhere, and a reader deciding whether to trust this file
    # needs the header to reflect the whole file.
    depths = [d.get("troubleshooting", "none") for d in docs]
    if extra_depth:
        depths.append(extra_depth)
    depth = max(depths, key=lambda v: DEPTH_RANK.get(v, 0))
    lines.append(f"| Troubleshooting depth | **{depth}** |")
    lines.append(f"| Documents | {len(docs)} |")
    lines.append("")
    for d in docs:
        src = d["url"]
        if d.get("wayback"):
            src = f"{d['wayback']['original_url']} (via the Internet Archive, snapshot {d['wayback']['timestamp']})"
        lines.append(f"- **{d['title']}** — {d.get('revision') or 'no revision stated'}")
        lines.append(f"  - Source: {src}")
        lines.append(f"  - Answers: {d.get('answers', '')}")
    lines.append("")
    lines.append(
        "Extracted from the vendor document. Teardown chapters are omitted — they answer "
        "nothing a user asks. See `../SOURCES.md`."
    )
    lines.append("")
    return "\n".join(lines)


def apple_index(data: dict) -> str:
    """Apple publishes no service manual PDF, so the MacBook Pro file carries an
    index of Apple's own troubleshooting articles instead.

    These are pointers, not quotations. The authoritative text lives at each URL,
    and presenting a rendered paraphrase as a vendor quote is exactly the
    grounding failure section 4.7 exists to prevent.
    """
    block = data.get("apple_support_articles")
    if not block:
        return ""
    lines = [
        "",
        "## Apple troubleshooting articles",
        "",
        block["note"],
        "",
        "| Symptom | Apple article |",
        "|---|---|",
    ]
    for article in block["articles"]:
        lines.append(f"| {article['symptom']} | {article['url']} |")
    lines.append("")
    return "\n".join(lines)


def slug(model: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", model.lower()).strip("-")


def main(argv: list[str]) -> int:
    data = json.loads((HERE / "sources.json").read_text(encoding="utf-8"))
    OUT.mkdir(exist_ok=True)

    by_model: dict[str, list[dict]] = {}
    for doc in data["documents"]:
        model = doc.get("device_model") or "Dell — general (all models)"
        by_model.setdefault(model, []).append(doc)

    wanted_args = [a for a in argv if not a.startswith("--")]
    written = 0
    for model, docs in sorted(by_model.items()):
        name = slug(model)
        if wanted_args and not any(a.lower() in name for a in wanted_args):
            continue
        try:
            body = "\n".join(extract(d) for d in docs)
        except FileNotFoundError:
            print(f"  {model:<40} SKIPPED — PDF missing, run fetch_manuals.py", file=sys.stderr)
            continue
        articles = data.get("apple_support_articles")
        indexed = bool(articles) and articles["device_model"] == model
        text = header(model, docs, "pointers" if indexed else None) + "\n" + body
        if indexed:
            text += apple_index(data)
        (OUT / f"{name}.md").write_text(text, encoding="utf-8", newline="\n")
        print(f"  {model:<40} {len(text) / 1024:6.1f} KB  -> text/{name}.md")
        written += 1

    print(f"\n{written} model file(s) written to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
