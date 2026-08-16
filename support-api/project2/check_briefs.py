#!/usr/bin/env python3
"""Structural checks over the ten cohort-2026-07 project briefs.

Run from this directory:

    python check_briefs.py            # check all ten
    python check_briefs.py OSHA IRS   # check named projects only

Exit status is 1 if any check fails, so this can gate a build.

Every check here exists because the corresponding defect was found in a shipped
brief at least once. The briefs are ten near-identical documents maintained in
parallel, which is exactly the shape that lets a number drift in one copy and
nowhere else.

WHITESPACE. The corpus text is hard-wrapped at 92 characters and table cells wrap
inside their columns, so any multi-word phrase is routinely split across a
newline. Every search here collapses whitespace first, matching what
`corpus/fetch_corpus.py` does in its own verification pass. A naive grep over
these files reports phrases as missing when they are present; do not "fix" a
manifest on the strength of one.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys

BOX = "│┐┘┌┤├"
WORD = {2: "two", 3: "three"}



def norm(text: str) -> str:
    """Collapse all whitespace and lowercase. The only correct way to search this corpus."""
    return " ".join(text.split()).lower()


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class Project:
    def __init__(self, folder: str) -> None:
        self.folder = folder
        self.name = folder.replace("project2-", "")
        self.brief = read(os.path.join(folder, "project2-requirements-2person.md"))
        self.manifest = read(os.path.join(folder, "corpus", "MANIFEST.md"))
        self.sources = json.loads(read(os.path.join(folder, "corpus", "sources.json")))
        self.texts = {
            os.path.basename(p)[:-4]: norm(read(p))
            for p in glob.glob(os.path.join(folder, "corpus", "text", "*.txt"))
        }
        self.corpus = " ".join(self.texts.values())

    def section(self, n: int) -> str:
        """The body of `## n. ...` up to the next numbered section."""
        body = self.brief.split(f"## {n}.", 1)[1]
        nxt = re.search(r"^## \d+\. ", body, re.M)
        return body[: nxt.start()] if nxt else body

    def count(self, term: str) -> dict[str, int]:
        t = norm(term)
        return {doc: text.count(t) for doc, text in self.texts.items() if text.count(t)}


# --------------------------------------------------------------------------- #
# checks
# --------------------------------------------------------------------------- #

def check_skeleton(p: Project) -> list[str]:
    n = len(re.findall(r"^## \d+\. ", p.brief, re.M))
    return [] if n == 16 else [f"brief has {n} numbered sections, expected 16"]


def check_page_and_word_arithmetic(p: Project) -> list[str]:
    out = []
    sec3 = p.section(3)
    pp = [int(c) for c in re.findall(r"^\| `[A-Z0-9-]+` \|[^|]*\|[^|]*\| (\d+) \|", sec3, re.M)]
    stated = int(re.search(r"documents, (\d+) pages", sec3).group(1))
    in_manifest = int(re.search(r"(\d+) pages", p.manifest).group(1))
    if not pp:
        out.append("no per-document page counts found in the §3 table")
    elif not (sum(pp) == stated == in_manifest):
        out.append(f"pages disagree: §3 column sums to {sum(pp)}, §3 prose says {stated}, MANIFEST says {in_manifest}")

    claimed_words = int(re.search(r"([\d,]+) words", p.manifest).group(1).replace(",", ""))
    actual_words = sum(len(read(f).split()) for f in glob.glob(os.path.join(p.folder, "corpus", "text", "*.txt")))
    if claimed_words != actual_words:
        out.append(f"MANIFEST claims {claimed_words:,} words, corpus has {actual_words:,}")
    return out


def check_conditional_worker(p: Project) -> list[str]:
    """A worker assigned a rule must be able to reach the rules engine.

    §5 blocks any dossier carrying a threshold outcome with no recorded invocation,
    so a conditional worker with a rule id and no engine produces findings that are
    blocked at runtime.
    """
    row = re.search(r"\|\s*\*\*([A-Za-z ]+Worker)\*\* \*\(conditional\)\*.*", p.brief)
    if not row:
        return ["no conditional worker row found in the §4 agent table"]
    cells = [c.strip() for c in row.group(0).split("|")]
    rules, tools = cells[4], cells[5]
    holders = re.search(r"\| `evaluate_rule` \| ([^|]+) \|", p.brief).group(1)
    short = row.group(1).replace(" Worker", "")
    if rules == "—":
        return []
    if short not in holders or "rules engine" not in tools.lower():
        return [f"{row.group(1)} is assigned {rules} but is not an `evaluate_rule` holder with a rules engine"]
    return []


def check_cross_reference_count(p: Project) -> list[str]:
    designated = re.search(r"Cross-references ([0-9, and]+?) (?:are|is)\b", p.manifest)
    if not designated:
        return ["MANIFEST does not designate which cross-references the golden set must exercise"]
    n = len(re.findall(r"\d+", designated.group(1)))
    phrase = f"The {WORD[n]} manifest cross-references designated as the chain"
    if phrase not in p.brief:
        return [f"MANIFEST designates {n} cross-references; §16 does not say '{WORD[n]}'"]
    return []


def check_golden_set_table(p: Project) -> list[str]:
    sec13 = p.section(13)
    rows = [int(x) for x in re.findall(r"^\| [A-Z][^|]*\| (\d+) \|", sec13, re.M)]
    total = int(re.search(r"\*\*Total\*\* \| \*\*(\d+)\*\*", p.brief).group(1))
    return [] if sum(rows) == total else [f"§13 categories sum to {sum(rows)}, table says {total}"]


def check_workflow_diagram(p: Project) -> list[str]:
    lines = p.brief.split("\n")
    i = next(k for k, l in enumerate(lines) if l.startswith("### The workflow graph"))
    j = lines.index("```", i)
    e = lines.index("```", j + 1)
    rails = {
        max(k for k, ch in enumerate(l) if ch in BOX)
        for l in lines[j + 1 : e]
        if any(ch in BOX for ch in l)
    }
    if len(rails) != 1:
        return [f"workflow diagram's right rail wanders across columns {sorted(rails)}"]
    return []


def check_verification_lists(p: Project) -> list[str]:
    """The lists fetch_corpus.py enforces, re-checked here against the committed text."""
    v = p.sources["verification"]
    out = []
    for term in v["out_of_corpus"]:
        if norm(term) in p.corpus:
            out.append(f"declared out-of-corpus but present: {term!r}")
    for term in v["near_miss"]:
        if norm(term) not in p.corpus:
            out.append(f"declared near-miss but absent: {term!r}")
    for term in v["distractors"]:
        if norm(term) not in p.corpus:
            out.append(f"declared distractor but absent: {term!r}")
    return out


def check_rule_sources_resolve(p: Project) -> list[str]:
    """Every section cited in a §5 Source column must exist in this project's own corpus."""
    cited: set[str] = set()
    for row in re.findall(r"^\| R[1-4] \|[^|]*\|([^|]*)\|", p.section(5), re.M):
        cited |= set(re.findall(r"\b\d{2,4}\.\d+[a-z]?(?:\([a-z0-9]+\))*", row))
    missing = [c for c in sorted(cited) if c.split("(")[0] not in p.corpus]
    return [f"§5 cites {c}, which is not in this corpus" for c in missing]


def check_encode_exactly_phrases(p: Project) -> list[str]:
    """Strings §3 tells trainees to encode verbatim must actually be in the corpus."""
    bq = re.search(r"> \*\*The Python rule functions must match.*?\n", p.brief, re.S)
    if not bq:
        return ["§3 has no 'must match the wording exactly' blockquote"]
    out = []
    for phrase in re.findall(r'"([^"]{6,200})"', bq.group(0)):
        # a quotation may elide its middle with an ellipsis; each fragment must resolve
        for fragment in (f for f in re.split(r"…|\.\.\.", phrase) if len(f.strip()) > 5):
            if norm(fragment) not in p.corpus:
                out.append(f"§3 says to encode {fragment.strip()!r}, which is not in the corpus")
    return out


def check_outcome_qualification(p: Project) -> list[str]:
    """An outcome value more than one rule returns must never be named unqualified.

    §9 and §16 drive escalation. If R1 and R2 both return `not_required` and §16
    says "every `not_required` escalates", the two rules have been conflated.
    """
    per = {
        rid: set(re.findall(r"`([a-z0-9_]+)`", body))
        for rid, body in re.findall(r"^\| (R[1-5]) \|[^|]*\|[^|]*\|([^|]*)\|", p.section(5), re.M)
    }
    if not per:
        return []
    every = set().union(*per.values())
    ambiguous = {v for v in every if sum(v in vals for vals in per.values()) > 1} - {"insufficient_data"}
    out = []
    for label, body in (("§9", p.section(9)), ("§16", p.section(16))):
        for m in re.finditer(r"`([a-z0-9_]+)`", body):
            val = m.group(1)
            if val not in ambiguous:
                continue
            if not re.search(r"\bR[1-5]\b", body[max(0, m.start() - 40) : m.start()]):
                owners = sorted(r for r, vals in per.items() if val in vals)
                out.append(f"{label} names `{val}` without a rule qualifier; {' and '.join(owners)} both return it")
    return sorted(set(out))


# An occurrence count in §3 prose, and only that. Deliberately narrow: §3 is dense
# with CFR part numbers, section numbers, page ranges and Federal Register pages,
# and a loose pattern reports every one of them. Only a number explicitly labelled
# "times" or "occurrences" is treated as a claim about the corpus.
COUNT_CLAIM = re.compile(r"\b(\d+)(?:\s+of\s+(\d+))?\s+(?:times|occurrences)\b", re.I)
TERM_BEFORE = re.compile(r'"([^"]{2,60})"|`([^`]{2,60})`')


def check_section3_numeric_claims(p: Project) -> list[str]:
    """Occurrence counts stated in §3 must be obtainable from the corpus.

    §3 restates measurements that `corpus/MANIFEST.md` also carries, which is a
    second place for a number to go stale — it has happened twice. Each claim is
    matched back to the nearest term the sentence quotes and measured.
    """
    failures: list[str] = []
    for sentence in re.split(r"(?<=[.!?])\s+", " ".join(p.section(3).split())):
        for m in COUNT_CLAIM.finditer(sentence):
            claimed = [int(g) for g in m.groups() if g]
            # "34 occurrences of `voltage`" names its term after the number;
            # `"adverse driving" appears 60 times` names it before. Try after first.
            after = re.match(r"\s+of\s+(?:\"([^\"]{2,60})\"|`([^`]{2,60})`)", sentence[m.end() :])
            if after:
                term = after.group(1) or after.group(2)
            else:
                terms = [a or b for a, b in TERM_BEFORE.findall(sentence[: m.start()])]
                terms = [t for t in terms if not re.fullmatch(r"[A-Z][A-Z0-9-]{2,}", t)]
                if not terms:
                    continue
                term = terms[-1]
            per = p.count(term)
            obtainable = set(per.values()) | {sum(per.values())}
            for value in claimed:
                if value not in obtainable:
                    failures.append(
                        f"§3 claims {value} occurrences of {term!r}; corpus gives "
                        f"{sum(per.values())} total {dict(sorted(per.items(), key=lambda kv: -kv[1]))}"
                    )
    return failures


def check_packet_artifacts_described(p: Project) -> list[str]:
    """Every file in the packet tree must be described in 'The supporting artifacts'.

    The trees name three or four files each and, before this check existed, only the
    government form got any guidance on how to build one. A file a trainee cannot
    build is a rule input they will guess at.
    """
    path = os.path.join(p.folder, "packet-preparation.md")
    if not os.path.exists(path):
        return []
    doc = read(path)
    tree = re.search(r"```\n(packets/.*?)```", doc, re.S)
    if not tree:
        return ["packet-preparation.md has no packet tree"]
    artifacts = re.findall(r"[├└]──\s+([\w.-]+\.\w+)", tree.group(1))
    section = re.search(r"## The supporting artifacts\n(.*?)\n---", doc, re.S)
    if not section:
        return ["packet-preparation.md has no 'The supporting artifacts' section"]
    described = set(re.findall(r"^\| `([^`]+)` \|", section.group(1), re.M))
    return [f"packet artifact {a} is in the tree but not described" for a in artifacts if a not in described]


def check_packet_examples_exist(p: Project) -> list[str]:
    """Every artifact a team must author needs a worked example, not just a field list.

    Before this check, nine of ten handouts contained no example of any document —
    a filename, a format and a word count, and nothing to copy. A field list is a
    specification; it is not something a team can build from on day one.

    The real government forms are exempt: the blank ships in the corpus and the
    P1-P4 tables give the field values.
    """
    path = os.path.join(p.folder, "packet-preparation.md")
    if not os.path.exists(path):
        return []
    doc = read(path)
    section = re.search(r"## What they look like filled in\n(.*?)\n## ", doc, re.S)
    if not section:
        return ["packet-preparation.md has no 'What they look like filled in' section"]
    # every artifact named in bold in that section should carry a fenced example,
    # unless it is explicitly excused (a real form, an absent file, or a photograph)
    body = section.group(1)
    named = re.findall(r"\*\*`([^`]+)`\*\*(.{0,400}?)(?=\n\*\*`|\Z)", body, re.S)
    out = []
    for name, blurb in named:
        excused = any(w in blurb.lower() for w in ("the real ", "absent", "not in this packet", "photograph"))
        if "```" not in blurb and not excused:
            out.append(f"{name} is described but has no worked example")
    return out


CLEARS = "one packet in the set that clears with no § 9 trigger firing"


def _escalation_triggers(p: Project) -> set[str]:
    """The rule outcomes §9 escalates on, as bare values.

    Each escalation bullet states its trigger first and its rationale after an em
    dash, and the rationale routinely names outcomes that *do not* escalate — the
    HIPAA population bullet names `presumed_breach` and `unsecured` precisely to
    say they are safe. So the scan stops at the end of the sentence that mentions
    the rule, and drops any `anything other than X` clause, where X is what a
    packet needs to return rather than what escalates.
    """
    body = p.section(9).split("### Escalation", 1)[1].split("### Bounds", 1)[0]
    out: set[str] = set()
    for bullet in re.findall(r"^- (.+)$", body, re.M):
        if "insufficient_data" in bullet:
            out.add("insufficient_data")
        rule = re.search(r"\bR\d\b", bullet)
        if not rule:
            continue
        sentence = bullet[rule.start():].split(". ")[0]
        for clause in sentence.split(", or "):
            if "other than" in clause:
                continue
            out |= set(re.findall(r"`([a-z][a-z0-9_]+)`", clause))
    return out


def check_clean_packet(p: Project) -> list[str]:
    """Exactly one packet must be named as the one that clears, and it must.

    §15 requires an escalation contrast, §16 requires four paired triggers that
    each stay silent on one of a pair, and the demo's middle third is a clean
    incident clearing. All three need a base case that fires nothing. A walk of
    the four packets against §9 in all ten projects found only five with a
    reliable one and only one handout that said which it was.
    """
    path = os.path.join(p.folder, "packet-preparation.md")
    if not os.path.exists(path):
        return []
    doc = read(path)
    if doc.count(CLEARS) != 1:
        return [f"packet-preparation.md names {doc.count(CLEARS)} packets as the one that clears, expected 1"]

    before = re.findall(r"^### (P\d)", doc[: doc.index(CLEARS)], re.M)
    if not before:
        return ["the clean-packet sentence is not under a packet heading"]
    packet = before[-1]
    block = re.split(r"^### P\d", doc, flags=re.M)[int(packet[1])]
    outcome = re.search(r"\*\*Expected outcome\.\*\*(.*?)(?=\n\n)", block, re.S)
    if not outcome:
        return [f"{packet} has no Expected outcome paragraph"]

    returned = set(re.findall(r"\bR\d[^.]{0,80}?returns?\s+\*{0,2}`([a-z0-9_]+)`", outcome.group(1)))
    fires = sorted(returned & _escalation_triggers(p))
    return [f"{packet} is named as the packet that clears but returns {', '.join('`%s`' % v for v in fires)}, which §9 escalates"] if fires else []


def check_packet_dates_stated(p: Project) -> list[str]:
    """The dates a packet carries must be specified per packet, not in the aggregate.

    §16 asks that every packet carry a named set of dates that differ. Backported
    across all ten without reading each handout, that item demanded dates two
    projects deliberately omit — RCRA's accumulation start, which is what keeps P1
    a single-worker dispatch, and CMS's receipt date, which is what P1's five-day
    presumption exists to test. A blanket claim cannot express a deliberate
    absence, so the handout has to speak packet by packet.
    """
    path = os.path.join(p.folder, "packet-preparation.md")
    if not os.path.exists(path):
        return []
    doc = read(path)
    section = re.search(r"## Getting the (?:dates|times) right\n(.*?)\n---", doc, re.S)
    if not section:
        return ["packet-preparation.md has no 'Getting the dates right' section"]
    named = {m for m in re.findall(r"\bP[1-4]\b", section.group(1))}
    if len(named) < 2:
        return [f"the dates section names {len(named)} packet(s); it must say which packets carry which dates"]

    item = [ln for ln in p.section(16).split("\n") if "☐" in ln and re.search(r"date|time", ln)]
    if not item:
        return ["§16 has no acceptance item covering the packet dates"]
    return []


def check_entitlement_subject(p: Project) -> list[str]:
    """An entitlement needs something to be an entitlement *over*.

    "Entitle" appeared three times in every brief — the §10 requirement, the §12
    test list and the CI tier that hard-fails the build on it — with no role, no
    scope and no partition anywhere, and §7 seeding subject records but never an
    analyst or a grant. A team could satisfy the letter of it with a function that
    returns True.
    """
    out = []
    subject = re.search(r"keyed by `\(analyst_id, (\w+), participant\)`", p.section(7))
    if not subject:
        return ["§7's session key does not name a participant alongside the analyst and the subject"]
    grant = re.search(r"grant is a `\(analyst_id, (\w+)\)` row", p.section(7))
    if not grant:
        out.append("§7 seeds no grants, so §10's entitlement check has no partition to deny on")
    elif grant.group(1) == subject.group(1):
        out.append(f"§7 partitions entitlements on `{grant.group(1)}`, which is the subject itself, not a partition")
    item = [ln for ln in p.section(16).split("\n") if "☐" in ln and "grant" in ln and "deni" in ln]
    if not item:
        out.append("§16 has no acceptance item asserting a grant-less caller is denied, which the CI tier hard-fails on")
    return out


def check_run_record_measurable(p: Project) -> list[str]:
    """§12 wants cost and latency measured from the run records, so they must hold it.

    §12 asks for cost per subject per scenario "measured (not estimated)", a
    per-iteration cost and a tier comparison, and its latency table is measured
    from the same rows. §7 listed the run record among the tables and never said
    what a row carries, so none of those numbers had a source.
    """
    sec7 = norm(p.section(7))
    missing = [w for w in ("token", "duration", "cost") if w not in sec7]
    return [f"§7's run record names no {', no '.join(missing)}, which §12 measures from it"] if missing else []


def check_near_boundary_item(p: Project) -> list[str]:
    """§9 configures near-boundary margins everywhere; §16 graded them in four projects.

    §9 requires a margin per rule in all ten and §13 requires a paired case on one,
    but the acceptance item that grades the mechanism survived in four briefs and
    was absent from the other six — and where it did survive it rode on the same
    line as a domain trigger, which is why it was easy to drop.
    """
    item = [ln for ln in p.section(16).split("\n") if "☐" in ln and "near-boundary margin" in ln.lower()]
    if not item:
        return ["§16 has no acceptance item for near-boundary margins, which §9 requires in every project"]
    if "unit" not in item[0].lower():
        return ["§16's near-boundary item does not require the margins to carry their units"]
    return []


def check_image_artifacts_exist(p: Project) -> list[str]:
    """The multimodal step must not be pointed at an artifact no packet ships.

    Two briefs sent the multimodal deployment after a screenshot and after device
    photographs, and made §9 escalate when one contradicted the narrative. Neither
    handout asks for either. Every project's P3 is a scanned form, so the step has
    real work in all ten; anything beyond that has to be in the packet tree.
    """
    path = os.path.join(p.folder, "packet-preparation.md")
    if not os.path.exists(path):
        return []
    step = re.search(r"^3\. \*\*Images\*\* — (.+)$", p.section(6), re.M)
    if not step:
        return ["§6 has no Images step"]
    extra = [w for w in ("photograph", "screenshot", "image gallery") if w in step.group(1).lower()]
    if not extra:
        return []
    tree = re.search(r"```\n(packets/.*?)```", read(path), re.S)
    images = re.findall(r"[├└]──\s+[\w.-]+\.(?:jpg|jpeg|png)", tree.group(1)) if tree else []
    if not images:
        return [f"§6 sends the multimodal deployment after a {extra[0]}, which no packet in the tree carries"]
    return []


def check_markdown_shape(p: Project) -> list[str]:
    """A blockquote flush against a preceding bullet breaks the list on GitHub."""
    out = []
    for path in (
        os.path.join(p.folder, "project2-requirements-2person.md"),
        os.path.join(p.folder, "corpus", "MANIFEST.md"),
        os.path.join(p.folder, "packet-preparation.md"),
    ):
        if not os.path.exists(path):
            continue
        lines = read(path).split("\n")
        # A pipe or a blockquote marker inside a fenced block is content, not markdown.
        # The worked examples in packet-preparation.md draw ASCII forms with `|`.
        fenced, inside = [False] * len(lines), False
        for i, line in enumerate(lines):
            if line.startswith("```"):
                inside = not inside
                fenced[i] = True
            else:
                fenced[i] = inside
        for i in range(1, len(lines)):
            if fenced[i]:
                continue
            if lines[i].startswith(">") and lines[i - 1].startswith("- ") and lines[i - 1].strip():
                out.append(f"{os.path.basename(path)}:{i + 1} blockquote breaks the preceding list")
        for i, line in enumerate(lines, 1):
            if fenced[i - 1]:
                continue
            if line.startswith("|") and line.count("|") < 3:
                out.append(f"{os.path.basename(path)}:{i} malformed table row")
    return out


CHECKS = [
    ("skeleton", check_skeleton),
    ("page/word arithmetic", check_page_and_word_arithmetic),
    ("conditional worker", check_conditional_worker),
    ("cross-reference count", check_cross_reference_count),
    ("golden-set table", check_golden_set_table),
    ("workflow diagram", check_workflow_diagram),
    ("verification lists", check_verification_lists),
    ("rule sources resolve", check_rule_sources_resolve),
    ("encode-exactly phrases", check_encode_exactly_phrases),
    ("outcome qualification", check_outcome_qualification),
    ("packet artifacts described", check_packet_artifacts_described),
    ("packet examples exist", check_packet_examples_exist),
    ("clean packet", check_clean_packet),
    ("entitlement subject", check_entitlement_subject),
    ("run record measurable", check_run_record_measurable),
    ("near-boundary item", check_near_boundary_item),
    ("image artifacts exist", check_image_artifacts_exist),
    ("packet dates stated", check_packet_dates_stated),
    ("markdown shape", check_markdown_shape),
]


def main(argv: list[str]) -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    folders = sorted(glob.glob("project2-*"))
    if argv:
        wanted = {a.upper() for a in argv}
        folders = [f for f in folders if f.replace("project2-", "").upper() in wanted]
        if not folders:
            print(f"no project matches {', '.join(argv)}", file=sys.stderr)
            return 2

    total_failures = 0

    for folder in folders:
        p = Project(folder)
        problems: list[str] = []
        for _, fn in CHECKS:
            problems.extend(fn(p))
        problems.extend(check_section3_numeric_claims(p))

        if problems:
            total_failures += len(problems)
            print(f"{p.name:<7} FAIL")
            for problem in problems:
                print(f"          {problem}")
        else:
            print(f"{p.name:<7} ok")

    print()
    if total_failures:
        print(f"{total_failures} problem(s) across {len(folders)} project(s).")
        return 1
    print(f"All checks pass across {len(folders)} project(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
