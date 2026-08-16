# Claimpath admission status and appeals corpus

This directory contains excerpts of federal public-domain material — 42 CFR Parts 412 and 405, the Federal Register preamble that created the two-midnight framework, and three chapters of the CMS Internet-Only Manuals covering inpatient services, claims appeals and the Advance Beneficiary Notice — reproduced as a training artifact for the Claimpath exercise.

**It is not a current or authoritative source, and it is not billing, coverage or legal guidance.** Sections have been excerpted out of their surrounding text, and the material is fixed at its 14 August 2026 retrieval date. Anyone with an actual admission, billing or appeal decision to make must consult the published sources, which are linked per document in [MANIFEST.md](MANIFEST.md), and their own compliance function.

The denial files the system analyses are fictional. Anselm Regional Health does not exist, and no patient, physician or facility named in `packets/` is real.

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
python fetch_corpus.py            # all six documents, then verify
python fetch_corpus.py CFR-412    # one document, no verification
```

Raw upstream downloads are cached in `.cache/`, which is not committed. Delete it to force a fresh pull.

Rebuilds are byte-reproducible: given the same upstream bytes, a rebuild produces the same PDFs and text files, so a clean run leaves no git diff. A diff means an upstream source moved — or that your renderer differs from the one that built the committed files. The PDFs here were produced with **reportlab 5.0.0** and **pypdf 6.16.1**; font metrics and stream layout are version-dependent, so a different reportlab rewrites every PDF and can shift page counts on documents you did not touch. Before changing `sources.json`, rebuild unchanged and confirm `git status` is clean. If it is not, your versions differ and the diff is yours, not the agency's.

A full rebuild ends with a verification pass over the extracted text. Every topic declared out-of-corpus in `sources.json`'s `verification` block must have zero occurrences and every near-miss topic must have at least one; the build fails otherwise, and distractor counts are printed for transcription into the manifest. `MANIFEST.md` transcribes those same lists for a human reader — the build does not read it, so an edit there that is not mirrored into `sources.json` changes nothing but the claim. This exists because a refusal test written against a topic that turns out to be present tests the opposite of what it claims to, and nothing about the test itself reveals the mistake. It has already caught one here — see the manifest's note on "occupational safety", which appears in § 412.1 because of an N95 respirator payment adjustment.

The two CFR parts are pinned to eCFR issue date 2026-08-04 and will reproduce exactly. The **Internet-Only Manuals are not versioned**: CMS updates them by transmittal at stable URLs, so the same address returns different contents over time. Each manual section carries its own revision line, which is what a diff of `text/` will show you. Page ranges are what shift first — read the first page of each excerpt before trusting a rebuild that produced a diff.

## The corpus spells its own central term four ways

The phrase everyone uses for this rule is **"the two-midnight rule"**. It appears **zero times** in these documents.

What they contain is `2 midnights` (69), `2-midnight` (58) and `two midnights` (4) — and § 412.3 uses two of those spellings within the same subsection. A retrieval strategy that assumes the practitioner's vocabulary reaches the regulation will fail on the one section that decides every case, and it will fail silently, returning plausible neighbouring text.

The same split runs through the clocks: the regulation writes "120 calendar days", the manual writes "120 days". Neither finds the other.

## Manuals are not regulation, and three of six documents are manuals

`IOM-APPEALS`, `IOM-INPATIENT` and `MANUAL-ABN` are CMS instructing its own contractors. They bind those contractors and they state CMS's operational reading, but they are not the rule, and where a manual and a regulation appear to differ the regulation governs.

For this exercise that means a determination grounded only in a manual is incomplete. Every claim should cite the manual **and** the regulation it implements — and the brief makes that an acceptance item rather than a suggestion.

`IOM-APPEALS` is also the table-extraction problem. CHART 1 associates five appeal levels with their filing deadlines and monetary thresholds; CHART 2 associates the same five levels with where each request is filed, split three ways. Cells that survive extraction without their row and column associations are worse than no extraction at all, because they still look like an answer.

## Two things the corpus deliberately does not contain

Both are named by documents that are here, and both must produce a refusal rather than an invention.

- **The inpatient-only procedure list.** § 412.3(d)(2) makes an admission appropriate regardless of expected duration when the procedure is on the list at § 419.22(n). Part 419 is not carried. The rule is citable; whether a given procedure is on the list is not answerable.
- **The amount-in-controversy figures.** CHART 1's monetary-threshold column carries a CMS.gov URL rather than a dollar amount, because the figures are adjusted annually. § 405.1006 states the requirement. No document here states the number.
