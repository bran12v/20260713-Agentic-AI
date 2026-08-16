# Claimpath corpus manifest

Six documents, 90 pages, 49,333 words. Retrieved 14 August 2026. eCFR issue date 4 August 2026.

Every document is federal public-domain material. This file records where each came from, what a citation to it must resolve to, and the three things the evaluation suite is built from: the cross-references, the retrieval distractors, and the declared out-of-corpus and near-miss topic lists.

## Documents

### `CFR-412` — 42 CFR Part 412, Prospective Payment Systems for Inpatient Hospital Services

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-412 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-42.xml?part=412` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 412.1, 412.2, 412.3, 412.4 |
| Pages | 10 |
| Anchor | Section number and paragraph. The eCFR structural API has no pagination. |
| Backs | R1 |

The controlling text on admission status. § 412.1 states the scope of the prospective payment system and what it does and does not cover, § 412.2 the basis of payment, § 412.4 discharges and transfers. § 412.3 is the whole determination.

**§ 412.3(d) is the trap, and it has three layers.**

The general rule at **(d)(1)** is that an inpatient admission is generally appropriate for payment under Part A "when the admitting physician **expects** the patient to require hospital care that **crosses two midnights**". The test is the physician's expectation at the time of admission. It is **not** a count of midnights actually spent, and a determination built on the actual duration of the stay has answered a question the regulation does not ask.

Three provisions carve at that rule from different directions:

- **(d)(1)(i)** — the expectation must rest on complex medical factors, and "the factors that lead to a particular clinical expectation **must be documented in the medical record in order to be granted consideration**." An expectation that is real but undocumented gets no weight.
- **(d)(1)(ii)** — where an unforeseen circumstance such as death or transfer produces a shorter stay than the physician expected, the patient "may be considered to be appropriately treated on an inpatient basis". The expectation survives the stay being cut short.
- **(d)(2)** — a procedure on the inpatient-only list at § 419.22(n) is appropriate "**regardless of the expected duration of care**", which removes the two-midnight question entirely.
- **(d)(3)** — even where the physician expects a stay shorter than 2 midnights, an inpatient admission may still be appropriate "based on the clinical judgment of the admitting physician and medical record support for that determination".

So a one-midnight stay can be correctly inpatient by three separate routes, and a three-midnight stay can be incorrectly inpatient if the expectation was never documented.

> **§ 419.22(n) is named but not carried.** § 412.3(d)(2) turns on whether a procedure is on the inpatient-only list, and that list is in Part 419, which is not in this corpus. The system must cite § 412.3(d)(2) for the *rule* and refuse to assert whether any particular procedure is on the list. This is a deliberate corpus gap, not an oversight.

### `CFR-405` — 42 CFR Part 405 Subpart I, Determinations and Appeals

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-I |
| Excerpted | §§ 405.904, .921, .924, .926, .940, .942, .946, .948, .960, .962, .966, .968, .970, .1002, .1006 |
| Pages | 19 |
| Anchor | Section number and paragraph. |
| Backs | R2, R3 |

The appeal ladder in regulation. § 405.904 lays out the five levels, §§ 405.940–.970 govern redetermination and reconsideration, §§ 405.1002–.1006 the ALJ hearing and its amount in controversy.

**Three provisions here are load-bearing and all are easy to flatten.**

**§ 405.924 and § 405.926 are a matched pair, and neither is closed.** § 405.924 says what an initial determination *is* — paragraph (b) covers claims for benefits under Part A and Part B, which is where a denied inpatient claim lands — and it qualifies its own list with "includes, but is not limited to". It also carries an inline exclusion pointing at § 424.32, which is in Part 424 and **not carried by this corpus**; a packet that puts the validity of the claim submission in question cannot be resolved here.

**§ 405.926 looks like a closed list and is not.** It enumerates actions that are not initial determinations and are therefore unappealable, in paragraphs (a) through (j) — but it opens "Actions that are not initial determinations and are not appealable under this subpart **include, but are not limited to** the following". A rule that treats the enumeration as exhaustive, and returns `appealable` for anything absent from it, has misread the section's own first sentence. Set membership is sufficient to establish unappealability and is **not** necessary.

**§ 405.942(a) runs its clock from receipt, and receipt is presumed.** A request for redetermination must be filed "within **120 calendar days** from the date a party **receives** the notice of the initial determination", and (a)(1) provides that "the date of receipt of the initial determination will be **presumed to be 5 calendar days after the date of the notice** of initial determination, **unless there is evidence to the contrary**."

The presumption is rebuttable in both directions. Where the file records an actual receipt date, that governs; where it does not, the deadline is the notice date plus 125 calendar days, not plus 120. A rule that computes 120 days from the notice date is five days early on every claim, and a rule that hard-codes 125 ignores the evidence when it exists.

### `FR-2013` — 78 FR 50496, the FY2014 IPPS final rule

| | |
|---|---|
| `doc_type` | `preamble` |
| Source | https://www.federalregister.gov/documents/2013/08/19/2013-18956/ |
| PDF | `https://www.govinfo.gov/content/pkg/FR-2013-08-19/pdf/2013-18956.pdf` |
| Published | 19 August 2013 |
| Excerpted | Printed pp. 50941–50955, hospital inpatient admission and medical review criteria |
| Pages | 15 |
| Anchor | Federal Register page number, printed in the running head. The excerpt is one contiguous run renumbered from 1, so shipped page *n* is printed page *n* + 50940 — shipped pp. 1–15 are printed 50941–50955. |
| Backs | R1 |

Where § 412.3(d) came from and what CMS meant by it. This is the rulemaking that created the two-midnight framework, and it is the only document in the corpus that explains the reasoning: why a time-based benchmark at all, what the benchmark presumes, how the review contractors were told to apply it, and what CMS said in response to the comments arguing it was arbitrary.

The excerpt is the densest document in the corpus — 17,555 words across 15 pages of three-column Federal Register text — and it is the natural second hop for any question about *why* the rule reads as it does. § 412.3 states the rule in nine paragraphs and explains nothing.

### `IOM-INPATIENT` — Medicare Benefit Policy Manual, Chapter 1

| | |
|---|---|
| `doc_type` | `manual` |
| Source | https://www.cms.gov/medicare/regulations-guidance/manuals/internet-only-manuals-ioms |
| PDF | `https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/bp102c01.pdf` |
| Excerpted | Printed pp. 4–18, inpatient hospital services covered under Part A |
| Pages | 15 |
| Anchor | Manual section number, in the form 10.2, 10.3. |
| Backs | R1 |

CMS instructing its own contractors on how the admission determination is made. It covers what makes a service an inpatient hospital service, the practitioner order and who may furnish it, the physician certification requirements, and the relationship between the order and the expectation.

This is the operational reading of § 412.3(a)–(c), and it is where the order requirement is spelled out at a level the regulation does not reach.

### `IOM-APPEALS` — Medicare Claims Processing Manual, Chapter 29

| | |
|---|---|
| `doc_type` | `manual` |
| Source | https://www.cms.gov/medicare/regulations-guidance/manuals/internet-only-manuals-ioms |
| PDF | `https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c29.pdf` |
| Excerpted | Printed pp. 4–20, the glossary through the time limits for filing |
| Pages | 17 |
| Anchor | Manual section number, in the form 230, 240.1. |
| Backs | R2, R3 |

The appeal ladder as CMS operates it, and **the table-heavy document of this corpus**.

**CHART 1 — The Medicare Fee-for-Service Appeals Process** is a three-column table associating each of the five appeal levels with its filing deadline and its monetary threshold. **CHART 2 — Where to File an Appeal** is a four-column table associating each level with the entity that receives the request, split by Part A, Part B and DME. A chunker that captures the cells without preserving which deadline belongs to which level has produced something worse than nothing, because it looks like an answer.

Two details in CHART 1 matter beyond the deadlines:

- The footnote — where a party requests QIC review of a contractor's **dismissal** of a redetermination request, the filing limit is **60 days**, not the 180 that applies to a reconsideration on the merits.
- **The amount-in-controversy column does not contain the amounts.** For the ALJ and federal court levels it carries a URL to CMS.gov instead, because the figures are adjusted annually. The dollar thresholds are therefore **not in this corpus** and a system that supplies one has invented it. § 405.1006 states the requirement; neither document states the current number.

### `MANUAL-ABN` — Medicare Claims Processing Manual, Chapter 30 § 50

| | |
|---|---|
| `doc_type` | `manual` |
| Source | https://www.cms.gov/medicare/forms-notices/beneficiary-notices-initiative/ffs-abn |
| PDF | `https://www.cms.gov/files/document/medicareclaimsprocessingmanualch30sec50abnpdf` |
| Excerpted | Printed pp. 1–14, the scope of the ABN through effective delivery |
| Pages | 14 |
| Anchor | Manual section number, in the form 50.3, 50.6.1. |
| Backs | R4 |

The Advance Beneficiary Notice of Noncoverage, Form CMS-R-131 — the notice that shifts financial liability to the beneficiary under § 1879 of the Act, and the conditional third leg's only ground.

This section specifies the form rather than reproducing it: the ten lettered blanks (A) through (J), what goes in each, who may complete which, the delivery requirements, and what makes a notice defective. Two rules govern the packets:

- **Blanks (G)–(I) must be completed by the beneficiary or their representative when the notice is issued and "may never be pre-filled."** A provider that pre-prints the option selection has issued a defective notice.
- **Insertions "may be typed or legibly hand-written."** Legibility is a stated requirement of the form itself, which is why the handwritten packet artifact belongs here.

A defective ABN does not shift liability. That makes ABN validity a determination in its own right, separate from whether the service was covered.

## Recorded cross-references

Multi-hop retrieval is only real if a claim genuinely lives across two documents. Each of these has been confirmed present at both ends.

| # | From | To | The hop |
|---|---|---|---|
| 1 | `FR-2013` two-midnight discussion | `CFR-412` § 412.3(d) | The preamble explains what the benchmark presumes and why; the regulation states it in nine paragraphs and explains nothing. `412.3` appears 11 times in the preamble. |
| 2 | `CFR-412` § 412.3(a) | `IOM-INPATIENT` practitioner order | The regulation requires an order by a qualified practitioner; the manual is where who may furnish it, and when, is actually spelled out. |
| 3 | `IOM-APPEALS` CHART 1 | `CFR-405` §§ 405.942, .962, .1002 | The chart states each level's deadline operationally; the regulation states the same deadlines with the receipt presumption the chart omits. |
| 4 | `IOM-APPEALS` amount-in-controversy column | `CFR-405` § 405.1006 | The chart points to a URL for the figure; the regulation states the requirement. Neither states the number, and that is the point. |
| 5 | `MANUAL-ABN` liability shift | `CFR-405` and `IOM-APPEALS` § 1879 | Whether the beneficiary is liable and whether the denial is appealable are different questions arising from the same notice. `1879` appears in three of the six documents — `MANUAL-ABN` 8, `IOM-APPEALS` 4, `CFR-405` 3. |
| 6 | `CFR-412` § 412.3(d)(2) | *(§ 419.22(n), absent)* | The inpatient-only exception names a list this corpus does not carry. The correct behaviour is to cite the rule and refuse the list. |

Cross-references 1 and 3 are the chain the golden set must exercise. Cross-reference 6 is a deliberate dead end and must be exercised as a refusal.

## Retrieval distractors

Queries whose naive keyword match lands on the wrong section, or on nothing. At least one golden case must be built on each of the first three.

| Term | Why it misleads | Where it appears |
|---|---|---|
| `2-midnight` | The trap's own term — and the corpus spells it **four different ways**. See below; this is the sharpest retrieval hazard in the bank | 58 total, all in `FR-2013` |
| `inpatient` | Appears 492 times across five documents and discriminates nothing. It is in the title of two of them. An unfiltered query on it returns the corpus | 492 total — `FR-2013` 312, `IOM-INPATIENT` 98, `CFR-412` 78, `IOM-APPEALS` 2, `CFR-405` 2 |
| `medical necessity` | The phrase every practitioner uses, but the operative statutory phrase is **"reasonable and necessary"**, which appears more often and in different documents. A query on the colloquial term misses the regulation entirely | 26 total — `IOM-INPATIENT` 12, `FR-2013` 11, `IOM-APPEALS` 1, `MANUAL-ABN` 1, `CFR-405` 1. Against `reasonable and necessary` at 36 — `FR-2013` 19, `MANUAL-ABN` 11, `CFR-405` 3 |
| `redetermination` | One level of five, and the only one most queries name. 97 occurrences make it look central when it is the first rung | 97 total — `CFR-405` 54, `IOM-APPEALS` 43 |

**The spelling problem is this corpus's defining structural distractor, and it is worse than a hyphen.** The phrase every practitioner, every trade publication and every hospital policy uses is **"the two-midnight rule"**. That exact string appears **zero times** in this corpus. What the documents actually contain:

| Spelling | Count | Where |
|---|---|---|
| `2 midnights` | 69 | `FR-2013` 67, `CFR-412` 2 |
| `2-midnight` | 58 | `FR-2013` 58 |
| `two midnights` | 4 | `IOM-INPATIENT` 3, `CFR-412` 1 |
| `two-midnight` | **0** | — |

**§ 412.3 uses both spellings inside itself.** Paragraph (d)(1) says the physician "expects the patient to require hospital care that crosses **two midnights**"; (d)(1)(ii) refers to "the physician's expectation of at least **2 midnights**"; (d)(3) to a stay that "does not cross **2 midnights**". A term-match query on either spelling misses part of the single section that governs the determination.

The same hazard recurs on the clocks. The regulation writes **"120 calendar days"** and **"60 calendar days"**; the manual writes **"120 days"** and **"60 days"**. Neither wording finds the other.

Counts are reported by `fetch_corpus.py` on every full rebuild. Transcribe them here when an upstream source shifts.

## Declared out-of-corpus topics

Refusal test cases draw from this list. Every topic here has been confirmed to have **zero occurrences** across all six documents, so a grounded answer is impossible and a refusal is the only correct outcome. `fetch_corpus.py` re-checks each one on every full rebuild and fails the build if any of them turns up — reading the search terms from `sources.json`'s `verification.out_of_corpus`, not from this file. The list below is a readable transcription of that array, and the two must be kept in step: a topic that appears here and not there is never checked, and the build will pass while the claim above is false.

- Minimum wage
- Family and medical leave
- Workers' compensation
- Hazardous waste
- Sexual harassment
- Non-compete agreements
- Prevailing wage
- Child labor
- Drug testing
- Age discrimination
- Non-healthcare: GDPR and data protection
- Non-healthcare: Sarbanes-Oxley and financial audit
- Healthcare but not carried: the anti-kickback statute
- Healthcare but not carried: the Stark Law
- Healthcare but not carried: EMTALA
- Healthcare but not carried: clinical trials

> **Two categories in scope for the domain are not carried here, and neither is a clean absence. Word those refusal cases with care.**
>
> **The inpatient-only list.** § 419.22(n) is named twice in `CFR-412` and twice in `FR-2013`, and `inpatient only` appears 5 times, because § 412.3(d)(2) turns on it. The list itself is in Part 419 and is not carried. A refusal case must ask whether a *named procedure* is on the list, not whether the exception exists.
>
> **HIPAA.** `hipaa` appears **5 times** — `CFR-405` 3, `IOM-APPEALS` 1, `MANUAL-ABN` 1 — because the appeal and notice rules reference the privacy and administrative-simplification provisions in passing. It was a candidate for this list and was removed after the rebuild caught it. Do not build a refusal case on HIPAA; the sibling Perimeter project carries that corpus.

An earlier draft of this list also carried **occupational safety**, which the verification pass rejected: § 412.1(a)(10) provides a payment adjustment for "domestic National Institute for **Occupational Safety** and Health approved surgical N95 respirators". A refusal case built on it would have failed for a reason unrelated to anything the corpus teaches.

## Near-miss topics

Covered by the corpus but easy to over-refuse. At least one golden case must confirm these are answered, not refused. `fetch_corpus.py` fails the build if one of them goes missing, because a near-miss case built on an absent topic can never fail.

- Observation — 35 occurrences; `FR-2013` 34, `CFR-405` 1. The outpatient alternative to admission, discussed throughout the preamble
- Inpatient only — 5 occurrences; `CFR-412` 3, `FR-2013` 2. The *exception* is covered even though the list is not
- Quality improvement organization — 4 occurrences; `IOM-INPATIENT` 2, `IOM-APPEALS` 1, `CFR-405` 1, plus `QIO` 5 times. Sparse, and the term most likely to be wrongly refused
- Amount in controversy — 31 occurrences; `CFR-405` 19, `IOM-APPEALS` 12. The *requirement* is covered even though the dollar figures are not

## Drift note

The two-midnight framework at § 412.3(d) has been stable since the FY2016 rulemaking added the case-by-case exception at (d)(3). The appeal ladder in Subpart I is older and more stable still.

Three cautions.

**The CMS Internet-Only Manuals are updated by transmittal, continuously, and the PDFs are served from stable URLs with unstable contents.** Each section carries its own revision line — `(Rev. 4380, Issued: 08-30-19, ...)` — so a diff of `text/` tells you which sections moved. Page ranges are the thing most likely to shift under you; check the first page of each excerpt after any rebuild that produces a diff.

**The amount-in-controversy figures are adjusted annually and are deliberately not in this corpus.** CHART 1 points to a CMS.gov URL rather than stating them. If a future revision of Chapter 29 inlines the numbers, the manifest's cross-reference 4 stops being a refusal case and becomes an ordinary lookup — which is a change to the evaluation suite, not just to the corpus.

**Manual guidance is not regulation.** `IOM-APPEALS`, `IOM-INPATIENT` and `MANUAL-ABN` are CMS instructing its contractors. They bind the contractors and describe CMS's reading; they are not the rule. Every determination should cite the manual **and** the regulation it implements, and § 16 makes that an acceptance item.
