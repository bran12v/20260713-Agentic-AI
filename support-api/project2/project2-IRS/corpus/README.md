# Payline worker classification and payroll deposit corpus

This directory contains excerpts of federal public-domain material — 26 CFR Part 31, Rev. Proc. 2025-10 and Rev. Rul. 2025-3, Publications 15 and 15-A, and Form SS-8 with its instructions — reproduced as a training artifact for the Payline exercise.

**It is not a current or authoritative source, and it is not tax advice.** Sections have been excerpted out of their surrounding text, and the material is fixed at its 14 August 2026 retrieval date. Anyone with an actual classification, withholding or deposit decision to make must consult the published sources, which are linked per document in [MANIFEST.md](MANIFEST.md), and their own tax counsel.

The worker files the system analyses are fictional. Harbrook Staffing Group does not exist, and no worker, client or engagement named in `packets/` is real.

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
python fetch_corpus.py                # all seven documents, then verify
python fetch_corpus.py RP-2025-10     # one document, no verification
```

Raw upstream downloads are cached in `.cache/`, which is not committed. Delete it to force a fresh pull.

Rebuilds are byte-reproducible: given the same upstream bytes, a rebuild produces the same PDFs and text files, so a clean run leaves no git diff. A diff means an upstream source moved — or that your renderer differs from the one that built the committed files. The PDFs here were produced with **reportlab 5.0.0** and **pypdf 6.16.1**; font metrics and stream layout are version-dependent, so a different reportlab rewrites every PDF and can shift page counts on documents you did not touch. Before changing `sources.json`, rebuild unchanged and confirm `git status` is clean. If it is not, your versions differ and the diff is yours, not the agency's.

A full rebuild ends with a verification pass over the extracted text. Every topic declared out-of-corpus in `sources.json`'s `verification` block must have zero occurrences and every near-miss topic must have at least one; the build fails otherwise, and distractor counts are printed for transcription into the manifest. `MANIFEST.md` transcribes those same lists for a human reader — the build does not read it, so an edit there that is not mirrored into `sources.json` changes nothing but the claim. This exists because a refusal test written against a topic that turns out to be present tests the opposite of what it claims to, and nothing about the test itself reveals the mistake.

The two CFR documents are pinned to eCFR issue date 2026-08-04 and will reproduce exactly. **The IRS publications are not versioned and will move.** Publications 15 and 15-A are keyed to a tax year — these are the 2026 editions — and IRS reflows them every December, so a rebuild after a new edition posts will need new page ranges. Read the first page of each excerpt before trusting a rebuild that produced a diff.

## Section 530 is a statute you will not find in the Internal Revenue Code

Section 530 of the Revenue Act of 1978 decides whether a firm owes employment tax on a reclassified worker, and it was never codified. There is no `26 U.S.C. § 530` to cite for it — that section number belongs to Coverdell education savings accounts, which is a trap for anyone searching by citation alone.

**Section 530(b) also prohibits Treasury from issuing regulations or revenue rulings on the employment status of any individual.** That is why this corpus has no Federal Register rulemaking preamble where its sibling projects do: there is no notice-and-comment record, because the statute forbids creating one. Rev. Proc. 2025-10 § 2.06 addresses the point directly, explaining that the revenue procedure is permissible because it clarifies how section 530 is applied rather than classifying any worker or category of worker.

That limit is inherited by anything built on this corpus. **The documents can ground how the test is applied. They cannot ground what the answer is for a category of worker**, and a system that produces one is asserting something the government itself is barred from publishing.

## "Safe harbor" means two unrelated things here

The term appears 18 times across two documents and denotes two different rules from two different bodies of law:

1. **The section 530 reasonable-basis safe harbors** — judicial precedent, prior audit, industry practice — at `RP-2025-10` § 6. These decide whether a firm owes employment tax at all.
2. **The deposit-shortfall safe harbor** at `CFR-DEPOSIT` § 31.6302-1(f), which `PUB-15` calls the accuracy-of-deposits rule. This decides whether a penalty applies to a computation.

An unfiltered query returns both. Filtering on `doc_type` will not separate them, since one is guidance and one is regulation but the publication restates the regulation in a third vocabulary. This is what `section_path` filtering is for, and it is the retrieval problem this corpus is built around.

Practitioners call the first set the "**safe havens**". That phrase appears zero times here.

## Guidance is not regulation, and the two most important documents are guidance

`RP-2025-10` and `RR-2025-3` carry the section 530 analysis and the reclassification liability rules, and both are IRS published guidance rather than regulation. Guidance binds the IRS in the sense that taxpayers may rely on it; it is not the statute, and where a revenue procedure and a regulation appear to differ the regulation governs.

For this exercise that means a determination grounded only in guidance is incomplete wherever a regulation exists on the same point — which is the case for R1 and R4, and not the case for R2, because section 530 has no regulations by statutory prohibition. The brief handles that asymmetry explicitly rather than requiring a paired citation that cannot exist.

## The table is in Publication 15

`PUB-15` carries the deposit penalty tiers as a genuine table — 2% at 1 to 5 days late, 5% at 6 to 15, 10% at 16 or more but before 10 days from the first notice, 15% after that — plus the monthly and semiweekly schedules and the $100,000 next-day rule with a worked example. Cells that survive extraction without their row associations are worse than no extraction at all, because a penalty rate detached from its day range still looks like an answer.
