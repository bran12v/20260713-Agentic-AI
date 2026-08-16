# Ledgerline currency and suspicious activity corpus

This directory contains excerpts of federal public-domain material — 31 CFR Parts 1010 and 1020, the 2016 Customer Due Diligence rulemaking, six FinCEN administrative rulings, the Designation of Exempt Person form, and the FinCEN SAR and CTR filing instructions — reproduced as a training artifact for the Ledgerline exercise.

**It is not a current or authoritative source, and it is not legal or compliance guidance.** Sections have been excerpted out of their surrounding text, and the material is fixed at its 13 August 2026 retrieval date. Anyone with an actual reporting decision to make must consult the published sources, which are linked per document in [MANIFEST.md](MANIFEST.md), and their own compliance function.

The alerts the system analyses are fictional. Calloway Federal Savings does not exist, and no customer named in `packets/` is a real person or business.

## Layout

| Path | What it is |
|---|---|
| `pdf/` | The excerpted PDFs. These are what the ingestion pipeline cracks. |
| `text/` | Plain-text extraction of each PDF, committed so a diff reveals when an upstream source has changed. |
| `sources.json` | The URL manifest: source addresses, section lists, page ranges, and the declared topic lists. Everything project-specific lives here. |
| `fetch_corpus.py` | Rebuilds `pdf/` and `text/` from `sources.json`. Identical across every project in the cohort. |
| `MANIFEST.md` | Per-document provenance, the recorded cross-references, the retrieval distractors, and the declared out-of-corpus topic list. |

## Rebuilding

```bash
pip install requests "pypdf[crypto]" reportlab
python fetch_corpus.py             # all six documents, then verify
python fetch_corpus.py CFR-1020    # one document, no verification
```

Raw upstream downloads are cached in `.cache/`, which is not committed. Delete it to force a fresh pull.

Rebuilds are byte-reproducible: given the same upstream bytes, a rebuild produces the same PDFs and text files, so a clean run leaves no git diff. A diff means an upstream source moved — or that your renderer differs from the one that built the committed files. The PDFs here were produced with **reportlab 5.0.0** and **pypdf 6.16.1**; font metrics and stream layout are version-dependent, so a different reportlab rewrites every PDF and can shift page counts on documents you did not touch. Before changing `sources.json`, rebuild unchanged and confirm `git status` is clean. If it is not, your versions differ and the diff is yours, not the agency's.

A full rebuild ends with a verification pass over the extracted text. Every topic declared out-of-corpus in `sources.json`'s `verification` block must have zero occurrences and every near-miss topic must have at least one; the build fails otherwise, and distractor counts are printed for transcription into the manifest. `MANIFEST.md` transcribes those same lists for a human reader — the build does not read it, so an edit there that is not mirrored into `sources.json` changes nothing but the claim. This exists because a refusal test written against a topic that turns out to be present tests the opposite of what it claims to, and nothing about the test itself reveals the mistake.

`CFR-1010` and `CFR-1020` are pinned to eCFR issue date 2026-08-04 and will reproduce exactly. The FinCEN PDFs and the Federal Register document are served without version pinning, so if a rebuild produces different page counts, compare against `text/` to see what shifted before assuming the excerpt ranges in `sources.json` are still correct.

## What could not be carried

The **FFIEC BSA/AML Examination Manual** is the document every examiner and every compliance officer actually works from, and it is not here. `ffiec.gov` and `bsaaml.ffiec.gov` return HTTP 403 to automated clients, and the manual is published only as HTML sections and Word documents behind that block.

The interpretive layer is therefore built from **FinCEN's own administrative rulings**, which are published as PDFs and which FinCEN states have precedential value. That is arguably the better source for a determination system — a ruling answers a specific question in writing over a signature, where the manual states examiner expectations — but it is a narrower body of material, and a question that would ordinarily be answered from the manual may have no grounding here.
