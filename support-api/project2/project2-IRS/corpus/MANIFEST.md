# Payline corpus manifest

Seven documents, 79 pages, 42,234 words. Retrieved 14 August 2026. eCFR issue date 4 August 2026.

Every document is federal public-domain material. This file records where each came from, what a citation to it must resolve to, and the three things the evaluation suite is built from: the cross-references, the retrieval distractors, and the declared out-of-corpus and near-miss topic lists.

## Documents

### `CFR-EMPLOYEE` — 26 CFR Part 31, who is an employee

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-26.xml?part=31` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 31.3121(d)-1, 31.3121(d)-2, 31.3306(i)-1, 31.3401(c)-1 |
| Pages | 7 |
| Anchor | Section number and paragraph. The eCFR structural API has no pagination. |
| Backs | R1 |

The common-law test, stated three times for three different taxes. § 31.3121(d)-1 defines *employee* for FICA, § 31.3306(i)-1 for FUTA, § 31.3401(c)-1 for income tax withholding — and the three definitions are not identical in wording even though they are applied alike.

The operative language is at § 31.3121(d)-1(c)(2): the relationship exists "when the person for whom services are performed has the right to control and direct the individual who performs the services, not only as to the result to be accomplished by the work but also as to the details and means by which that result is accomplished."

Two details in that subsection decide most cases. The test is the **right** to control, not its exercise — "it is not necessary that the employer actually direct or control the manner in which the services are performed; it is sufficient if he has the right to do so." And § 31.3121(d)-1(d)(3) provides that where the relationship exists, "the designation or description of the relationship by the parties as anything other than that of employer and employee is immaterial." A contractor agreement decides nothing. The same sentence appears at § 31.3306(i)-1(d) and § 31.3401(c)-1(e), which is why it turns up three times in a seven-page document.

### `CFR-DEPOSIT` — 26 CFR Part 31, deposit rules

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31 |
| Excerpted | §§ 31.6071(a)-1, 31.6302-1 |
| Pages | 10 |
| Anchor | Section number and paragraph. |
| Backs | R4 |

The deposit obligation. § 31.6302-1 sets the whole scheme out in its own introduction: an employer is either a monthly or a semi-weekly depositor on an annual determination keyed to the lookback period, paragraph (c)(3) overrides both where $100,000 or more of employment taxes accumulate, and paragraph (f) supplies safe harbors for an employer who inadvertently underdeposits.

That last one matters for a reason unrelated to deposits — see the distractor table below.

### `RP-2025-10` — Rev. Proc. 2025-10, implementation of section 530

| | |
|---|---|
| `doc_type` | `guidance` |
| Source | https://www.irs.gov/pub/irs-drop/rp-25-10.pdf |
| Published | 2025 |
| Excerpted | Sections 1 through 11, the whole revenue procedure less the drafting information |
| Pages | 23 |
| Anchor | Revenue procedure section and subsection, cited as 5.02 or 6.03 — but **assembled, not printed**. The document carries a `SECTION 5.` heading and then bare `.02` / `.04` markers; the joined form appears nowhere in the text. |
| Backs | R2 |

**The controlling document of this corpus, and where the trap lives.** Section 530 of the Revenue Act of 1978 is a statute that was never codified into the Internal Revenue Code, and § 530(b) prohibits Treasury from publishing regulations or revenue rulings on the employment status of any individual. This revenue procedure is therefore the closest thing to an authoritative rulebook that exists, and it supersedes Rev. Proc. 85-18.

Relief requires all three of: **reporting consistency** (§ 4), **substantive consistency** (§ 5), and **reasonable basis** (§ 6).

**§ 5 is the trap, and it has three layers.**

- **The general rule.** Relief is available on the three requirements above.
- **The carve-back, § 5.02.** Substantive consistency requires that the taxpayer or a predecessor "not have treated an individual, **or any individual holding a substantially similar position**, as an employee for any period beginning after December 31, 1977." One similar worker on the payroll destroys relief for everyone.
- **The carve-back to the carve-back, § 5.04.** "Treatment of an individual, or an individual holding a substantially similar position, as an employee in a period **subsequent to the period under audit** will not cause a taxpayer to fail the substantive consistency requirement for the period under audit or prior periods under audit." A firm that converted its contractors to employees *after* the years being examined keeps its relief for those years.

**"Substantially similar position" is itself a two-prong test.** Section 5.02 cites § 530(e)(6) and states that such a position exists "if the job functions, duties, and responsibilities are substantially similar **and** the control and supervision of those duties and responsibilities are substantially similar." Comparing job titles, or comparing duties alone, answers half the question. That sentence appears **once** in the corpus.

**Two further structural facts that a naive implementation flattens:**

- **§ 4.03 — reporting consistency is satisfied period by period.** "A taxpayer that filed information returns for one period but that did not file information returns for a prior or subsequent period may satisfy the reporting consistency requirement only for the period for which it filed information returns." Relief is therefore per worker *and* per period, never a single verdict for a firm.
- **Footnote 14 — the cutoff is the date of first IRS contact.** "In no event will a return filed **after the date on which the IRS first contacts the taxpayer** concerning an examination of the period to which the return relates be considered as filed on a basis consistent with good faith treatment." A 1099 filed to paper over the gap once the examination opens is worth nothing. This is in a footnote, which makes it the hardest legitimate retrieval target in the corpus.

### `RR-2025-3` — Rev. Rul. 2025-3, section 3509 and reclassification

| | |
|---|---|
| `doc_type` | `guidance` |
| Source | https://www.irs.gov/pub/irs-drop/rr-25-03.pdf |
| Published | 2025 |
| Excerpted | Issues, five situations, law and analysis, and the holdings |
| Pages | 13 |
| Anchor | Situation number and holding number. |
| Backs | R3 |

What the firm owes once relief is unavailable, worked through **five situations with matching holdings** — the document in this corpus that settles edge cases against the general reading.

It also fixes the **order of operations**, which is what makes the topology defensible. Holding 1: section 530 applies where the taxpayer did not treat the individuals as employees and the IRS is reclassifying them; **"If section 530 does not apply, § 3509 of the Code may be applicable."** The reduced rates are reached only after relief fails. The ruling also states when a § 7436 Notice issues, which is the taxpayer's route to Tax Court review.

### `PUB-15A` — Publication 15-A, Employer's Supplemental Tax Guide

| | |
|---|---|
| `doc_type` | `publication` |
| Source | https://www.irs.gov/forms-pubs/about-publication-15-a |
| PDF | `https://www.irs.gov/pub/irs-pdf/p15a.pdf` |
| Excerpted | Printed pp. 3–10, who are employees through statutory nonemployees |
| Pages | 8 |
| Anchor | Publication section heading and page. |
| Backs | R1 |

The common-law test as IRS explains it to employers, organized into the **three categories of evidence** — behavioral control, financial control, and the type of relationship. This is the vocabulary a firm will actually use, and it is not the vocabulary of the regulation, which speaks only of the right to control.

It also carries two closed lists that decide cases before the common-law test is reached.

**Statutory employees** — four categories, and membership alone is not enough. A worker who "would be an independent contractor under the common-law rules" is nevertheless treated as an employee for certain employment tax purposes if they fall within **any one of four categories** — a commission or agent driver distributing specified goods, a full-time life insurance sales agent writing primarily for one company, an individual working at home on materials the firm supplies to the firm's specifications, or a full-time travelling or city salesperson turning in orders for resale merchandise — **and** meet **all three** further conditions on personal performance, no substantial investment in facilities, and a continuing relationship. A rule that tests category membership and stops has evaluated a third of the test.

**Statutory nonemployees** — three categories: direct sellers, licensed real estate agents and certain companion sitters. For the first two, self-employed treatment applies only where substantially all payment is tied to output rather than hours **and** a written contract provides they will not be treated as employees.

A worker on either list is classified by the list, not by the facts of control.

### `PUB-15` — Publication 15, Circular E

| | |
|---|---|
| `doc_type` | `publication` |
| Source | https://www.irs.gov/forms-pubs/about-publication-15 |
| PDF | `https://www.irs.gov/pub/irs-pdf/p15.pdf` |
| Excerpted | Printed pp. 31–38, when to deposit through deposit penalties |
| Pages | 8 |
| Anchor | Publication section heading and page. |
| Backs | R4 |

**The table-heavy document of this corpus.** It carries the deposit schedules, the lookback period, the $100,000 next-day rule with a worked example, the accuracy-of-deposits rule, and the penalty tier table:

| Penalty | Charged for |
|---|---|
| 2% | Deposits made 1 to 5 days late |
| 5% | Deposits made 6 to 15 days late |
| 10% | Deposits made 16 or more days late, but before 10 days from the date of the first IRS notice |
| 15% | Amounts still unpaid more than 10 days after the first notice, or the day notice and demand for immediate payment is received, whichever is earlier |

The tier boundaries are what a rule engine must encode exactly, and the last row has two triggers joined by "whichever is earlier". Note also the closing sentence: "Late deposit penalty amounts are determined using **calendar** days, starting from the due date of the liability."

A separate **"averaged" FTD penalty of 2% to 10%** applies where the depositor misreported its liability on Form 941 line 16 or Schedule B. It is a different penalty with a different trigger and it is easy to conflate with the tier table.

### `FORM-SS8` — Form SS-8 and its instructions

| | |
|---|---|
| `doc_type` | `form` |
| Source | https://www.irs.gov/forms-pubs/about-form-ss-8 |
| Excerpted | The five-page form and its five-page instructions, assembled from two upstream PDFs |
| Pages | 10 |
| Anchor | Form part and line number, or instruction page. |
| Backs | R1 |

Determination of Worker Status for Purposes of Federal Employment Taxes and Income Tax Withholding — the form a firm or a worker files to ask the IRS to decide the question, and the handwritable artifact of this project. Its parts track the three categories of evidence directly: general information, behavioral control, financial control, and the relationship of the worker and firm.

The instructions state what the determination process does and does not do, which is worth reading before building packets: the IRS determines status, not liability, and a determination is not a substitute for an examination.

## Recorded cross-references

Multi-hop retrieval is only real if a claim genuinely lives across two documents. Each of these has been confirmed present at both ends.

| # | From | To | The hop |
|---|---|---|---|
| 1 | `PUB-15A` three categories of evidence | `CFR-EMPLOYEE` § 31.3121(d)-1(c)(2) | The publication organizes the enquiry into behavioral control, financial control and type of relationship; only the regulation supplies the right-to-control test those categories are evidence of. |
| 2 | `RP-2025-10` § 5.02 | `RP-2025-10` § 5.04 | Both halves of the trap are in one document but different sections, and a retrieval that stops at § 5.02 gets the wrong answer. The nearest thing to a single-document multi-hop in the bank. |
| 3 | `RR-2025-3` Holding 1 | `RP-2025-10` §§ 4–6 | The ruling fixes the order — § 3509 is reached only if section 530 does not apply — and the revenue procedure supplies the three requirements that decide whether it applies. |
| 4 | `RP-2025-10` § 4.02 | `FORM-SS8` and 1099-NEC references | Reporting consistency turns on which information returns were filed; `1099-NEC` appears in four of the seven documents. |
| 5 | `PUB-15` deposit schedules | `CFR-DEPOSIT` § 31.6302-1(b), (c) | The publication states the schedules operationally with worked examples; the regulation states the annual determination and the $100,000 override that generate them. |
| 6 | `PUB-15` accuracy-of-deposits rule | `CFR-DEPOSIT` § 31.6302-1(f) | The publication's "greater of $100 or 2%" tolerance is the regulation's deposit safe harbor. Same rule, two vocabularies. |

Cross-references 2 and 3 are the chain the golden set must exercise.

## Retrieval distractors

Queries whose naive keyword match lands on the wrong section, or on the wrong body of law entirely. At least one golden case must be built on each of the first three.

| Term | Why it misleads | Where it appears |
|---|---|---|
| `safe harbor` | **The term means two entirely unrelated things in this corpus**, backing two different rules. See below — this is the sharpest distractor here | 18 total — `RP-2025-10` 13, `CFR-DEPOSIT` 5 |
| `employee` | 423 occurrences across all seven documents, and it is the word in the title of the question. It discriminates nothing | 423 total — `PUB-15A` 117, `RP-2025-10` 107, `CFR-EMPLOYEE` 84, `RR-2025-3` 69, `PUB-15` 28, `FORM-SS8` 10, `CFR-DEPOSIT` 8 |
| `substantially similar` | The trap's own phrase, and 17 of its 20 occurrences are in one document. A query that reaches `PUB-15A`'s single mention instead gets a one-line summary of a three-layer rule | 20 total — `RP-2025-10` 17, `RR-2025-3` 2, `PUB-15A` 1 |
| `reasonable basis` | One of three section 530 requirements, and the only one most queries name. It is also the requirement with the most text, so it dominates retrieval over the requirement that actually decides the packets | 32 total — `RP-2025-10` 24, `RR-2025-3` 5, `PUB-15A` 2, `FORM-SS8` 1 |

**The `safe harbor` collision is the structural distractor, and it is a genuine ambiguity rather than a spelling accident.** In this corpus the term denotes:

1. **The section 530 reasonable-basis safe harbors** — judicial precedent, prior audit, and industry practice — at `RP-2025-10` § 6. These decide whether a firm owes employment tax at all. They back **R2**.
2. **The deposit-shortfall safe harbor** at `CFR-DEPOSIT` § 31.6302-1(f), which `PUB-15` calls the accuracy-of-deposits rule: no penalty where the shortfall does not exceed the greater of $100 or 2% and is made up on time. This decides a penalty computation. It backs **R4**.

An unfiltered query for "safe harbor" returns both, and they are not variations on one idea — they are different rules, from different bodies of law, answering different questions, for different workers. Filtering on `doc_type` does not separate them either, since one is guidance and one is regulation but the publication restates the regulation. This is what `section_path` filtering is for.

**A vocabulary absence worth knowing about.** Practitioners and the Internal Revenue Manual call the section 530 reasonable-basis safe harbors the "**safe havens**". That phrase appears **zero times** in this corpus — the published guidance says "safe harbors" throughout. A query in the practitioner's idiom returns nothing.

Counts are reported by `fetch_corpus.py` on every full rebuild. Transcribe them here when an upstream source shifts.

## Declared out-of-corpus topics

Refusal test cases draw from this list. Every topic here has been confirmed to have **zero occurrences** across all seven documents, so a grounded answer is impossible and a refusal is the only correct outcome. `fetch_corpus.py` re-checks each one on every full rebuild and fails the build if any of them turns up — reading the search terms from `sources.json`'s `verification.out_of_corpus`, not from this file. The list below is a readable transcription of that array, and the two must be kept in step: a topic that appears here and not there is never checked, and the build will pass while the claim above is false.

- Hazardous waste
- Occupational safety
- Medical devices
- Breach notification
- Hours of service
- Suspicious activity reports
- Money laundering
- GDPR and data protection
- Sarbanes-Oxley and financial audit
- EMTALA
- The two-midnight rule
- Employment eligibility verification
- The Fair Labor Standards Act
- The economic-reality test

The middle five are drawn from sibling projects in this bank, which makes them useful in a second way: a team that has seen another team's corpus should still get a refusal.

> **The last two are the ones to build a case on, and they matter more than they look.** A worker can be an employee for wage-and-hour purposes and an independent contractor for tax purposes, because the FLSA applies an **economic-reality** test and this corpus applies the **common-law right-to-control** test. They are different tests under different statutes administered by different agencies, and they reach different answers on the same facts routinely. Neither `Fair Labor Standards` nor `economic reality` appears anywhere here.
>
> Word the case with care all the same. `minimum wage` and `overtime` each appear **once**, both in `RP-2025-10`, in passing. Ask about the economic-reality test by name, not about wages generally. The sibling Straighttime project carries that corpus.

## Near-miss topics

Covered by the corpus but easy to over-refuse. At least one golden case must confirm these are answered, not refused. `fetch_corpus.py` fails the build if one of them goes missing, because a near-miss case built on an absent topic can never fail.

- Statutory employee — the four-category list in `PUB-15A`, which decides status without reaching the common-law test
- Statutory nonemployee — qualified real estate agents, direct sellers and certain companion sitters, in `PUB-15A`
- Common-law — 32 occurrences, the test itself
- Lookback period — 49 occurrences; `PUB-15` 28, `CFR-DEPOSIT` 21. The input to the deposit schedule determination

## Drift note

Section 530 has been substantially unchanged since the Small Business Job Protection Act of 1996 added the burden-shifting rule and the industry-practice clarifications. The common-law regulations are older still.

Three cautions.

**Rev. Proc. 2025-10 and Rev. Rul. 2025-3 are both recent, and published guidance is superseded rather than amended.** Rev. Proc. 2025-10 itself superseded Rev. Proc. 85-18 after forty years. When it is superseded in turn, the URL will not change and the document at it will. Check § 9, "Effect on Other Documents", after any rebuild that produces a diff.

**IRS publications are revised annually and the page ranges will move.** `PUB-15` and `PUB-15A` are keyed to a tax year — the copies here are the 2026 editions — and IRS reflows them every December. A rebuild in January will almost certainly need new page ranges. Read the first page of each excerpt before trusting it.

**Section 530(b) bars Treasury from issuing regulations or revenue rulings on the employment status of any individual**, which is why this corpus has no Federal Register rulemaking preamble where its sibling projects do. There is no notice-and-comment record to cite, because the statute forbids creating one. Rev. Proc. 2025-10 § 2.06 addresses this directly, explaining that the revenue procedure is permissible because it clarifies the application of section 530 rather than classifying any worker. Any determination this system produces inherits that limit: **the corpus can ground how the test is applied and never what the answer is for a category of worker.**
