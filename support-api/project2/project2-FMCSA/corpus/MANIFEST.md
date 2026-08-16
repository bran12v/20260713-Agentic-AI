# Roadwatch corpus manifest

Six documents, 84 pages, 44,622 words. Retrieved 13 August 2026. eCFR issue date 4 August 2026.

Every document is federal public-domain material. This file records where each came from, what a citation to it must resolve to, and the three things the evaluation suite is built from: the cross-references, the retrieval distractors, and the declared out-of-corpus and near-miss topic lists.

## Documents

### `CFR-395` — 49 CFR Part 395, Hours of Service of Drivers

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-49.xml?part=395` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 395.1, 395.2, 395.3, 395.5, 395.8, 395.13, each in full |
| Pages | 17 |
| Anchor | Section number, and paragraph letter where the determination turns on one. The eCFR structural API has no pagination. |
| Backs | R1–R3 |

The controlling text, and the document the whole exercise turns on. § 395.3 sets the property-carrying limits — 11 hours driving after 10 consecutive off at (a)(1)–(2), the 30-minute break at (a)(3)(ii), and the 60/70-hour weekly limits at (b). § 395.5 sets the different passenger-carrying limits. § 395.1(b)(1) grants the adverse driving conditions extension and § 395.2 defines what qualifies. § 395.8 governs the record of duty status itself, and § 395.13 covers drivers declared out of service.

Excluded: §§ 395.7, 395.10, 395.11, 395.12, 395.15–395.38. The electronic logging device technical specifications are a hardware conformance topic, not a determination the system makes.

### `CFR-391` — 49 CFR Part 391, Qualifications of Drivers

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-391 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-49.xml?part=391` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 391.11, 391.41, 391.43, 391.45, 391.51, each in full |
| Pages | 9 |
| Anchor | Section number. |
| Backs | R4 |

The second determination's ground. § 391.11 states the general qualification requirements, § 391.41 the physical standards a driver must meet, § 391.43 the examination that establishes them, § 391.45 who must be examined and when, and § 391.51 exactly what the driver qualification file must contain and how long each item is kept.

Excluded: § 391.23, the investigation and inquiry requirements, at 18,000 characters the largest section in the part and concerned with hiring rather than with whether a currently employed driver is qualified today.

### `HOS-GUIDE` — FMCSA Interstate Truck Driver's Guide to Hours of Service

| | |
|---|---|
| `doc_type` | `guide` |
| Source | https://www.fmcsa.dot.gov/regulations/hours-service/interstate-truck-drivers-guide-hours-service |
| PDF | `https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2022-04/FMCSA-HOS-395-DRIVERS-GUIDE-TO-HOS(2022-04-28)_0.pdf` |
| Edition | 28 April 2022 |
| Excerpted | Printed pp. 10–27: the rest break and restart, the adverse driving conditions exception, the short-haul exception, the record of duty status with a completed log grid, and Appendix A |
| Pages | 18 |
| Anchor | Printed page number. The excerpt starts at printed page 10 and is renumbered from 1, so printed page *n* is shipped page *n* − 9. |
| Backs | R1–R3 |

FMCSA's plain-language reading, and the operational layer between the regulation and the log sheet. Two parts of it carry weight the regulation does not. Printed page 18 — **shipped page 9** — reproduces **a completed log grid**, which is the only worked example in the corpus of what a compliant record of duty status actually looks like. And Appendix A, printed pp. 20–27 or shipped pp. 11–18, is a **multi-column exception table** — Category, Type of Exception, Conditions That Must Be Met, and the regulatory cite — which is the reason table extraction is a graded item on this project. An exception read out of the wrong row grants relief the regulation does not.

Excluded: pp. 1–9, the cover, table of contents, and the introduction to interstate commerce and on-duty time, all of which the regulation states more precisely.

### `FR-2020` — 85 FR 33396, Hours of Service of Drivers, final rule

| | |
|---|---|
| `doc_type` | `preamble` |
| Source | https://www.federalregister.gov/documents/2020/06/01/2020-11469/hours-of-service-of-drivers |
| PDF | `https://www.govinfo.gov/content/pkg/FR-2020-06-01/pdf/2020-11469.pdf` |
| Published | 1 June 2020 |
| Excerpted | Printed pp. 33412–33416 (PDF pp. 17–21), the comment analysis on adverse driving conditions; and pp. 33435–33438 (PDF pp. 40–43), the discussion of the final rule and the section-by-section analysis |
| Pages | 9 |
| Anchor | Federal Register page number. The excerpt is **two non-contiguous runs**, so no single offset works: shipped pp. 1–5 are printed 33412–33416, and shipped pp. 6–9 are printed 33435–33438. |
| Backs | R2 |

The rulemaking record for the adverse driving conditions exception as it now stands — what FMCSA was asked to change, what it changed, and what it deliberately did not. The phrase "adverse driving" appears 60 times in these nine pages against five times in the regulation itself, which is why the preamble is the second hop for any question about the exception's scope.

Excluded: the 40 pages of comment summary, regulatory impact analysis and executive-order reviews that carry no interpretive weight for R2.

### `GUIDE-PACK` — FMCSA regulatory guidance on the hours of service rules

| | |
|---|---|
| `doc_type` | `interpretation` |
| Source | https://www.federalregister.gov/agencies/federal-motor-carrier-safety-administration |
| Retrieved | 13 August 2026 |
| Excerpted | Six regulatory guidance documents published between 2010 and 2018 |
| Pages | 22 |
| Anchor | Federal Register citation, as printed in the section heading. |
| Backs | R1, R3 |

Six documents in which FMCSA states what a rule *means* when its text leaves a question open. This is the direct analogue to an interpretation letter, and the interpretive layer of this corpus.

FMCSA publishes regulatory guidance on its own website as HTML, and **`fmcsa.dot.gov/regulations/` returns HTTP 403 to every automated client at every user agent**. The same guidance is published in the Federal Register, which is not blocked, so that is where these come from.

Each resolves a different edge:

- **77 FR 33331** — the property-carrier limits in § 395.3 apply to a driver operating a vehicle *designed or used to transport passengers* on a driveaway-towaway trip. Being built to carry people does not by itself make the operation passenger-carrying.
- **78 FR 76757** — a driver who begins the day exempt from the 30-minute break as a short-haul driver, and exceeds the short-haul distance mid-day.
- **83 FR 26377** — when moving a commercial motor vehicle counts as off-duty personal conveyance rather than driving time.
- **83 FR 26374** — how far the agricultural commodity exception reaches, including unladen return trips.
- **75 FR 32860** — what satisfies the requirement to prepare the record of duty status in duplicate.
- **79 FR 39342** — a record of duty status produced by logging software is still the driver's own record.

Guidance is not regulation. Each of these states FMCSA's reading of a rule; none of them amends one, and each carries its own effective date. A claim grounded here should cite the guidance *and* the section it construes.

### `FORM-MER` — FMCSA Form MCSA-5875, Medical Examination Report

| | |
|---|---|
| `doc_type` | `form` |
| Source | https://www.fmcsa.dot.gov/medical/driver-medical-requirements/medical-applications-and-forms |
| PDF | `https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-04/Medical%20Examination%20Report%20Form%20MCSA-5875%20508pdf.pdf` |
| Excerpted | All 9 pages: the form at pp. 1–5, the completion instructions at pp. 6–9 |
| Pages | 9 |
| Anchor | Page number, 1–9. |
| Backs | R4 |

The form a medical examiner completes to certify a driver, and the artifact the qualification determination reads. Pages 2 and 3 are a **driver health history grid** — a column of conditions against yes/no boxes — which is the second table in the corpus that must survive extraction with its rows intact. Page 4 carries the examiner's determination and the certification period, which is the field R4 depends on.

## Recorded cross-references

Multi-hop retrieval is only real if a claim genuinely lives across two documents. Each of these has been confirmed present at both ends.

| # | From | To | The hop |
|---|---|---|---|
| 1 | `HOS-GUIDE` adverse driving conditions | `CFR-395` § 395.1(b)(1) | The guide says the exception gives "**Up to 2 additional hours**" — the numeral, three times. The regulation says "**two additional hours** *beyond the maximum allowable hours permitted under § 395.3(a) or § 395.5(a)*" — spelled out, once, and it names no other paragraph. The two ends do not share a spelling, so a query matched on either finds only one of them. That is the hop and the hazard in one row. |
| 2 | `FR-2020` discussion of the final rule | `CFR-395` § 395.1(b)(1) | The preamble is the rulemaking record for the exception's present scope, and states what FMCSA declined to extend. |
| 3 | `HOS-GUIDE` Appendix A | `CFR-395` § 395.1 | The exception table indexes the regulation's exemptions by category and cite; neither the table row nor the regulation states the whole condition alone. |
| 4 | `GUIDE-PACK` 77 FR 33331 | `CFR-395` §§ 395.3, 395.5 | The guidance says property-carrier limits govern a driveaway trip in a vehicle *designed or used to transport passengers*. Only the regulation supplies the two limit sets the guidance is choosing between. |
| 5 | `FORM-MER` examiner determination | `CFR-391` § 391.43 | The form implements the examination the regulation requires, and its certification period is the input R4 needs. |
| 6 | `CFR-391` § 391.41 | `FORM-MER` health history grid | The physical qualification standards are what the grid's rows test; the grid alone does not say which answer disqualifies. |

Cross-references 1 and 2 are the chain the golden set must exercise, because they are where retrieving one end and stopping produces a confidently wrong answer.

## Retrieval distractors

Queries whose naive keyword match lands on the wrong section. At least one golden case must be built on each of the first three.

| Term | Why it misleads | Where it appears |
|---|---|---|
| `adverse driving` | The exception, the definition that narrows it, the comment analysis of alternatives FMCSA rejected, and the regulatory-impact discussion all use it. The preamble outweighs the regulation twelve to one, so an unfiltered query answers from commentary rather than from the rule | 77 total — `FR-2020` 60, `HOS-GUIDE` 12, `CFR-395` 5 |
| `personal conveyance` | Off-duty movement of a commercial motor vehicle, which looks like driving time in every log and is not. The term appears **only** in the guidance, so a query that stays inside the regulation finds nothing and may wrongly refuse | 48 total — `GUIDE-PACK` 48 |
| `8 consecutive hours` | The off-duty period that resets a **passenger-carrying** driver under § 395.5. Property-carrying drivers need 10. A query that matches this phrase and stops has silently switched rule sets | 19 total — `CFR-395` 14, `FR-2020` 4, `HOS-GUIDE` 1 |
| `off-duty` | Spans the qualifying rest period, the sleeper-berth split, personal conveyance, and time that is merely not driving. Worse, the corpus is **inconsistently hyphenated** — 84 occurrences of `off-duty` against 58 of `off duty`, split unevenly by document, so a literal query for either form misses most of the corpus | 84 total — `CFR-395` 36, `GUIDE-PACK` 28, `FR-2020` 17, `HOS-GUIDE` 3 |

Counts are reported by `fetch_corpus.py` on every full rebuild. Transcribe them here when an upstream source shifts.

## Declared out-of-corpus topics

Refusal test cases draw from this list. Every topic here has been confirmed to have **zero occurrences** across all six documents, so a grounded answer is impossible and a refusal is the only correct outcome. `fetch_corpus.py` re-checks each one on every full rebuild and fails the build if any of them turns up — reading the search terms from `sources.json`'s `verification.out_of_corpus`, not from this file. The list below is a readable transcription of that array, and the two must be kept in step: a topic that appears here and not there is never checked, and the build will pass while the claim above is false.

- Minimum wage
- Overtime pay
- Family and medical leave
- Workers' compensation
- Unemployment insurance
- Collective bargaining
- Prevailing wage
- Sexual harassment
- Non-compete agreements
- Non-transport: GDPR and data protection
- Non-transport: Sarbanes-Oxley and financial audit
- Non-transport: HIPAA

> Driver pay, detention time and per-diem arrangements sit close to several of these and are **not** safe refusal topics — the corpus discusses compensation incentives in the preamble's comment analysis. Test a refusal on a topic from the list above, not on one that merely sounds like employment law.

## Near-miss topics

Covered by the corpus but easy to over-refuse. At least one golden case must confirm these are answered, not refused. `fetch_corpus.py` fails the build if one of them goes missing, because a near-miss case built on an absent topic can never fail.

- Sleeper berth splits — `CFR-395` § 395.1(g), and again in `HOS-GUIDE` and `FR-2020`
- The short-haul exception — `CFR-395` § 395.1(e), `HOS-GUIDE` pp. 14–15, `FR-2020`
- The 34-hour restart — `CFR-395` § 395.3(c), `HOS-GUIDE` pp. 10–11. Note the phrasing gap: the regulation says an off-duty period of **"34 or more consecutive hours"**, while the guide writes it three ways — "at least 34 consecutive hours", and twice as the bare quantity "34 consecutive hours". Only the regulation's form carries the inequality, so a query matched on the guide's bare phrasing retrieves text that reads like an exact figure. A rule that tests equality passes its own unit test and fails on every real restart longer than 34 hours
- Oilfield operations — `CFR-395` § 395.1(d), and in the `HOS-GUIDE` Appendix A table

## Drift note

Two things about this corpus will age differently.

`CFR-395` and `CFR-391` are pinned to an eCFR issue date and reproduce exactly. The hours-of-service limits themselves have been stable since the 2020 rule took effect, and R1 through R3 are written against them.

`GUIDE-PACK` is stable in a different way. Federal Register documents are permanent and their citations never move, so these six will fetch indefinitely. What can change is their *status*: FMCSA withdraws and supersedes guidance without amending the regulation, and a withdrawal notice is itself a Federal Register document that will not appear in this corpus. Before trusting a guidance-grounded answer in a later cohort, check whether the guidance still stands. The regulation is the authority; the guidance only construes it.
