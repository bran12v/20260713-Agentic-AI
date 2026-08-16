# Ledgerline corpus manifest

Six documents, 88 pages, 46,653 words. Retrieved 13 August 2026. eCFR issue date 4 August 2026.

Every document is federal public-domain material. This file records where each came from, what a citation to it must resolve to, and the three things the evaluation suite is built from: the cross-references, the retrieval distractors, and the declared out-of-corpus and near-miss topic lists.

## Documents

### `CFR-1020` — 31 CFR Part 1020, Rules for Banks

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-31.xml?part=1020` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 1020.100, 1020.210, 1020.220, 1020.310, 1020.315, 1020.320, each in full |
| Pages | 13 |
| Anchor | Section number and paragraph. The eCFR structural API has no pagination. |
| Backs | R1–R4 |

The controlling text for a bank. § 1020.210 sets the anti-money-laundering programme requirement, § 1020.220 the customer identification programme, § 1020.320 the suspicious activity report — its single $5,000 threshold at (a)(2), the three suspicion grounds at (a)(2)(i)–(iii), and the filing clocks at (b)(3). The two-basis framing a compliance officer will recite from memory — $5,000 with a suspect, $25,000 without — is **not** in this section; it lives in `FILING-SPEC`, and keeping the two apart is R1's job.

**§ 1020.315 is the trap.** It grants a currency-transaction-reporting exemption to an "exempt person", and paragraph (b)(6) extends that to a **non-listed business** — any commercial enterprise meeting quantitative criteria about accounts, frequency and domestic operation. But (b)(6) opens by excepting "an enterprise specified in paragraph (e)(8)", and **(e)(8) is a closed list of activities** that may never be treated as a non-listed business however well the numbers fit: financial institutions and their agents, sale or purchase of motor vehicles of any kind, vessels, aircraft, farm equipment or mobile homes, the practice of law, accountancy or medicine, auctioning, chartering or operating ships, buses or aircraft, gaming, investment advice, and more.

Paragraph (f) then adds a second limitation: a transaction carried out by an exempt person **as agent for a beneficial owner** is not exempt at all.

### `CFR-1010` — 31 CFR Part 1010, General Provisions

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010 |
| Excerpted | §§ 1010.306, 1010.311, 1010.313, 1010.314, 1010.315, 1010.330, 1010.410 |
| Pages | 14 |
| Anchor | Section number and paragraph. |
| Backs | R2, R4 |

The reporting obligation itself. § 1010.311 requires a report of each transaction in currency of **more than $10,000**; § 1010.313 sets the aggregation rules that decide when several transactions are one; § 1010.314 addresses structured transactions; § 1010.330 covers reports of currency received in a trade or business; § 1010.410 sets the records to be made and retained, including the funds-transfer rules.

### `FR-2016` — 81 FR 29398, Customer Due Diligence Requirements

| | |
|---|---|
| `doc_type` | `preamble` |
| Source | https://www.federalregister.gov/documents/2016/05/11/2016-10567/customer-due-diligence-requirements-for-financial-institutions |
| PDF | `https://www.govinfo.gov/content/pkg/FR-2016-05-11/pdf/2016-10567.pdf` |
| Published | 11 May 2016 |
| Excerpted | Printed pp. 29398–29399, 29404–29411, 29419–29421 |
| Pages | 13 |
| Anchor | Federal Register page number. The excerpt is **three non-contiguous runs**, so no single offset works: shipped pp. 1–2 are printed 29398–29399, shipped pp. 3–10 are printed 29404–29411, and shipped pp. 11–13 are printed 29419–29421. |
| Backs | — (grounds the conditional worker) |

The rulemaking that added beneficial ownership as a fifth pillar. The section-by-section analysis explains the **25 percent** ownership threshold and the control prong, why FinCEN declined to require verification of beneficial owners to the same standard as customers, and how the new obligation relates to suspicious activity reporting. "beneficial owner" appears 160 times in these thirteen pages against three times in the regulation.

Excluded: the other 48 pages, which are comment summary and regulatory impact analysis.

### `FIN-RULINGS` — FinCEN administrative rulings

| | |
|---|---|
| `doc_type` | `interpretation` |
| Source | https://www.fincen.gov/resources/statutes-regulations/administrative-rulings |
| Excerpted | Five administrative rulings and one guidance note, assembled from six upstream PDFs |
| Pages | 15 |
| Anchor | Ruling number, as printed in the section heading. |
| Backs | R2, R3 |

FinCEN answering one institution's specific question in writing. FinCEN states that published administrative rulings have precedential value, which makes these the closest available analogue to an interpretation letter — and the substitute for the FFIEC manual, which could not be carried.

| Ruling | What it resolves |
|---|---|
| FIN-2020-R001 | Currency transaction reporting where a sole proprietorship or legal entity operates under a different name |
| FIN-2018-R002 | Whether beneficial ownership must be recollected on a certificate-of-deposit rollover or loan renewal |
| Ruling 2001-1 | A bank's question on the treatment of a customer's currency transactions |
| Ruling 2003-8 | Whether a merchant payment processor is a money transmitter |
| Ruling 2004-4 | Whether a debt management company is a money services business |
| Backfiling guidance | Instructions for backfiling and amending currency transaction reports |

Rulings answer the facts presented and are dated; several here are more than twenty years old. A claim grounded in one must cite the ruling **and** the section it construes.

**The last row is not a ruling.** The backfiling document is FinCEN guidance — it carries no ruling number and none of the precedential value the paragraph above claims for the other five. A claim grounded in it cites the guidance by title and the section it construes, and must not be presented as resting on an administrative ruling.

**None of these six resolves to a section number in the rest of the corpus.** The rulings cite the pre-2011 numbering — 31 CFR Part 103, sixteen times across the document — which was renumbered into Parts 1010 and 1020 and no longer matches anything the index holds. § 103.22(b) is today's § 1010.311; § 103.11 is § 1010.100. Any citation-resolution check that walks a ruling's own section reference will fail unless you map the old numbering forward, and the multi-hop chains through this document all depend on that mapping.

### `FORM-DOEP` — FinCEN Form 110, Designation of Exempt Person

| | |
|---|---|
| `doc_type` | `form` |
| Source | https://www.fincen.gov/resources/filing-information |
| Excerpted | The two-page form with its general instructions, and the seven-page electronic filing instructions, assembled from two upstream PDFs |
| Pages | 9 |
| Anchor | Form item number, or instruction page. |
| Backs | R3 |

The artifact the trap lives on, and the artifact the packets are built from. A bank designates a customer as exempt by filing this form, and in doing so asserts which category of exempt person the customer falls into. **The form asks the bank to state the exemption category; it does not ask, and cannot check, whether the customer's line of business appears on the § 1020.315(e)(8) ineligible list.** A correctly completed form and an unlawful exemption look identical.

### `FILING-SPEC` — FinCEN SAR and CTR filing instructions

| | |
|---|---|
| `doc_type` | `instructions` |
| Source | https://www.fincen.gov/resources/filing-information |
| Excerpted | Printed pp. 3–14 of each of the SAR and CTR electronic filing instructions, assembled from two upstream PDFs |
| Pages | 24 |
| Anchor | Report type and item number. |
| Backs | R1, R2, R4 |

What each report actually asks for, item by item. The SAR instructions carry the filing deadlines and the narrative requirements; the CTR instructions carry the transaction, person-conducting and person-on-whose-behalf structure that the aggregation rules turn on.

Neither report has a paper form — both are filed through the BSA E-Filing System — which is why the corpus carries the instructions rather than a form for these two.

## Recorded cross-references

Multi-hop retrieval is only real if a claim genuinely lives across two documents. Each of these has been confirmed present at both ends.

| # | From | To | The hop |
|---|---|---|---|
| 1 | `FORM-DOEP` | `CFR-1020` § 1020.315(e)(8) | The form takes an exemption category as an assertion; only the regulation lists the businesses that can never qualify. |
| 2 | `FIN-RULINGS` FIN-2020-R001 | `CFR-1020` sole proprietorship rules | The ruling resolves how a sole proprietorship trading under another name is reported; the regulation supplies the underlying treatment. |
| 3 | `FR-2016` section-by-section | `CFR-1020` § 1020.210(b)(5) | The regulation makes beneficial ownership the fifth programme pillar and then defers — customer information "shall include information regarding the beneficial owners of legal entity customers (as defined in § 1010.230 of this chapter)". **§ 1010.230 is not carried by this corpus**, so the duty is in the regulation and the 25 percent threshold and control prong exist only in the preamble. A worker that stops at the regulation has the obligation and neither number. |
| 4 | `FILING-SPEC` SAR items | `CFR-1020` § 1020.320 | The instructions say what to enter and by when; only the regulation says what makes a transaction reportable in the first place. |
| 5 | `FILING-SPEC` CTR items | `CFR-1010` § 1010.313 | The CTR's person-conducting and person-on-whose-behalf structure only makes sense against the aggregation rules. |
| 6 | `FIN-RULINGS` backfiling | `CFR-1010` § 1010.311 | Backfiling guidance presupposes the reporting obligation the regulation creates. |

Cross-references 1 and 3 are the chain the golden set must exercise. Number 1 is where a confidently wrong answer comes from reading the artifact instead of the rule. Number 3 is the opposite failure: the regulation is reachable, sounds complete, and does not contain the threshold the question is asking for. Neither end is optional.

> **Do not build a hop onto § 1010.230.** `CFR-1020` points at it twice and `FR-2016` twenty-four times, but the section is not in this corpus. A citation resolving to it is a citation failure, and a question that turns on the definition of a legal entity customer is a refusal.

## Retrieval distractors

Queries whose naive keyword match lands on the wrong section. At least one golden case must be built on each of the first three.

| Term | Why it misleads | Where it appears |
|---|---|---|
| `exempt person` | The term of art, and it is dominated by the **form** rather than the rule — 46 of 74 occurrences are in `FORM-DOEP`. A query about who is exempt lands in the filing instructions, which explain how to assert an exemption and never state who may not claim one | 74 total — `FORM-DOEP` 46, `CFR-1020` 27, `FIN-RULINGS` 1 |
| `$10,000` | The **CTR** threshold. The SAR thresholds are $5,000 and $25,000 and appear far less often, so a threshold question matched on the common figure answers about the wrong report | 36 total — `CFR-1010` 24, `FILING-SPEC` 4, `FORM-DOEP` 3, `FIN-RULINGS` 2, `CFR-1020` 2, `FR-2016` 1 |
| `suspicious` | Spans the SAR obligation, the filing instructions' item labels, and the preamble's discussion of how customer due diligence feeds suspicious activity monitoring | 76 total — `FILING-SPEC` 40, `FR-2016` 20, `CFR-1020` 14, `FORM-DOEP` 2 |
| `15 days` | **Two different reports share one clock phrase inside one document.** § 1010.306(a)(1) sets the CTR deadline at 15 days; § 1010.330 sets a 15-day deadline for the Form 8300 report a non-financial trade or business files on cash over $10,000 received. Different filer, different form, different trigger — and the wrong one outnumbers the right one two to one. Both sit in `CFR-1010`, so **no `doc_type` filter separates them**; only `section_path` does | 6 total, all `CFR-1010` — `§ 1010.330` 4, `§ 1010.306` 2 |
| `30 calendar days` | **The same obligation is spelled three different ways.** The SAR deadline is "30 calendar days"; the exemption designation deadline at § 1020.315(c)(1) is "the close of the 30-calendar day period"; and `FORM-DOEP`'s own instructions say "30 days". A literal query for the first finds the SAR clock and misses the designation clock entirely — which is the trap's own deadline | `30 calendar days` 4 — `CFR-1020` 2, `FILING-SPEC` 2. `30-calendar day period` 1 — `CFR-1020`. `30 days` 2 — `FORM-DOEP` |

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
- Non-BSA: GDPR and data protection
- Non-BSA: Sarbanes-Oxley and financial audit
- Non-BSA: HIPAA

> **Two further categories must be refused for a different reason, and both are in scope for a real analyst — but neither is a clean absence, so word the refusal cases carefully.**
>
> **OFAC sanctions screening** is a separate Treasury programme under a different chapter. No OFAC regulation, no sanctions list and no guidance on the fifty percent rule is carried — but the word **OFAC appears 3 times and "sanctions" 6 times in `FR-2016`**, where the preamble discusses how sanctions screening sits alongside customer due diligence. So the corpus can say that the two programmes are distinct and cannot answer any question about a blocked person or a specific match. A refusal case must be written against the second, not the first.
>
> The **FFIEC BSA/AML Examination Manual** could not be carried at all because `ffiec.gov` blocks automated clients, and nothing in this corpus substitutes for it. Questions of the form "what will an examiner expect" are a clean refusal.

## Near-miss topics

Covered by the corpus but easy to over-refuse. At least one golden case must confirm these are answered, not refused. `fetch_corpus.py` fails the build if one of them goes missing, because a near-miss case built on an absent topic can never fail.

- Money services businesses — `FIN-RULINGS` 2003-8 and 2004-4 both turn on the definition
- Beneficial owners — `FR-2016` at length, and `CFR-1020`
- The safe harbour from liability for filing — 9 occurrences, in `FR-2016` 8 and `CFR-1010` 1. Not in `CFR-1020`
- Casinos — 6 occurrences across `CFR-1010`, `FILING-SPEC` and `FIN-RULINGS`. Note that § 1020.315(e)(8) excludes "gaming of any kind" without using the word

## Drift note

The reporting obligations here are among the most stable in the bank: the $10,000 currency threshold has not moved in decades, and the exemption structure has been in its present form since the 2008 revision.

Three cautions. The **administrative rulings are old** — two date from 2001 and 2003 — and FinCEN withdraws or supersedes rulings without amending any regulation; they are carried because they record FinCEN's reasoning, not because each is current. The **beneficial ownership regime is in motion**: the 2016 rule carried here is the operative CDD requirement, but the separate beneficial ownership reporting regime under the Corporate Transparency Act has been through repeated changes and is **not** in this corpus, so a question about that regime must be refused. And the **filing instructions track the E-Filing System**, which is revised without notice; the page ranges excerpted here are a snapshot.
