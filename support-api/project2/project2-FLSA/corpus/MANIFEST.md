# Straighttime corpus manifest

Seven documents, 93 pages, 46,009 words. Retrieved 13 August 2026. eCFR issue date 4 August 2026.

Every document is federal public-domain material. This file records where each came from, what a citation to it must resolve to, and the three things the evaluation suite is built from: the cross-references, the retrieval distractors, and the declared out-of-corpus and near-miss topic lists.

Seven rather than six, because the FLSA splits its rules across four CFR parts that cannot be merged and are all load-bearing.

## Documents

### `CFR-541` — 29 CFR Part 541, the white-collar exemptions

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-A/part-541 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-29.xml?part=541` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 541.100, .101, .102, .200, .202, .203, .300, .301, .600, .601, .602, .604 |
| Pages | 16 |
| Anchor | Section number and paragraph. The eCFR structural API has no pagination. |
| Backs | R1 |

The exemption test, in its two halves. §§ 541.100, 541.200 and 541.300 give the executive, administrative and professional duties tests, with §§ 541.102, 541.202 and 541.301 elaborating them. § 541.600 sets the salary level at **$684 per week**; § 541.601 sets the highly compensated threshold at **$107,432**; § 541.602 states the salary basis rule and, critically, which deductions destroy it; § 541.604 covers extra compensation on top of a salary.

### `CFR-778` — 29 CFR Part 778, the regular rate

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-B/part-778 |
| Excerpted | §§ 778.107, .108, .114, .200, .208, .209, .211, .212, .215, .221, .223, .224 |
| Pages | 15 |
| Anchor | Section number and paragraph. |
| Backs | R2, R4 |

§ 778.107 opens the part with the general standard R4 applies — overtime at not less than one and one-half times the regular rate for hours worked over 40 in a workweek. Everything else in the part exists to decide what the regular rate *is*.

**§ 778.211 is the trap.** Section 7(e)(3) lets an employer exclude a bonus from the regular rate only if **both** the fact of payment **and** the amount are at the employer's sole discretion until near the end of the period, and not paid pursuant to any prior contract, agreement or promise. Paragraph (c) then rules out anything "promised to employees upon hiring", anything resulting from collective bargaining, and anything "announced to employees to induce them to work more steadily or more rapidly or more efficiently or to remain with the firm".

And paragraph (d) says it outright: **"Labels are not determinative."** A payment called a discretionary bonus on the payroll register is not one because it says so.

§ 778.208 states the general rule that bonuses go into the rate; § 778.212 covers gifts; § 778.215 the bona fide benefit plan exclusion; §§ 778.221–.224 the other § 7(e) exclusions. § 778.114 is the fluctuating workweek method.

### `CFR-785` — 29 CFR Part 785, hours worked

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-B/part-785 |
| Excerpted | §§ 785.11–.14, .16, .18, .19, .27–.29, .33, .35, .38, .39, .47 |
| Pages | 15 |
| Anchor | Section number. |
| Backs | R3 |

What counts as time worked. Waiting time (§§ 785.14–.16), rest and meal periods (§§ 785.18–.19), lectures and training (§§ 785.27–.29), home-to-work and travel-away-from-home (§§ 785.35, .38, .39), and the **de minimis** rule at § 785.47 that a system computing compensable minutes has to know about before it starts adding them up.

### `CFR-553` — 29 CFR Part 553 Subpart C, public safety employees

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-A/part-553/subpart-C |
| Excerpted | §§ 553.201, .210, .211, .212, .230, .233 |
| Pages | 7 |
| Anchor | Section number. |
| Backs | — (grounds the conditional worker) |

The § 7(k) partial exemption, and the third leg's only ground. § 553.201(a) confines the exemption to employees of public agencies, and § 553.210 then defines who is "engaged in fire protection activities" — a three-part conjunction of suppression training, legal authority to suppress, and employment by a fire department of a municipality, county, fire district or State, with paragraph (b) excluding a department's civilian staff. Between them they are the dispatch predicate. **§ 553.230 carries the corpus's one real table**: a 22-row mapping from work-period length, 7 to 28 days, onto the maximum hours before overtime is owed — 212 hours over 28 days for fire protection, 171 for law enforcement, scaling down proportionally. § 553.212 sets the 20 percent limit on non-exempt work.

### `FR-2019` — 84 FR 51230, the rulemaking that set the current salary level

| | |
|---|---|
| `doc_type` | `preamble` |
| Source | https://www.federalregister.gov/documents/2019/09/27/2019-20353/defining-and-delimiting-the-exemptions-for-executive-administrative-professional-outside-sales-and |
| PDF | `https://www.govinfo.gov/content/pkg/FR-2019-09-27/pdf/2019-20353.pdf` |
| Published | 27 September 2019 |
| Excerpted | Printed pp. 51230–51235 (PDF 1–6) and pp. 51246–51251 (PDF 17–22) |
| Pages | 12 |
| Anchor | Federal Register page number. The excerpt is **two non-contiguous runs**, so no single offset works: shipped pp. 1–6 are printed 51230–51235, and shipped pp. 7–12 are printed 51246–51251. |
| Backs | R1 |

Why $684, how the Department derived it, the special salary tests for the territories, the highly compensated test, and the rule that **nondiscretionary** bonuses may count toward up to 10 percent of the salary level.

That last point is worth pausing on, because it runs opposite to the trap. The same nondiscretionary bonus that **counts toward** the salary threshold under § 541.602(a)(3) must also be **included in** the regular rate under § 778.208 — while a genuinely discretionary bonus does neither. One payment, two tests, and the answer is the same word in both but for opposite reasons.

**The 2024 rulemaking is deliberately absent.** It raised the threshold in stages and was vacated nationwide before the later increases took effect; the current text reverts to the 2019 figures. Carrying its preamble would place a persuasive account of numbers that are not law directly beside the regulation.

### `WHD-OPS` — Wage and Hour Division opinion letters

| | |
|---|---|
| `doc_type` | `interpretation` |
| Source | https://www.dol.gov/agencies/whd/opinion-letters/flsa |
| Excerpted | Six letters, assembled from six upstream PDFs |
| Pages | 26 |
| Anchor | Letter number, as printed in the section heading. |
| Backs | R1–R3 |

The closest thing in this bank to a true interpretation letter, because that is exactly what these are: the Division answering one employer's or employee's specific facts, in writing, over a signature.

| Letter | What it resolves |
|---|---|
| FLSA2026-2 | Whether § 7(e) permits excluding particular bonus payments from the regular rate, and how to include them if not |
| FLSA2025-04 | Whether "emergency pay" to firefighters can be excluded from the regular rate — the one letter that touches both the trap and the § 7(k) leg |
| FLSA2026-1 | Reclassification from exempt to non-exempt where the employee believes the learned professional duties are still met |
| FLSA2026-5 | An exempt employee taking a secondary non-exempt role at an hourly rate, and the overtime consequences |
| FLSA2026-7 | Whether voluntary off-site travel for a meal is compensable |
| FLSA 2025-05 | Overtime where one person works for a restaurant and a members-only club under common ownership. Note the space — this pack is internally inconsistent about the separator, and the anchor is whatever the letter itself prints |

Opinion letters answer the facts presented. They bind the Division only as to the requester, and an employer relying on one whose facts differ has relied on nothing. A claim grounded here must cite the letter **and** the section it applies.

### `FORM-WH347` — Form WH-347, certified payroll

| | |
|---|---|
| `doc_type` | `form` |
| Source | https://www.dol.gov/agencies/whd/government-contracts/construction/forms |
| PDF | `https://www.dol.gov/sites/dolgov/files/WHD/legacy/files/wh347.pdf` |
| Edition | January 2025 |
| Excerpted | Both pages: the payroll grid and the statement of compliance on the reverse |
| Pages | 2 |
| Anchor | Column heading or numbered paragraph of the statement of compliance. |
| Backs | R4 |

The artifact the packets are built on. It is a Davis-Bacon certified payroll rather than an FLSA form — there is no FLSA payroll form — but it is the one federal payroll document an employer signs under penalty of perjury, and its grid carries exactly the fields the determinations need: hours worked each day, straight time and overtime hours, rate of pay, gross earned, and **deductions**.

## Recorded cross-references

Multi-hop retrieval is only real if a claim genuinely lives across two documents. Each of these has been confirmed present at both ends.

| # | From | To | The hop |
|---|---|---|---|
| 1 | `WHD-OPS` FLSA2026-2 | `CFR-778` § 778.211 | The letter applies § 7(e)(3) to one employer's bonus; only the regulation states the two-part discretion test and that labels do not decide it. |
| 2 | `WHD-OPS` FLSA2025-04 | `CFR-553` § 553.230 | Firefighter emergency pay only makes sense against the § 7(k) work period, whose hours table lives solely in Part 553. |
| 3 | `FR-2019` salary level | `CFR-541` § 541.602(a)(3) | The preamble explains the 10 percent nondiscretionary-bonus allowance toward the salary level; the regulation states it without the reasoning. |
| 4 | `WHD-OPS` FLSA2026-1 | `CFR-541` § 541.301 | The letter turns on the learned professional duties test, which only Part 541 defines. |
| 5 | `WHD-OPS` FLSA2026-7 | `CFR-785` | Whether meal-related travel is compensable is decided by Part 785's hours-worked rules, which the letter applies but does not restate. |
| 6 | `FORM-WH347` deductions column | `CFR-541` § 541.602 | The certified payroll records deductions as a bookkeeping fact; only the salary basis rule says which deductions defeat an exemption. |

Cross-references 1 and 3 are the chain the golden set must exercise. Number 3 is the one where a careless reader gets the direction of a bonus's treatment backwards.

## Retrieval distractors

Queries whose naive keyword match lands on the wrong section. At least one golden case must be built on each of the first three.

| Term | Why it misleads | Where it appears |
|---|---|---|
| `discretionary` | The single most consequential word in the corpus, and it appears far more often in its **negation**. A payment is excludable only if discretionary; it counts toward the salary level only if **non**discretionary. Substring matching cannot tell the two apart, and the preamble dominates the count | 75 total — `FR-2019` 46, `WHD-OPS` 17, `CFR-778` 8, `CFR-541` 4 |
| `salary basis` | One of three separate requirements that all use the word salary — the **basis** test at § 541.602, the **level** test at § 541.600, and the **fee basis** alternative. Failing any one defeats the exemption, and they fail for different reasons | 42 total — `CFR-541` 22, `WHD-OPS` 11, `FR-2019` 9 |
| `regular rate` | The most common phrase in the corpus. It spans what goes into the rate, what is excluded from it, how it is computed under the fluctuating workweek, and how overtime premiums derive from it | 126 total — `CFR-778` 58, `WHD-OPS` 57, `FR-2019` 9, `CFR-553` 2 |
| `work period` | The § 7(k) term of art, meaning a 7-to-28-day cycle for fire and police only. It is **not** the workweek, and matching it outside Part 553 is almost always a mistake | 14 total — `CFR-553` 12, `WHD-OPS` 2 |

**The first is the sharpest.** "discretionary" and "nondiscretionary" differ by a prefix and point in opposite directions on both tests in this project: a discretionary bonus is excluded from the regular rate and does not count toward the salary level; a nondiscretionary bonus is included in the rate and does count, up to 10 percent. A retriever that treats the two as the same term will produce a confident, fluent, exactly-inverted answer.

Counts are reported by `fetch_corpus.py` on every full rebuild. Transcribe them here when an upstream source shifts.

## Declared out-of-corpus topics

Refusal test cases draw from this list. Every topic here has been confirmed to have **zero occurrences** across all seven documents, so a grounded answer is impossible and a refusal is the only correct outcome. `fetch_corpus.py` re-checks each one on every full rebuild and fails the build if any of them turns up — reading the search terms from `sources.json`'s `verification.out_of_corpus`, not from this file. The list below is a readable transcription of that array, and the two must be kept in step: a topic that appears here and not there is never checked, and the build will pass while the claim above is false.

- Workers' compensation
- Unemployment insurance
- Non-compete agreements
- Occupational safety
- Hazardous waste
- Child labor
- Drug testing
- Equal pay
- Age discrimination
- Non-wage: GDPR and data protection
- Non-wage: Sarbanes-Oxley and financial audit
- Non-wage: HIPAA

> **Family and medical leave and sexual harassment were drafted onto this list and removed when the build caught them.** Both appear in `CFR-541` — § 541.602 permits salary deductions for full-day absences under the FMLA, and for penalties imposed for infractions of workplace conduct rules, which is where harassment enters. Neither is a valid refusal topic. **Minimum wage** is likewise present, 31 times, and is not a refusal topic either. All three are the kind of employment-law subject an analyst would plausibly ask about while working a pay question, which is precisely why they had to be measured rather than assumed.

> **A further category must be refused for a different reason.** Many states set their own overtime thresholds, daily overtime rules and exemption tests, several of which are stricter than the FLSA. **No state law is carried here.** A question about what a particular state requires has no grounding and must be refused with the gap named.

## Near-miss topics

Covered by the corpus but easy to over-refuse. At least one golden case must confirm these are answered, not refused. `fetch_corpus.py` fails the build if one of them goes missing, because a near-miss case built on an absent topic can never fail.

- Meal periods — 36 occurrences; `WHD-OPS` 29, `CFR-785` 6, `CFR-778` 1
- Learned and highly compensated employees — 16 occurrences of "highly compensated"; `FR-2019` 10, `CFR-541` 6
- Outside sales — 9 occurrences; `FR-2019` 8, `CFR-541` 1
- Computer employees — 7 occurrences; `FR-2019` 6, `CFR-541` 1

The last two are thin on purpose. Both exemptions exist, both are named in the regulation, and neither is elaborated here — a system that refuses them entirely is over-refusing, and a system that answers them in detail is inventing.

## Drift note

The operative numbers in this corpus are stable but were recently contested, and that is the thing to watch.

§ 541.600's **$684 per week** and § 541.601's **$107,432** are the 2019 figures. A 2024 rule raised them in stages and was vacated nationwide; the eCFR text carried here reflects the reversion. If a future rebuild shows different figures, the ground has moved again and every R1 boundary test needs rechecking before the golden set is trusted — this is the one project in the bank where the headline threshold has changed twice in three years.

The opinion letters are dated and fact-specific by nature; several here are from 2026 and the Division withdraws and reissues letters without amending any regulation. And no state law is carried, though many states set stricter rules.
