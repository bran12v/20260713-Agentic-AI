"""Rebuild the laptop-manual corpus from its published vendor sources.

Reads `sources.json`, downloads each vendor PDF, and verifies that what came
back is the document that was asked for — not merely that something arrived.

    python fetch_manuals.py                      # fetch everything, then verify
    python fetch_manuals.py MANUAL-LAT-5420-SVC  # fetch one document
    python fetch_manuals.py --verify-only        # check what is already on disk

The PDFs are not committed. They are ~150 MB against a repository whose entire
history is under 300 MB, and vendor manuals are freely republishable from the
URLs recorded here. Run this once and you have the corpus.

Verification is the point of this script rather than an afterthought. Three
documents turned out not to be what their URL implied, and one was a different
computer:

  * `latitude-14-5420-laptop` is the Latitude 5420 **Rugged** (P85G), not the
    standard Latitude 5420 (P137G) — 145 pages of confident, entirely wrong
    procedure for a different chassis. The model-name check does not catch it,
    because that manual also says "Latitude 5420". Only the regulatory model
    separates them, which is why it is checked.
  * `g-series-15-5510-laptop_reference-guide` is "Me and My Dell", a generic
    guide spanning four product families. It is kept with a null device_model.
  * `latitude-15-5521-laptop_reference-guide` is a Windows re-imaging guide.

Three documents are fetched from the Internet Archive rather than the vendor,
and carry a `wayback` block recording the snapshot. Dell has taken those files
down; the archive serves the vendor's original bytes, not a mirror's copy. The
verification below applies to them unchanged, which is what makes that
acceptable — an archived file still has to name its own model and regulatory
model or it fails like any other.

Requires: requests, pypdf.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import requests
from pypdf import PdfReader

HERE = Path(__file__).parent
SOURCES = HERE / "sources.json"

# dl.dell.com serves a 403 block page to the default requests user-agent. The
# body is ~450 bytes of HTML, so it reads as a permissions problem rather than
# a missing file — which is the wrong thing to go and debug.
BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


def load() -> dict:
    return json.loads(SOURCES.read_text(encoding="utf-8"))


def fetch(doc: dict) -> Path:
    target = HERE / doc["file"]
    print(f"  {doc['doc_id']:<26} downloading ...", flush=True)
    r = requests.get(doc["url"], headers={"User-Agent": BROWSER_UA}, timeout=300)
    r.raise_for_status()

    if not r.content.startswith(b"%PDF"):
        raise ValueError(
            f"{doc['doc_id']}: response is not a PDF "
            f"({r.headers.get('content-type')}, {len(r.content)} bytes). "
            "A 403 block page and a 404 both arrive as HTML."
        )

    target.write_bytes(r.content)
    return target


def verify(doc: dict) -> list[str]:
    """Return a list of problems. Empty means the file is what it claims."""
    problems: list[str] = []
    path = HERE / doc["file"]

    if not path.exists():
        return [f"{doc['file']} is missing — run without --verify-only"]

    reader = PdfReader(str(path))

    if doc.get("pages") and len(reader.pages) != doc["pages"]:
        problems.append(
            f"page count is {len(reader.pages)}, manifest says {doc['pages']} "
            "— the vendor may have published a new revision"
        )

    head = " ".join((p.extract_text() or "") for p in reader.pages[:12])
    head = re.sub(r"\s+", " ", head)

    # The expected text must actually appear. For a model-specific document
    # that is the model name; for the generic guide it is the title.
    if doc["verify_text"] not in head:
        problems.append(
            f"the first 12 pages never say {doc['verify_text']!r} "
            "— this is probably a different document"
        )

    expected_reg = doc.get("regulatory_model")
    if expected_reg:
        # A guidebook that covers two chassis prints both, slash-separated:
        # the Latitude 7350 title page reads "Regulatory Model: P179G/P178G".
        # Compare as sets so one manual can legitimately claim both.
        found = re.search(r"Regulatory Model:\s*([A-Z0-9]+(?:/[A-Z0-9]+)*)", head)
        if not found:
            problems.append(f"no regulatory model on the title page, expected {expected_reg}")
        elif set(found.group(1).split("/")) != set(expected_reg.split("/")):
            problems.append(
                f"regulatory model is {found.group(1)}, expected {expected_reg} "
                "— same marketing name, different computer"
            )

    return problems


def report_coverage(data: dict) -> None:
    """Which fleet models have a document and which do not.

    A document with a null device_model — the generic Dell guide — covers no
    model by design, so it is excluded from the count.
    """
    missing = data.get("unavailable", [])
    covered = sorted({d["device_model"] for d in data["documents"] if d.get("device_model")})

    if missing:
        print()
        print(f"{len(missing)} model(s) have no obtainable PDF:")
        for m in missing:
            print(f"  {m['device_model']}")
            print(f"      {m['manual_url']}")
        print()
        print("  Open each URL in a browser, expand all topics, print to PDF, then add")
        print("  it to sources.json with its retrieval date. Do not substitute a")
        print("  third-party mirror — the edition is unverifiable.")

    print()
    print(f"Fleet coverage: {len(covered)} documented, {len(missing)} not.")
    for m in covered:
        print(f"  +  {m}")
    for m in missing:
        print(f"  -  {m['device_model']}")


def main(argv: list[str]) -> int:
    data = load()
    docs = data["documents"]

    verify_only = "--verify-only" in argv
    wanted = [a for a in argv if not a.startswith("--")]
    if wanted:
        docs = [d for d in docs if d["doc_id"] in wanted]
        if not docs:
            print(f"No document matches {wanted}", file=sys.stderr)
            return 2

    if not verify_only:
        print(f"Fetching {len(docs)} document(s)")
        print()
        for doc in docs:
            try:
                path = fetch(doc)
                print(f"  {doc['doc_id']:<26} {path.stat().st_size / 1e6:.1f} MB")
            except Exception as exc:  # noqa: BLE001 — report and keep going
                print(f"  {doc['doc_id']:<26} FAILED: {exc}", file=sys.stderr)
        print()

    print("Verifying")
    print()
    failed = 0
    for doc in docs:
        problems = verify(doc)
        if problems:
            failed += 1
            print(f"  {doc['doc_id']:<26} MISMATCH")
            for p in problems:
                print(f"      {p}")
        else:
            print(f"  {doc['doc_id']:<26} ok")

    if not wanted:
        report_coverage(data)

    if failed:
        print()
        print(f"{failed} document(s) failed verification.", file=sys.stderr)
        return 1

    print()
    print("All documents verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
