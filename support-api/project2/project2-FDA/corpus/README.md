# Vigil device vigilance corpus

This directory contains excerpts of federal public-domain material — 21 CFR Parts 803, 806 and 807, FDA's guidance on medical device reporting and on when a device change requires a new 510(k), and Form FDA 3500A with its instructions — reproduced as a training artifact for the Vigil exercise.

**It is not a current or authoritative source, and it is not regulatory or clinical guidance.** Sections have been excerpted out of their surrounding text, and the material is fixed at its 14 August 2026 retrieval date. Anyone with an actual reporting or submission decision to make must consult the published sources, which are linked per document in [MANIFEST.md](MANIFEST.md), and their own regulatory affairs function.

The complaints the system analyses are fictional. Northvale Medical Devices does not exist, and no patient, clinician or facility named in `packets/` is real.

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
python fetch_corpus.py CFR-803    # one document, no verification
```

Raw upstream downloads are cached in `.cache/`, which is not committed. Delete it to force a fresh pull.

Rebuilds are byte-reproducible: given the same upstream bytes, a rebuild produces the same PDFs and text files, so a clean run leaves no git diff. A diff means an upstream source moved — or that your renderer differs from the one that built the committed files. The PDFs here were produced with **reportlab 5.0.0** and **pypdf 6.16.1**; font metrics and stream layout are version-dependent, so a different reportlab rewrites every PDF and can shift page counts on documents you did not touch. Before changing `sources.json`, rebuild unchanged and confirm `git status` is clean. If it is not, your versions differ and the diff is yours, not the agency's.

A full rebuild ends with a verification pass over the extracted text. Every topic declared out-of-corpus in `sources.json`'s `verification` block must have zero occurrences and every near-miss topic must have at least one; the build fails otherwise, and distractor counts are printed for transcription into the manifest. `MANIFEST.md` transcribes those same lists for a human reader — the build does not read it, so an edit there that is not mirrored into `sources.json` changes nothing but the claim. This exists because a refusal test written against a topic that turns out to be present tests the opposite of what it claims to, and nothing about the test itself reveals the mistake.

The three CFR parts are pinned to eCFR issue date 2026-08-04 and will reproduce exactly. The FDA guidance documents and forms are served from `fda.gov/media/<id>/download`, where the identifier is opaque and **is not stable across revisions** — FDA reissues a guidance under a new identifier rather than updating the old one. If a rebuild returns a document about something else entirely, that is what happened; check `text/` before assuming the page ranges are wrong.

## Guidance is not regulation, and this corpus is mostly guidance

Three of the six documents are FDA guidance, and every one of them carries the words **"Contains Nonbinding Recommendations"** on nearly every page. That phrase is not decoration. FDA guidance states the Agency's current thinking; it does not create enforceable obligations, and a manufacturer may use an alternative approach that satisfies the statute.

For this exercise that means a determination grounded only in guidance is incomplete. Every claim should cite the guidance **and** the regulation it construes — and the brief makes that an acceptance item rather than a suggestion.

The 510(k) change guidance is also unusual in shape: it decides by **flowchart** rather than by prose rule. Twelve of its twenty carried pages are decision diagrams, which is a harder extraction problem than a table and is the reason it is in the corpus.
