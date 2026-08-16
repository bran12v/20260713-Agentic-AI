# Cradle corpus manifest

Six documents, 91 pages, 41,702 words. Retrieved 13 August 2026. eCFR issue date 4 August 2026.

Every document is federal public-domain material. This file records where each came from, what a citation to it must resolve to, and the three things the evaluation suite is built from: the cross-references, the retrieval distractors, and the declared out-of-corpus and near-miss topic lists.

## Documents

### `CFR-261` — 40 CFR Part 261, Identification and Listing of Hazardous Waste

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-40/chapter-I/subchapter-I/part-261 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-40.xml?part=261` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 261.2, 261.3, 261.7, 261.20, 261.21, 261.22, 261.23, 261.24, 261.30, 261.31, each in full |
| Pages | 22 |
| Anchor | Section number, and paragraph designation where the determination turns on one. The eCFR structural API has no pagination. |
| Backs | R1, R2 |

The document the whole exercise turns on. § 261.2 defines solid waste and § 261.3 hazardous waste, including the mixture and derived-from rules. §§ 261.20–261.24 define the four characteristics, with the toxicity table of D-codes at § 261.24. § 261.30 supplies the hazard-code legend and, at (d), names the acute F-codes in prose. § 261.31 is the F list.

**§ 261.7 is the trap.** In 2,590 characters it says that hazardous waste left in an empty container is not regulated; defines empty as all waste removed by common practice plus no more than one inch of residue or 3 percent by weight at 119 gallons or less, 0.3 percent above; and excludes acute hazardous waste from that test by its own terms, requiring triple rinsing instead.

Excluded, and this constrains what the corpus can answer: **§ 261.4** (the exclusions) at 99,000 characters and **§ 261.33** (the P and U commercial chemical product lists) at 118,000 are both too large to carry. A question that turns on whether a particular P-code or U-code is listed cannot be grounded here and must be refused. The acute-waste chain runs through § 261.30(d) and § 261.31 instead.

### `CFR-262` — 40 CFR Part 262, Standards Applicable to Generators of Hazardous Waste

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-40/chapter-I/subchapter-I/part-262 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-40.xml?part=262` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 262.11, 262.13, 262.16, 262.17, 262.20, each in full |
| Pages | 20 |
| Anchor | Section number. |
| Backs | R3, R4 |

The second determination's ground. § 262.11 states the duty to make a waste determination and how. § 262.13 assigns the generator category, monthly, through **Table 1** — the table that carries the 1 kg acute threshold and the 100 kg and 1,000 kg non-acute thresholds. § 262.16 sets the small quantity generator's 180-day accumulation limit and its 270-day extension for a treatment facility more than 200 miles away; § 262.17 sets the large quantity generator's 90 days. § 262.20 states when a manifest is required.

### `CFR-268` — 40 CFR Part 268, Land Disposal Restrictions

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-40/chapter-I/subchapter-I/part-268 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-40.xml?part=268` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 268.9, 268.48, 268.49, each in full |
| Pages | 9 |
| Anchor | Section number. |
| Backs | — (grounds the conditional worker) |

The conditional third leg's only ground. § 268.9 explains how a waste carrying a characteristic is brought into the land disposal restrictions. § 268.48 is the **Universal Treatment Standards** table — constituent, CAS number, wastewater standard, non-wastewater standard — and is the second table in the corpus that must survive extraction with its rows intact. § 268.49 covers contaminated soil.

Excluded: **§ 268.40**, the treatment standards by waste code, at 239,000 characters larger than this entire corpus. A question asking for the treatment standard for a specific waste code cannot be grounded here.

### `FR-2016` — 81 FR 85732, Hazardous Waste Generator Improvements Rule

| | |
|---|---|
| `doc_type` | `preamble` |
| Source | https://www.federalregister.gov/documents/2016/11/28/2016-27429/hazardous-waste-generator-improvements-rule |
| PDF | `https://www.govinfo.gov/content/pkg/FR-2016-11-28/pdf/2016-27429.pdf` |
| Published | 28 November 2016 |
| Excerpted | Printed pp. 85736–85737, 85742–85743, 85748–85750, 85755–85757 |
| Pages | 10 |
| Anchor | Federal Register page number. The excerpt is **four non-contiguous runs**, so no single offset works: shipped pp. 1–2 are printed 85736–85737, shipped pp. 3–4 are printed 85742–85743, shipped pp. 5–7 are printed 85748–85750, and shipped pp. 8–10 are printed 85755–85757. |
| Backs | R3 |

The rulemaking record for the generator standards as they now stand. Four passages are carried: the reorganisation that moved the generator rules out of Part 261 into Part 262, the treatment of a generator producing **both acute and non-acute waste in the same month**, the waste determination requirement, and the section-by-section discussion of generator category determination.

Excluded: the other 88 pages, which are comment summary and regulatory impact analysis.

### `RO-PACK` — EPA guidance and interpretations on empty containers

| | |
|---|---|
| `doc_type` | `interpretation` |
| Source | https://rcrapublic.epa.gov/rcraonline/ |
| Retrieved | 13 August 2026 |
| Excerpted | The Generator Regulations Compendium Volume 11 (14 pp), RCRA Online 12161 (2 pp), RCRA Online 12307 (2 pp) |
| Pages | 18 |
| Anchor | Compendium page number, or RCRA Online document number for the letters. |
| Backs | R2 |

The interpretive layer for the trap, assembled from three upstream PDFs into one document.

The **compendium** is EPA's own compilation of its guidance on § 261.7 — what counts as common practice, what happens to residue, how the acute-waste requirement differs. **RO 12161** (13 December 1983) addresses triple rinsing directly, and is candid that EPA has never defined the term in the regulations. **RO 12307** (11 September 1984) applies the one-inch and 3-percent tests to containers that held commercial chemical products.

RCRA Online documents are historical agency correspondence. They record how EPA read the rule on the date they were written, and several predate the current text; the compendium is the more current statement. A claim should cite the regulation and use these to explain it, not the reverse.

### `FORM-8700` — EPA Form 8700-22, Uniform Hazardous Waste Manifest

| | |
|---|---|
| `doc_type` | `form` |
| Source | https://www.epa.gov/hwgenerators/uniform-hazardous-waste-manifest-instructions-sample-form-and-continuation-sheet |
| Excerpted | The manifest itself (1 p) and the item-by-item instructions (11 pp), assembled from two upstream PDFs |
| Pages | 12 |
| Anchor | Manifest item number, or instruction page. |
| Backs | R4 |

The form that accompanies every shipment, and the artifact the packets are built on. Items 9b, 10, 11 and 13 — the waste description, containers, total quantity and waste codes — are the fields the determination writes into, and item 14's special handling instructions are where an acute waste has to be flagged.

EPA distributes the real form only through registered printers; the PDF here is EPA's published sample, which is what a training corpus should carry anyway.

## Recorded cross-references

Multi-hop retrieval is only real if a claim genuinely lives across two documents. Each of these has been confirmed present at both ends.

| # | From | To | The hop |
|---|---|---|---|
| 1 | `RO-PACK` compendium | `CFR-261` § 261.7(b)(1) | The guidance discusses "one inch" of residue in plain terms 10 times; the regulation states it once, as "2.5 centimeters (one inch)", and attaches the alternative percentage tests. |
| 2 | `RO-PACK` RO 12161 | `CFR-261` § 261.7(b)(3) | The letter is the only document that says EPA never defined triple rinsing, which is the test the regulation requires for acute waste and nowhere explains. |
| 3 | `FR-2016` generator category | `CFR-262` § 262.13 Table 1 | The preamble explains why the thresholds are where they are; only the table states them. |
| 4 | `CFR-261` § 261.30(d) | `CFR-262` § 262.13 Table 1 | § 261.30(d) names F020–F023, F026 and F027 as subject to the acute limits, and points at the table that sets them. Without this hop an F-code cannot be tested against the 1 kg threshold. |
| 5 | `FORM-8700` instructions | `CFR-262` § 262.20 | The instructions say what to write in each item; the regulation says when a manifest is required at all. |
| 6 | `CFR-268` § 268.9 | `CFR-261` §§ 261.20–261.24 | A characteristic waste enters the land disposal restrictions through its characteristic, which only Part 261 defines. |

Cross-references 1, 2 and 4 are the chain the golden set must exercise. Number 4 is where a wrong answer propagates: mistaking an acute code for a non-acute one moves the applicable threshold by three orders of magnitude.

## Retrieval distractors

Queries whose naive keyword match lands on the wrong section. At least one golden case must be built on each of the first three.

| Term | Why it misleads | Where it appears |
|---|---|---|
| `empty` | The single most overloaded word in the corpus. It carries the regulatory term of art from § 261.7, the ordinary English sense used throughout the guidance, and the manifest instruction to leave an item blank. Guidance outweighs regulation five to one, so an unfiltered query answers from commentary | 67 total — `RO-PACK` 55, `CFR-261` 11, `FORM-8700` 1 |
| `acute hazardous waste` | Governs two different things that a determination must keep apart: the § 261.7 empty test and the § 262.13 quantity threshold. Most occurrences are the second | 85 total — `FR-2016` 55, `CFR-262` 14, `RO-PACK` 13, `CFR-261` 3 |
| `180 days` | The small quantity generator's accumulation limit, which sits beside a 270-day extension and the large quantity generator's 90 days. Matching the phrase does not establish which category the generator is in | 11 total — `CFR-262` 10, `FR-2016` 1 |
| `generator category` | Appears far more often in the preamble explaining the 2016 reorganisation than in the regulation that assigns one | 49 total — `FR-2016` 40, `CFR-262` 8, `CFR-261` 1 |

**A structural distractor, not a lexical one.** Wide tables are rendered as fixed-width text with long cells wrapped inside their column, so a phrase that spans a wrap point does not appear contiguously. In § 262.13 Table 1 the header reads `Quantity of` / `acute` / `hazardous` / `waste` down four lines, and the string "Quantity of acute hazardous waste" occurs nowhere in `text/CFR-262.txt` despite being the column's plain meaning. A chunker that splits on lines, or a retriever relying on exact phrase match, will miss the most important table in the corpus. Chunk tables whole.

Counts are reported by `fetch_corpus.py` on every full rebuild. Transcribe them here when an upstream source shifts.

## Declared out-of-corpus topics

Refusal test cases draw from this list. Every topic here has been confirmed to have **zero occurrences** across all six documents, so a grounded answer is impossible and a refusal is the only correct outcome. `fetch_corpus.py` re-checks each one on every full rebuild and fails the build if any of them turns up — reading the search terms from `sources.json`'s `verification.out_of_corpus`, not from this file. The list below is a readable transcription of that array, and the two must be kept in step: a topic that appears here and not there is never checked, and the build will pass while the claim above is false.

- Minimum wage
- Family and medical leave
- Workers' compensation
- Unemployment insurance
- Collective bargaining
- Prevailing wage
- Sexual harassment
- Non-compete agreements
- Non-environmental: GDPR and data protection
- Non-environmental: Sarbanes-Oxley and financial audit
- Non-environmental: HIPAA

> Two further categories must be refused for a different reason — they are in scope for RCRA but **not carried by this corpus**. A question that turns on whether a specific **P-code or U-code** is listed (§ 261.33) or on the **treatment standard for a specific waste code** (§ 268.40) has no grounding here, and the correct behaviour is a refusal naming the gap. These are the most likely false-confident answers this corpus can produce, because the surrounding sections discuss both at length without listing either.

## Near-miss topics

Covered by the corpus but easy to over-refuse. At least one golden case must confirm these are answered, not refused. `fetch_corpus.py` fails the build if one of them goes missing, because a near-miss case built on an absent topic can never fail.

- Satellite accumulation areas — `CFR-262` 2, `FR-2016` 3
- Drip pads — `CFR-262` 15, `FR-2016` 1. The term sounds like something outside the corpus and is not
- Used oil — `CFR-261` 7, `CFR-262` 2, `FR-2016` 2
- Closure of a waste accumulation unit — `CFR-262` 22, all of them in § 262.17

Universal waste was drafted onto this list and removed: it appears twice in the whole corpus, once in `CFR-262` and once in `RO-PACK`, which is too thin to insist an answer is possible.

## Drift note

The federal baseline in this corpus is stable. The Generator Improvements Rule took effect in 2017 and the sections carried here have not moved since; the eCFR pin reproduces them exactly.

Two cautions apply anyway. **RCRA is a delegated programme**: most states run their own authorised versions, and a state may be stricter than the federal text on any point here, including accumulation times and the empty-container test. Nothing in this corpus reflects any state programme, and the brief's out-of-scope list says so. And the RCRA Online letters are decades old — they are carried because they record EPA's reasoning, not because they are current, and the compendium supersedes them where the two differ.
