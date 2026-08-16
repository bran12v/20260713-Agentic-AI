# Corpus manifest

Six documents, 76 pages, 48,107 words, all federal public-domain material excerpted from `osha.gov`, `ecfr.gov`, `govinfo.gov` and `federalregister.gov`. Retrieved **13 August 2026**; eCFR issue date **4 August 2026**.

`pdf/` holds the excerpted PDFs the ingestion pipeline cracks. `text/` holds a plain-text extraction of each, committed so that a diff shows when an upstream source has moved under you. `python fetch_corpus.py` rebuilds both from `sources.json` on a clean clone.

---

## Documents

### `CFR-1904` — 29 CFR Part 1904, Recording and Reporting Occupational Injuries and Illnesses

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1904 |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-29.xml?part=1904` |
| Excerpted | §§ 1904.4, 1904.5, 1904.6, 1904.7, 1904.29, 1904.39 — each in full |
| Pages | 13 |
| Anchor | Section number. eCFR has no pagination, and section numbers are what citations must resolve to. |
| Backs | R1, R2, R3, R4 |

The controlling text. §1904.4 recording criteria, §1904.5 work-relatedness, §1904.6 new-case test, §1904.7 general recording criteria including the day counts, the 180-day cap and the closed first-aid list at (b)(5)(ii), §1904.29 the forms rule and Form 300 column definitions, §1904.39 the 8-hour and 24-hour reporting clocks with the observation-only exclusion at (b)(10) and the amputation exclusion list at (b)(11).

### `CFR-269` — 29 CFR 1910.269, Electric Power Generation, Transmission, and Distribution

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/subpart-R/section-1910.269 |
| Excerpted | Paragraph (l), *Working on or near exposed energized parts*, in full — including the eight minimum-approach-distance tables it carries (Table R-3 for ac systems, R-8 for dc, R-9 for transient overvoltage) |
| Pages | 7 |
| Anchor | Paragraph designation within § 1910.269. |
| Backs | Hazard controls (no rule) |

The only document that can ground a hazard-control proposal, and the only one carrying column-aligned numeric tables. Paragraph (l) is 1 of 24 top-level paragraphs in a section that runs to several hundred pages whole; everything outside (l) is excluded.

The appendices to § 1910.269 are not reachable through the eCFR structural API at the section or subpart path and are not included. The approach distances the hazard-control worker needs are in Table R-3 inside paragraph (l).

> The ANSI, IEEE, NFPA and ASTM standards that § 1910.269 incorporates by reference are not public domain and are excluded, even though the federal text cites them.

### `CPL-172` — OSHA Instruction CPL 02-00-172, Part 1904 Recordkeeping Policies and Procedures

| | |
|---|---|
| `doc_type` | `directive` |
| Source | https://www.osha.gov/enforcement/directives/cpl-02-00-172 |
| PDF | https://www.osha.gov/sites/default/files/enforcement/directives/CPL-02-00-172.pdf |
| Effective | 13 January 2025 |
| Excerpted | § IX.E *Determining the Recordability of Fatalities, Injuries, or Illnesses* (printed pp. 10–24) · § IX.P *Reporting Severe Injuries and Illnesses to OSHA* (printed pp. 31–33) · Appendix B *Compliance Officer Checklist* |
| Pages | 21 |
| Anchor | Printed page number and section designation. Printed page *n* is PDF page *n + 3*. |
| Backs | R1, R2, R3 |

OSHA's own applied reading of Part 1904 — the procedural layer between the regulation and a determination. This directive supersedes CPL 02-00-135; do not substitute the older one. It contains no FAQ appendix.

Useful anchors inside the excerpt: the complete first-aid list restating §1904.7(b)(5)(ii) sits at **IX.E.10** (PDF pages 20–21 of the source, pages 8–9 of the excerpt); the non-reportable circumstances — motor vehicle on a public highway, commercial transport, beyond 30 days — sit at **IX.P.3**; the note that a hospitalization already reported needs no second report on later death sits at **IX.P.1**.

§ XIII *Inspection Procedures* is not included. It governs how OSHA conducts an inspection, which no rule in this system depends on.

### `FR-2014` — 79 FR 56130, Recording and Reporting Requirements: NAICS Update and Reporting Revisions

| | |
|---|---|
| `doc_type` | `preamble` |
| Source | https://www.federalregister.gov/documents/2014/09/18/2014-21514 |
| PDF | https://www.govinfo.gov/content/pkg/FR-2014-09-18/pdf/2014-21514.pdf |
| Published | 18 September 2014 |
| Excerpted | The section-by-section analysis of the § 1904.39 reporting requirements, printed pp. 56140–56156 |
| Pages | 17 |
| Anchor | Federal Register page number (`79 FR 561nn`). The excerpt is one contiguous run renumbered from 1, so shipped page *n* is printed page *n* + 56139 — shipped pp. 1–17 are printed 56140–56156. |
| Backs | R2 |

The rulemaking record behind the reporting rule as it now stands: why the 8-hour and 24-hour clocks are set where they are, why admission for observation or diagnostic testing alone is not an in-patient hospitalization, and why the amputation definition excludes avulsions, enucleations, deglovings, scalpings, severed ears and broken or chipped teeth. This is the interpretive layer for R2 — the rule with the most edge cases and the one P4 turns on.

### `LOI-PACK` — OSHA Letters of Interpretation, Part 1904

| | |
|---|---|
| `doc_type` | `interpretation` |
| Index | https://www.osha.gov/laws-regs/standardinterpretations/standardnumber/1904 |
| Pages | 11 |
| Anchor | Letter date. Each letter is an individually dated page. |
| Backs | R1, R2, R3, R4 |

Six letters, each resolving an edge case the regulation text alone does not settle.

| Date | Title | What it resolves | Backs |
|---|---|---|---|
| 2021-01-08 | Reporting two related reportable events | A hospitalization already reported, followed by death or amputation, needs **no second report** | R2 |
| 2015-04-15 | General requirements that apply to workers who drive heavy trucks and other commercial motor vehicles | Motor vehicle on a public street, and commercial or public transportation — **not reportable but still recordable** | R1, R2 |
| 2004-01-13 | Determining work-relatedness when the work event or exposure is only one of the discernable causes | Work-relatedness holds where the work exposure is one discernible cause, not the sole or predominant cause | R1 |
| 2006-08-03 | Recording an injury when physician recommends restriction but no restricted work is available | Restricted work where the physician recommends restriction but none is available | R4 |
| 2024-10-22 | Is the use of paraffin wax as a form of topical heat application considered medical treatment beyond first aid | An unlisted treatment tested against the closed first-aid list | R3 |
| 2026-01-20 | Recordability of workplace injuries resulting from personal rechargeable lithium-ion batteries | Work-relatedness of an injury caused by an employee's personal equipment on site | R1 |

Letter URLs follow `https://www.osha.gov/laws-regs/standardinterpretations/<date>`.

### `FORM-301` — OSHA Forms for Recording Work-Related Injuries and Illnesses

| | |
|---|---|
| `doc_type` | `form` |
| Source | https://www.osha.gov/recordkeeping/forms |
| PDF | https://www.osha.gov/sites/default/files/OSHA-RK-Forms-Package.pdf |
| Excerpted | Overview and column definitions (pp. 2–4) · How to Fill Out the Log, Form 300, Form 300A (pp. 6–8) · Form 301 Injury and Illness Incident Report (p. 10) |
| Pages | 7 |
| Anchor | Page number within the forms package. |
| Backs | R4 |

The Form 300 column definitions — G (death), H (days away from work), I (job transfer or restriction), J (other recordable cases) — and the blank Form 301 that the incident packets are built on.

---

## Recorded cross-references

Multi-hop retrieval is only real if a claim genuinely lives across two documents. Each of these has been confirmed present at both ends.

| # | From | To | The hop |
|---|---|---|---|
| 1 | `CPL-172` IX.E.10 | `CFR-1904` § 1904.7(b)(5)(ii) | The directive restates the closed first-aid list verbatim. A worker reaching only the directive has the list but not its regulatory authority; a worker reaching only the regulation has the list but not OSHA's applied reading of it. |
| 2 | `CPL-172` IX.P.1 | `LOI-PACK` 2021-01-08 | The directive's statement that an already-reported hospitalization needs no second report on later death traces to the letter of interpretation that established it. |
| 3 | `FORM-301` column definitions | `CFR-1904` § 1904.7(b)(3) | The G/H/I/J column rules on the form implement the day-counting and most-severe-outcome rules in the regulation, including the 180-day cap. |
| 4 | `FR-2014` § 1904.39 analysis | `CFR-1904` § 1904.39(b)(10), (b)(11) | The preamble is the rulemaking record for the observation-only exclusion and the amputation exclusion list as codified. |
| 5 | `LOI-PACK` 2024-10-22 | `CFR-1904` § 1904.7(b)(5)(ii) | The letter resolves a treatment that is not on the closed list, which is only decidable by reading the list itself. |
| 6 | `LOI-PACK` 2015-04-15 | `CFR-1904` § 1904.39(b)(3)–(4) | The letter's commercial-motor-vehicle guidance sits against the public-street reporting exclusion. |

Cross-references 1, 2 and 4 are the ones the golden set must exercise, because each is a case where retrieving one end and stopping produces a confidently wrong answer.

> **`CPL-172`'s anchors are section designations, not strings.** `IX.E.10` and `IX.P.1` are correct under the directive's own numbering, but neither appears as literal text — the directive prints a lettered section heading followed by numbered items. Verify these by reading the section, not by grepping for the compound designation. The same is true of every `(b)(10)`-style subparagraph cite in this manifest: eCFR renders a section heading and then bare paragraph markers, so the joined form is never written out.

## Retrieval distractors

Queries whose naive keyword match lands on the wrong section. At least one golden case must be built on each of the first three.

| Term | Why it misleads | Where it appears |
|---|---|---|
| `24 hours` | The reporting clock, record-retention language, and the preamble's discussion of alternative clock proposals all use it. Sharper than it looks: § 1904.39 writes the clock as "twenty-four (24) hours", so a literal `24 hours` match returns 38 hits and **none of them are the controlling regulation** | `FR-2014` 32, `CPL-172` 3, `LOI-PACK` 3 — `CFR-1904` 0 |
| `hospital` | Appears in reportable contexts (in-patient admission for care or treatment) and non-reportable ones (observation or diagnostic testing only) with no lexical signal separating them | 290 across five documents — `FR-2014` 231, `CFR-1904` 36, `CPL-172` 11, `LOI-PACK` 11, `FORM-301` 1. Absent from `CFR-269` |
| `amputation` | Appears in the reportable list and in the exclusion list that carves it back | 254 total — `FR-2014` 200, `CFR-1904` 36, `CPL-172` 10, `LOI-PACK` 7, `FORM-301` 1 |
| voltages and clearances | `CFR-269` carries 34 occurrences of `voltage`, 22 of `kV` and 12 of `volts`, most of them unrelated to any approach distance a hazard control would cite | `CFR-269` only |

Counts are reported by `fetch_corpus.py` on every full rebuild. Transcribe them here when an upstream source shifts.

## Declared out-of-corpus topics

Refusal test cases draw from this list. Every topic here has been confirmed to have **zero occurrences** across all six documents, so a grounded answer is impossible and a refusal is the only correct outcome. `fetch_corpus.py` re-checks each one on every full rebuild and fails the build if any of them turns up — reading the search terms from `sources.json`'s `verification.out_of_corpus`, not from this file. The list below is a readable transcription of that array, and the two must be kept in step: a topic that appears here and not there is never checked, and the build will pass while the claim above is false. The eleven topics below expand to fourteen search terms, because three of them are checked under two spellings each — hazard communication and safety data sheets, respiratory protection and fit testing, powered industrial trucks and forklifts.

- Hazard communication and safety data sheets (1910.1200)
- Respiratory protection and fit testing (1910.134)
- Ergonomics and musculoskeletal disorder programs
- Fall protection (1926.501)
- Powered industrial trucks and forklifts
- Respirable crystalline silica
- Process safety management (1910.119)
- Trenching and excavation (1926.650)
- Non-OSHA: GDPR and data protection
- Non-OSHA: Sarbanes-Oxley and financial audit
- Non-OSHA: HIPAA

> Bloodborne pathogens, hearing conservation, whistleblower complaints, asbestos and lead each appear somewhere in the corpus in passing. They are **not** valid refusal topics — a refusal case built on one of them tests the wrong thing, because a retriever that surfaces the passing mention is behaving correctly.

## Near-miss topics

Covered by the corpus but easy to over-refuse. At least one golden case must confirm these are answered, not refused. `fetch_corpus.py` fails the build if one of them goes missing, because a near-miss case built on an absent topic can never fail.

- Needlestick and sharps injuries — § 1904.8, and again in `CPL-172` IX.E and the Form 300 instructions
- Hearing loss recording — `CPL-172` IX.E, and the Form 300 column instructions
- Tuberculosis cases — `CPL-172` IX.E.15, citing § 1904.11
- Privacy-concern cases and the privacy case list — § 1904.29
