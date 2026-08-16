# Straighttime wage and hour corpus

This directory contains excerpts of federal public-domain material — 29 CFR Parts 541, 778, 785 and 553, the 2019 rulemaking that set the current salary level, six Wage and Hour Division opinion letters, and Form WH-347 — reproduced as a training artifact for the Straighttime exercise.

**It is not a current or authoritative source, and it is not legal or wage-and-hour guidance.** Sections have been excerpted out of their surrounding text, and the material is fixed at its 13 August 2026 retrieval date. Anyone with an actual pay question must consult the published sources, which are linked per document in [MANIFEST.md](MANIFEST.md), and their own counsel — and note that many states set their own overtime and exemption rules, none of which are in this corpus.

The pay records the system analyses are fictional. Ardent Field Services does not exist, and no employee named in `packets/` is a real person.

## Layout

| Path | What it is |
|---|---|
| `pdf/` | The excerpted PDFs. These are what the ingestion pipeline cracks. |
| `text/` | Plain-text extraction of each PDF, committed so a diff reveals when an upstream source has changed. |
| `sources.json` | The URL manifest: source addresses, section lists, page ranges, and the declared topic lists. Everything project-specific lives here. |
| `fetch_corpus.py` | Rebuilds `pdf/` and `text/` from `sources.json`. Identical across every project in the cohort. |
| `MANIFEST.md` | Per-document provenance, the recorded cross-references, the retrieval distractors, and the declared out-of-corpus topic list. |

**This corpus carries seven documents rather than the six most projects in the cohort use.** The FLSA splits its rules across four separate CFR parts that cannot be merged into one document — exemptions, the regular rate, hours worked, and the public-safety work period each live in their own part — and all four are load-bearing.

## Rebuilding

```bash
pip install requests "pypdf[crypto]" reportlab
python fetch_corpus.py            # all seven documents, then verify
python fetch_corpus.py CFR-778    # one document, no verification
```

Raw upstream downloads are cached in `.cache/`, which is not committed. Delete it to force a fresh pull.

Rebuilds are byte-reproducible: given the same upstream bytes, a rebuild produces the same PDFs and text files, so a clean run leaves no git diff. A diff means an upstream source moved — or that your renderer differs from the one that built the committed files. The PDFs here were produced with **reportlab 5.0.0** and **pypdf 6.16.1**; font metrics and stream layout are version-dependent, so a different reportlab rewrites every PDF and can shift page counts on documents you did not touch. Before changing `sources.json`, rebuild unchanged and confirm `git status` is clean. If it is not, your versions differ and the diff is yours, not the agency's.

A full rebuild ends with a verification pass over the extracted text. Every topic declared out-of-corpus in `sources.json`'s `verification` block must have zero occurrences and every near-miss topic must have at least one; the build fails otherwise, and distractor counts are printed for transcription into the manifest. `MANIFEST.md` transcribes those same lists for a human reader — the build does not read it, so an edit there that is not mirrored into `sources.json` changes nothing but the claim. This exists because a refusal test written against a topic that turns out to be present tests the opposite of what it claims to, and nothing about the test itself reveals the mistake.

The four CFR parts are pinned to eCFR issue date 2026-08-04 and will reproduce exactly. The opinion letters, the form and the Federal Register document are served without version pinning, so if a rebuild produces different page counts, compare against `text/` to see what shifted before assuming the excerpt ranges in `sources.json` are still correct.

`dol.gov` HTML pages return HTTP 403 to automated clients, so the opinion-letter index cannot be scraped. The letters themselves are fetched directly from their PDF paths under `dol.gov/sites/dolgov/files/`, which are not blocked.

## The salary level, and why the 2024 rule is not here

This corpus deliberately carries the **2019** rulemaking rather than the 2024 one.

The Department issued a rule in 2024 raising the salary threshold in stages. It was **vacated nationwide before its later increases took effect**, and the current regulation reverts to the 2019 figures: **$684 per week** at § 541.600 and **$107,432** for the highly compensated test at § 541.601. Those are the numbers in the eCFR text carried here, and those are the numbers the rules engine must encode.

Carrying the 2024 preamble would have put a persuasive, well-written, thoroughly reasoned account of thresholds that are **not law** directly alongside the regulation — the most dangerous possible corpus content for a retrieval system, because it reads as authoritative and is wrong. The 2019 rule is the rulemaking that actually produced the operative text, so it is the one that belongs here.
