# Attestor corpus manifest

Six documents, 70 pages, 46,544 words. Retrieved 13 August 2026. eCFR issue date 4 August 2026.

Every document is federal public-domain material. This file records where each came from, what a citation to it must resolve to, and the three things the evaluation suite is built from: the cross-references, the retrieval distractors, and the declared out-of-corpus and near-miss topic lists.

## Documents

### `CFR-274A` — 8 CFR Part 274a, Control of Employment of Aliens

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-8/chapter-I/subchapter-B/part-274a |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-8.xml?part=274a` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 274a.1, 274a.2, 274a.10, 274a.13, each in full |
| Pages | 17 |
| Anchor | Section number. The eCFR structural API has no pagination, so a citation resolves to a section, not a page. |
| Backs | R1–R4 |

The controlling text. § 274a.2 is the heart of it: who must complete which part of the Form I-9 and by when, what documents may be accepted, the receipt rule, the reverification duty at (b)(1)(vii), and the retention formula. § 274a.13 carries the automatic-extension provisions, split at (d) and (e) around the 30 October 2025 boundary. § 274a.10 carries the penalty structure. § 274a.1 supplies the definitions of *hire*, *employee* and *knowing* that the other three depend on.

Excluded: §§ 274a.3–274a.9, 274a.12 and 274a.14. § 274a.12 (classes of aliens authorized to accept employment) is 34,000 characters of category codes and would have doubled the document to serve a determination the system does not make.

### `M-274` — USCIS Handbook for Employers M-274

| | |
|---|---|
| `doc_type` | `handbook` |
| Source | https://www.uscis.gov/i-9-central/form-i-9-resources/handbook-for-employers-m-274 |
| Retrieved | 13 August 2026 |
| Excerpted | §§ 4.4, 5.1, 6.1, 7.1, 9.0, 10.0, 11.2, 13.2 |
| Pages | 12 |
| Anchor | Handbook section number, as printed in the section heading. |
| Backs | R1–R4 |

USCIS's applied reading — the procedural layer between the regulation and the determination. § 6.1 and § 7.1 together carry the rule the whole exercise turns on: permanent residence does not lapse when the card does, so a Permanent Resident Card is never reverified. § 5.1 explains how an automatic extension is computed. § 9.0 distinguishes a defect that correction cures from one it does not. § 11.2 is the anti-discrimination material the third worker grounds in.

The handbook is published only as HTML; there is no PDF edition. It is scraped page by page and re-rendered, which is why `fetch_corpus.py` carries a configurable content selector.

### `I9-INSTR` — Instructions for Form I-9

| | |
|---|---|
| `doc_type` | `instructions` |
| Source | https://www.uscis.gov/i-9 |
| PDF | `https://www.uscis.gov/sites/default/files/document/forms/i-9instr.pdf` |
| Edition | 01/20/25 |
| Excerpted | All 8 pages |
| Pages | 8 |
| Anchor | Printed page number, 1–8, which matches the PDF page number. |
| Backs | R1–R4 |

The document an employer actually reads. It states the three-business-day rule, the retention formula and — at the reverification heading — the do-not-reverify list in the plainest language anywhere in the corpus: *"Reverification does not apply to List B documentation."*

Served as an AES-encrypted PDF. `pypdf` cannot open it without `cryptography` installed, which is why the documented dependency set uses `pypdf[crypto]`.

### `FR-EAD` — 90 FR 48800, Removal of the Automatic Extension of Employment Authorization Documents

| | |
|---|---|
| `doc_type` | `preamble` |
| Source | https://www.federalregister.gov/documents/2025/10/30/2025-19702 |
| PDF | `https://www.govinfo.gov/content/pkg/FR-2025-10-30/pdf/2025-19702.pdf` |
| Published | 30 October 2025 |
| Excerpted | Printed pp. 48800–48812 (PDF pp. 2–14): legal framework, the history of the automatic extension, the discussion of the interim final rule, and the description of regulatory changes |
| Pages | 13 |
| Anchor | Federal Register page number. The excerpt is one contiguous run renumbered from 1, so shipped page *n* is printed page *n* + 48799 — shipped pp. 1–13 are printed 48800–48812. |
| Backs | R2 |

The rulemaking record behind § 274a.13(e) — why the automatic extension ended, and what happens to renewal applications filed on either side of 30 October 2025. Excluded: pp. 48813–48820, the regulatory-analysis appendices (Regulatory Flexibility Act, Unfunded Mandates, the executive-order reviews), which carry no interpretive weight for R2.

### `IER-PACK` — DOJ Immigrant and Employee Rights Section guidance

| | |
|---|---|
| `doc_type` | `interpretation` |
| Source | https://www.justice.gov/crt/immigrant-and-employee-rights-section |
| Retrieved | 13 August 2026 |
| Excerpted | Four pages: LPR employment rights, Form I-9 and E-Verify, the IER FAQs, and worker information |
| Pages | 16 |
| Anchor | Page label (`LPR`, `I9-EV`, `FAQ`, `WORKER`) and page title. |
| Backs | R2 |

The enforcement perspective, and the only place in the corpus that says what happens when an employer applies the general rule to a document the carve-back protects: *"Reverifying Permanent Resident Cards may constitute a violation of the anti-discrimination provision of the INA."* This is the second hop of cross-reference 3 and the ground for the Documentary Practice Worker.

Two properties of this document to know before writing golden cases. The FAQ page opens with a jump-link table of contents, so roughly 60 of its 127 paragraphs are questions with no answer attached, and the answers follow further down — see distractor 5. And DOJ labels its technical assistance letters as retained *for historical purposes only*; those letters are deliberately **not** in this corpus, and only current guidance pages are.

### `FORM-I9` — Form I-9, Employment Eligibility Verification

| | |
|---|---|
| `doc_type` | `form` |
| Source | https://www.uscis.gov/i-9 |
| PDF | `https://www.uscis.gov/sites/default/files/document/forms/i-9.pdf` |
| Edition | 01/20/25 |
| Excerpted | All 4 pages: the form, the Lists of Acceptable Documents, Supplement A, Supplement B |
| Pages | 4 |
| Anchor | Page number, 1–4, by the page's own title. |
| Backs | R2, R3 |

The form itself. Page 2, the Lists of Acceptable Documents, is a three-column table and is the reason table extraction is a graded item on this project — a List A entry misread into the List B column changes a valid I-9 into an invalid one. Page 4, Supplement B, is where reverification is recorded and is therefore the artifact that shows whether a prohibited reverification actually happened.

Page 1 is also the blank the four audit packets are built on.

## Recorded cross-references

Multi-hop retrieval is only real if a claim genuinely lives across two documents. Each of these has been confirmed present at both ends.

| # | From | To | The hop |
|---|---|---|---|
| 1 | `CFR-274A` § 274a.2(b)(1)(vii) | `I9-INSTR` reverification | The regulation states a flat duty — *"If an individual's employment authorization expires, the employer... must reverify"* — and the instructions carve out the documents it does not reach. A worker that stops at the regulation reverifies a green card. |
| 2 | `M-274` § 7.1 | `I9-INSTR` reverification | The handbook restates the carve-out and supplies the reason the instructions omit: permanent residence does not expire when the card does. |
| 3 | `IER-PACK` LPR | `M-274` § 7.1 | Acting on the general rule is not merely unnecessary but unlawful. Only IER says so; the handbook stops at "should not". |
| 4 | `FR-EAD` preamble | `CFR-274A` § 274a.13(d), (e) | The preamble is the rulemaking record for the 30 October 2025 split as codified. The date appears 27 times in the preamble and twice in the regulation. |
| 5 | `M-274` § 5.1 | `CFR-274A` § 274a.13(d) | The handbook's extension arithmetic implements the regulation's 540-day cap; neither states the whole rule alone. |
| 6 | `FORM-I9` Lists of Acceptable Documents | `M-274` § 13.2 | The form's column layout establishes that List B is identity only; the handbook explains why that means List B never triggers reverification. |

Cross-references 1, 2 and 3 are the chain the golden set must exercise, because each is a case where retrieving one end and stopping produces a confidently wrong answer — and in this corpus the wrong answer is itself a violation.

## Retrieval distractors

Queries whose naive keyword match lands on the wrong section. At least one golden case must be built on each of the first three.

| Term | Why it misleads | Where it appears |
|---|---|---|
| `reverif` | The stem covers both the duty and its prohibition, in near-identical language, with no lexical signal separating them | 110 total — `M-274` 28, `I9-INSTR` 24, `IER-PACK` 23, `FR-EAD` 14, `FORM-I9` 12, `CFR-274A` 9 |
| `expired` | Appears where reverification is required, where it is forbidden, and where a document is merely evidence of a lapsed extension | 89 total — `FR-EAD` 27, `IER-PACK` 24, `CFR-274A` 19, `M-274` 13, `FORM-I9` 3, `I9-INSTR` 3 |
| `540 days` | The automatic-extension period, which now applies only to renewal applications filed before 30 October 2025. Most occurrences describe the superseded regime | 30 total — `FR-EAD` 24, `M-274` 4, `CFR-274A` 2 |
| `list b` | Identity-only documents that look like documents subject to expiry and reverification, and are not | 39 total — `I9-INSTR` 13, `M-274` 13, `IER-PACK` 7, `FORM-I9` 5, `CFR-274A` 1 |
| IER FAQ jump links | The FAQ page repeats each of its ~60 questions as a table-of-contents entry before answering any of them, so a question-shaped query can retrieve a chunk containing the question and no answer | `IER-PACK` |

Counts are reported by `fetch_corpus.py` on every full rebuild. Transcribe them here when an upstream source shifts.

## Declared out-of-corpus topics

Refusal test cases draw from this list. Every topic here has been confirmed to have **zero occurrences** across all six documents, so a grounded answer is impossible and a refusal is the only correct outcome. `fetch_corpus.py` re-checks each one on every full rebuild and fails the build if any of them turns up — reading the search terms from `sources.json`'s `verification.out_of_corpus`, not from this file. The list below is a readable transcription of that array, and the two must be kept in step: a topic that appears here and not there is never checked, and the build will pass while the claim above is false.

- Minimum wage
- Family and medical leave
- Workers' compensation
- Unemployment insurance
- Occupational safety
- Prevailing wage determinations
- Child labor restrictions
- Drug testing
- Sexual harassment
- Non-compete agreements
- Wage garnishment
- Non-immigration: GDPR and data protection
- Non-immigration: Sarbanes-Oxley and financial audit
- Non-immigration: HIPAA

> Overtime, collective bargaining, pensions, severance and independent-contractor status each appear somewhere in the corpus in passing — the first two were drafted onto this list and removed when the build caught them. They are **not** valid refusal topics: a refusal case built on one of them tests the wrong thing, because a retriever that surfaces the passing mention is behaving correctly.

## Near-miss topics

Covered by the corpus but easy to over-refuse. At least one golden case must confirm these are answered, not refused. `fetch_corpus.py` fails the build if one of them goes missing, because a near-miss case built on an absent topic can never fail.

- Conditional residents — `I9-INSTR`, and again in `M-274` § 7.1 and `IER-PACK`
- Temporary Protected Status — `CFR-274A` § 274a.13, `FR-EAD`, `M-274` § 5.1, `IER-PACK`
- Asylees — `FR-EAD`, `I9-INSTR`, `M-274`, `IER-PACK`
- Supplement B and the rehire path — `FORM-I9` p. 4, `I9-INSTR`, `M-274` § 6.1

## Drift note

This corpus sits on unusually active ground and one part of it is dated by design.

The automatic extension of employment authorization documents changed three times in two years: a temporary rule in April 2024 raising the period to 540 days, a final rule in December 2024 making that permanent, and the interim final rule of 30 October 2025 that removed it prospectively. The current regulation therefore splits at that date — § 274a.13(d) governs renewal applications filed before it, § 274a.13(e) those filed on or after. `FR-EAD` is the record of the third change, and R2 is written against the split.

Two consequences. Any rebuild that produces a § 274a.13 without paragraph (e) means the ground has moved again and R2's boundary needs rechecking before the golden set is trusted. And `540 days` is in the distractor list precisely because most of its occurrences describe a regime that no longer applies to new filings.

`CFR-274A` is pinned to an eCFR issue date and will reproduce exactly. The USCIS and DOJ pages are not version-pinned; if a rebuild changes page counts, diff `text/` before assuming the excerpt ranges in `sources.json` are still correct.
