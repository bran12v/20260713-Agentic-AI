# Vigil corpus manifest

Six documents, 91 pages, 31,641 words. Retrieved 14 August 2026. eCFR issue date 4 August 2026.

Every document is federal public-domain material. This file records where each came from, what a citation to it must resolve to, and the three things the evaluation suite is built from: the cross-references, the retrieval distractors, and the declared out-of-corpus and near-miss topic lists.

## Documents

### `CFR-803` — 21 CFR Part 803, Medical Device Reporting

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-21.xml?part=803` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 803.3, .10, .11, .12, .17, .19, .20, .50, .52, .53, .56, .58 |
| Pages | 18 |
| Anchor | Section number and paragraph. The eCFR structural API has no pagination. |
| Backs | R1, R2, R4 |

The controlling text. § 803.3 supplies the definitions the whole determination runs on — *malfunction*, *serious injury*, *caused or contributed*, *become aware*. § 803.50 states the manufacturer's obligation, § 803.52 what a report must contain, § 803.53 the five-work-day report, § 803.19 the exemptions.

**§ 803.50(a)(2) is the trap.** A manufacturer must report within 30 calendar days of information that reasonably suggests a device "has malfunctioned and this device or a similar device that you market **would be likely to cause or contribute to a death or serious injury, if the malfunction were to recur**".

The second prong is **entirely counterfactual**. It asks what recurrence would likely do, not what this occurrence did. A malfunction that harmed nobody is reportable whenever recurrence would likely be serious, and "no injury occurred" is not an answer to the question the regulation asks. Note also the evidentiary bar in the opening words — "reasonably suggests", not establishes.

### `CFR-807` — 21 CFR Part 807 Subpart E, Premarket Notification

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-E |
| Excerpted | §§ 807.81, .87, .90, .92, .93, .97, .100 |
| Pages | 9 |
| Anchor | Section number and paragraph. |
| Backs | R3 |

When a new premarket notification is required. **§ 807.81(a)(3)** is the operative test: a 510(k) is required for a change to a device already in commercial distribution where the change "could significantly affect the safety or effectiveness of the device" or is "a major change or modification in the intended use". § 807.87 sets the content of a submission and § 807.92 the summary.

Both limbs of (a)(3) are qualitative and neither carries a number. That is deliberate on FDA's part and it is why the guidance exists.

### `CFR-806` — 21 CFR Part 806, Reports of Corrections and Removals

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-806 |
| Excerpted | §§ 806.2, 806.10, 806.20, 806.30, 806.40 |
| Pages | 7 |
| Anchor | Section number and paragraph. |
| Backs | — (grounds the conditional worker) |

The third leg's only ground. § 806.10 requires a report of any correction or removal initiated to reduce a risk to health or to remedy a violation, **"within 10-working days of initiating such correction or removal"**, and § 806.20 lists the corrections and removals that need only be recorded rather than reported.

Note the spelling: the regulation writes **"10-working days"**, hyphenated between the numeral and the word. A literal query for "10 working days" returns nothing from this corpus.

### `GUID-510K` — FDA guidance on deciding when a change requires a new 510(k)

| | |
|---|---|
| `doc_type` | `guidance` |
| Source | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/deciding-when-submit-510k-change-existing-device |
| PDF | `https://www.fda.gov/media/99812/download` |
| Excerpted | Printed pp. 5–11, introduction through guiding principles; pp. 12–24, how to use the guidance and the labeling and technology flowcharts |
| Pages | 20 |
| Anchor | Guidance page number, which matches the PDF page. |
| Backs | R3 |

FDA's reading of § 807.81(a)(3), and the only thing in the corpus that turns a qualitative test into a procedure.

**It decides by flowchart.** Twelve of the twenty carried pages are decision diagrams — a change enters at the top, and a sequence of yes/no questions routes it to "document to file" or "submit a 510(k)". This is a harder extraction problem than a table: the logic is in the arrows, and a chunker that captures the boxes without the edges has captured nothing usable. Check what Document Intelligence returns for these pages before trusting any answer built on them.

Excluded: pp. 25–78, the materials-change flowcharts, the risk-assessment appendix and the worked examples.

### `GUID-MDR` — FDA guidance on medical device reporting for manufacturers

| | |
|---|---|
| `doc_type` | `guidance` |
| Source | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/medical-device-reporting-manufacturers |
| PDF | `https://www.fda.gov/media/86420/download` |
| Excerpted | Printed pp. 9–24, the purpose of the regulation and the manufacturer reporting requirements |
| Pages | 16 |
| Anchor | Guidance section number, in the form 2.1, 4.5.1. |
| Backs | R1, R2, R4 |

FDA answering the questions the regulation raises, in explicit question-and-answer form — *"2.1 What are the reporting requirements that apply to me as a manufacturer?"*. It restates the recurrence standard on its third page of substance, which makes it the natural second hop for any question about whether a harmless malfunction is reportable.

"malfunction" appears 68 times here against 16 in the regulation, so an unfiltered query about malfunctions answers from guidance rather than from the rule.

### `FORM-3500A` — Form FDA 3500A, MedWatch mandatory reporting

| | |
|---|---|
| `doc_type` | `form` |
| Source | https://www.fda.gov/safety/medical-product-safety-information/medwatch-forms-fda-safety-reporting |
| Excerpted | The nine-page form and the first twelve pages of its general instructions, assembled from two upstream PDFs |
| Pages | 21 |
| Anchor | Form block letter and item number, or instruction page. |
| Backs | R2, R4 |

The report itself, edition 09/2025. Block B carries the adverse event description and the date the reporter became aware; Block D the device identification; Block H the manufacturer's own evaluation and conclusion codes. The instructions explain each, and they are where the difference between an event date, a reporting date and an awareness date is spelled out — three dates a packet will conflate and a clock depends on.

## Recorded cross-references

Multi-hop retrieval is only real if a claim genuinely lives across two documents. Each of these has been confirmed present at both ends.

| # | From | To | The hop |
|---|---|---|---|
| 1 | `GUID-MDR` recurrence discussion | `CFR-803` § 803.50(a)(2) | The guidance explains what the recurrence standard asks; the regulation states it once and never elaborates. |
| 2 | `GUID-510K` flowcharts | `CFR-807` § 807.81(a)(3) | The guidance converts "could significantly affect" into a decision procedure; the regulation supplies the test the procedure implements. |
| 3 | `FORM-3500A` blocks | `CFR-803` § 803.52 | The form's blocks are the required content; only the regulation says what must be reported and by when. |
| 4 | `CFR-806` corrections | `CFR-803` remedial action | A field correction and an MDR are different obligations arising from the same facts; each part refers to the other's subject without stating it. |
| 5 | `GUID-MDR` five-day discussion | `CFR-803` § 803.53 | The five-work-day report has two triggers, and the guidance is where they are explained. |
| 6 | `GUID-510K` intended use | `CFR-807` § 807.81(a)(3) second limb | A major change in intended use is a separate trigger from a change affecting safety or effectiveness, and the guidance treats them separately. |

Cross-references 1 and 2 are the chain the golden set must exercise. They are also where the corpus is most guidance-heavy, which is exactly where the "cite the regulation too" rule matters.

## Retrieval distractors

Queries whose naive keyword match lands on the wrong section. At least one golden case must be built on each of the first three.

| Term | Why it misleads | Where it appears |
|---|---|---|
| `malfunction` | The trap's own word, and **guidance outweighs regulation four to one**. An unfiltered query answers from FDA's commentary rather than from § 803.50(a)(2), and the commentary is nonbinding | 87 total — `GUID-MDR` 68, `CFR-803` 16, `FORM-3500A` 3 |
| `serious injury` | Carries a defined meaning at § 803.3 and an ordinary one everywhere else, and appears in both reporting parts for different purposes | 66 total — `GUID-MDR` 39, `CFR-803` 22, `FORM-3500A` 3, `CFR-806` 2 |
| `510(k)` | 147 of 163 occurrences are in the guidance, which is a decision procedure, not the rule. The rule is seven words in § 807.81(a)(3) | 163 total — `GUID-510K` 147, `CFR-807` 14, `GUID-MDR` 1, `FORM-3500A` 1 |
| `significantly affect` | The operative phrase of the whole change determination, and it appears twice in the regulation against 45 times in the guidance discussing how to apply it | 47 total — `GUID-510K` 45, `CFR-807` 2 |

**A structural distractor, not a lexical one.** Part 806's clock is written **"10-working days"** with a hyphen between the numeral and the word. A literal query for "10 working days" returns nothing from this corpus, even though that is how every practitioner says it aloud. The same hazard has appeared in three other projects in this bank under different spellings; assume the corpus is inconsistent and search accordingly.

Counts are reported by `fetch_corpus.py` on every full rebuild. Transcribe them here when an upstream source shifts.

## Declared out-of-corpus topics

Refusal test cases draw from this list. Every topic here has been confirmed to have **zero occurrences** across all six documents, so a grounded answer is impossible and a refusal is the only correct outcome. `fetch_corpus.py` re-checks each one on every full rebuild and fails the build if any of them turns up — reading the search terms from `sources.json`'s `verification.out_of_corpus`, not from this file. The list below is a readable transcription of that array, and the two must be kept in step: a topic that appears here and not there is never checked, and the build will pass while the claim above is false.

- Minimum wage
- Family and medical leave
- Workers' compensation
- Occupational safety
- Hazardous waste
- Sexual harassment
- Non-compete agreements
- Prevailing wage
- Non-device: GDPR and data protection
- Non-device: Sarbanes-Oxley and financial audit
- Healthcare but not device: the anti-kickback statute

> **Two further categories must be refused because they are in scope for the domain and not carried here — but neither is a clean absence, so word the refusal cases with care.**
>
> **Premarket approval.** No Part 814 text is carried and the corpus covers the 510(k) pathway only, so nothing here can answer what a PMA supplement requires. But "premarket approval" appears **5 times** and "PMA" **5 times** across four documents, and "part 814" once, because the 510(k) documents distinguish the two pathways in passing. A refusal case must ask what a PMA supplement *requires*, not whether the pathway exists.
>
> **The quality system.** Part 820 is not carried. It was amended in 2024 to harmonise with ISO 13485 and now incorporates that standard by reference, which is copyrighted and could not be included even if the part were. But "820" appears **20 times** and "quality system" **4 times** in the two guidance documents, which carry a banner about the amendment. **"design control" is genuinely absent** — that is the clean refusal to build a case on.

## Near-miss topics

Covered by the corpus but easy to over-refuse. At least one golden case must confirm these are answered, not refused. `fetch_corpus.py` fails the build if one of them goes missing, because a near-miss case built on an absent topic can never fail.

Counts are for the singular stem the build actually checks, which is also the string to write a golden case against — the plural forms are four to seven times rarer and a case built on one searches a much smaller corpus than the figure below suggests.

- `user facility` — 62 occurrences; `CFR-803` 27, `FORM-3500A` 23, `GUID-MDR` 12
- `correction` — 36 occurrences, 27 of them in `CFR-806`
- `importer` — 88 occurrences; `FORM-3500A` 29, `CFR-803` 29, `CFR-806` 19, `GUID-MDR` 11
- `remedial action` — 25 occurrences, in `GUID-MDR` 16, `CFR-803` 7 and `FORM-3500A` 2. Not in `CFR-806`, which uses "correction" and "removal" instead

## Drift note

The reporting obligations here are stable; Part 803 has been substantially unchanged since the electronic submission requirements took effect in 2015.

Three cautions, and the first is the most likely to bite. **FDA guidance URLs are opaque numeric identifiers** at `fda.gov/media/<id>/download`, and FDA issues a revised guidance under a **new** identifier rather than updating the old one. Two of the three identifiers used in an earlier draft of this corpus resolved to entirely unrelated documents — a contraception video script and a urinary-tract-infection drug guidance — which is how the wrong document silently enters a corpus. Always read the first page of what came back.

**The quality system ground moved recently.** Both guidance documents carry a banner noting that FDA amended Part 820 in February 2024 to the Quality Management System Regulation, effective February 2026. That change is outside this corpus and the guidance predates it, so any statement here about quality system obligations is describing a superseded regime.

And **guidance is nonbinding.** Three of six documents say so on nearly every page. Nothing in this corpus grounded only in guidance establishes an obligation.
