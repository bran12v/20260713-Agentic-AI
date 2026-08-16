# Perimeter corpus manifest

Six documents, 89 pages, 40,387 words. Retrieved 13 August 2026. eCFR issue date 4 August 2026.

Every document is federal public-domain material. This file records where each came from, what a citation to it must resolve to, and the three things the evaluation suite is built from: the cross-references, the retrieval distractors, and the declared out-of-corpus and near-miss topic lists.

## Documents

### `CFR-164D` — 45 CFR Part 164, Subpart D (Breach Notification) plus § 164.514

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-45.xml?part=164` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 164.400, 164.402, 164.404, 164.406, 164.408, 164.410, 164.412, 164.414 and 164.514, each in full |
| Pages | 15 |
| Anchor | Section number, and paragraph designation where the determination turns on one. The eCFR structural API has no pagination. |
| Backs | R1–R4 |

The controlling text, and short enough to carry whole.

**§ 164.402 is the trap, in 2,611 characters.** It defines breach, then does two things in sequence that a reader can easily collapse into one. Paragraph (1) **excludes** three situations outright: unintentional acquisition by a workforce member in good faith and within scope, inadvertent disclosure between two authorised people at the same entity, and a disclosure the recipient could not reasonably have retained. Paragraph (2) then says that anything *not* excluded is **"presumed to be a breach unless the covered entity... demonstrates that there is a low probability that the protected health information has been compromised"** through a risk assessment of at least four named factors.

The burden runs the opposite way from intuition. An impermissible disclosure is a breach by default, and staying silent requires an affirmative demonstration. §§ 164.404, 164.406 and 164.408 then set who must be told and when; § 164.412 allows delay for law enforcement; § 164.514 supplies the de-identification standard, including the eighteen Safe Harbor identifiers.

**§ 164.514 is not in Subpart D.** It sits in Subpart E, the Privacy Rule, and is carried here because R2 cannot run without it. The doc id and the document title both say Subpart D for brevity, so the `section_path` your chunker records must come from the section number itself, not from the document — a chunk of § 164.514 filtered as Subpart D is filed under the wrong rule.

### `CFR-164C` — 45 CFR Part 164 Subpart C, Security Standards

| | |
|---|---|
| `doc_type` | `regulation` |
| Source | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C |
| API | `https://www.ecfr.gov/api/versioner/v1/full/2026-08-04/title-45.xml?part=164` |
| Issue date | 4 August 2026 |
| Excerpted | §§ 164.302, 164.304, 164.306, 164.308, 164.310, 164.312, 164.314 and 164.316, each in full |
| Pages | 11 |
| Anchor | Section number and implementation specification. |
| Backs | — (grounds the conditional worker) |

The Security Rule, carried whole. § 164.306(d) is the section that matters most for the third leg: it splits every implementation specification into **required** and **addressable**, and defines "addressable" as a decision the entity must document — not an option it may ignore. Encryption at § 164.312(a)(2)(iv) and § 164.312(e)(2)(ii) is addressable, which is why an unencrypted device is a defensible position only if the assessment and the alternative were both written down.

### `FR-2013` — 78 FR 5566, the HIPAA Omnibus Final Rule

| | |
|---|---|
| `doc_type` | `preamble` |
| Source | https://www.federalregister.gov/documents/2013/01/25/2013-01073/modifications-to-the-hipaa-privacy-security-enforcement-and-breach-notification-rules-under-the |
| PDF | `https://www.govinfo.gov/content/pkg/FR-2013-01-25/pdf/2013-01073.pdf` |
| Published | 25 January 2013 |
| Excerpted | Printed pp. 5639–5647 (PDF 74–82), the breach definition and risk assessment; pp. 5654–5658 (PDF 89–93), the notification requirements |
| Pages | 14 |
| Anchor | Federal Register page number. The excerpt is **two non-contiguous runs**, so no single offset works: shipped pp. 1–9 are printed 5639–5647, and shipped pp. 10–14 are printed 5654–5658. |
| Backs | R1, R3 |

The rulemaking record, and the reason the current rule reads as it does. The 2009 interim rule had a **harm standard** — notify unless the incident posed a significant risk of harm. HHS replaced it in 2013 with the presumption plus the four-factor assessment, precisely because the harm standard let entities reason their way out of notifying. These fourteen pages are where that reasoning is set out, and "low probability" appears sixteen times in them against once in the regulation.

Excluded: the other 123 pages, covering the Privacy, Enforcement and GINA modifications.

### `DEID-GUID` — HHS Guidance on De-identification

| | |
|---|---|
| `doc_type` | `guidance` |
| Source | https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html |
| PDF | `https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/understanding/coveredentities/De-identification/hhs_deid_guidance.pdf` |
| Published | 26 November 2012 |
| Excerpted | Printed pp. 4–9, the overview of both methods; pp. 23–30, the Safe Harbor guidance |
| Pages | 14 |
| Anchor | Guidance page number, which matches the PDF page. |
| Backs | R2 |

The question that precedes every other one: is this information protected health information at all? The guidance walks the Safe Harbor method identifier by identifier and is far more concrete than § 164.514(b)(2)'s bare list — it says what "actual knowledge" of re-identification means, and how the three-digit ZIP rule works.

Excluded: pp. 10–22, the expert determination method, which is a statistical-disclosure discipline no rule in this system applies.

### `SEC-SERIES` — HHS HIPAA Security Series

| | |
|---|---|
| `doc_type` | `guidance` |
| Source | https://www.hhs.gov/hipaa/for-professionals/security/guidance/index.html |
| Excerpted | Administrative Safeguards paper pp. 3–15, and the Guidance on Risk Analysis Requirements pp. 1–9, assembled from two upstream PDFs |
| Pages | 22 |
| Anchor | Paper title and page number. |
| Backs | — (grounds the conditional worker) |

HHS's own reading of the Security Rule, and the third leg's interpretive layer. The Administrative Safeguards paper walks each standard and marks every specification required or addressable; the Risk Analysis guidance says what a compliant risk analysis has to contain.

These papers date from 2005 and were last revised in 2007. They are carried because they remain HHS's published explanation of specifications that have not changed, but a claim about current expectations should cite the regulation, not the paper.

### `FORM-OCR` — OCR breach report and complaint forms

| | |
|---|---|
| `doc_type` | `form` |
| Source | https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf |
| Excerpted | The breach portal's required-information document (9 pp) and the Health Information Privacy Complaint form (4 pp), assembled from two upstream PDFs |
| Pages | 13 |
| Anchor | Form field or question number. |
| Backs | R3, R4 |

What the Secretary actually asks for. The breach portal document enumerates every field a report must carry — including the date of the breach, the **date of discovery**, the number of individuals affected, the type of breach and the safeguards in place before it. The complaint form is the individual's side, and its question set is what the packets' own intake form is modelled on — the packets carry a form the team designs, because no federal incident intake form exists to build them on.

There is no paper breach report. Submission is through the portal, which is why the corpus carries the question set rather than a form.

## Recorded cross-references

Multi-hop retrieval is only real if a claim genuinely lives across two documents. Each of these has been confirmed present at both ends.

| # | From | To | The hop |
|---|---|---|---|
| 1 | `FR-2013` breach definition | `CFR-164D` § 164.402(2) | The preamble explains that the presumption replaced a harm standard and why; the regulation states the presumption in one sentence and never explains it. |
| 2 | `FR-2013` risk assessment | `CFR-164D` § 164.402(2)(i)–(iv) | "risk assessment" appears 48 times in the preamble against once in the regulation. The four factors are only elaborated in the preamble. |
| 3 | `DEID-GUID` Safe Harbor | `CFR-164D` § 164.514(b)(2) | The regulation lists eighteen identifiers; only the guidance says what removing them requires in practice. |
| 4 | `SEC-SERIES` administrative safeguards | `CFR-164C` § 164.306(d) | The paper marks each specification required or addressable; the regulation defines what "addressable" obliges an entity to do. |
| 5 | `FORM-OCR` breach report | `CFR-164D` § 164.404(a)(2) | The portal asks for a date of discovery; only the regulation says what discovery means and what clock it starts. |
| 6 | `CFR-164C` encryption specifications | `CFR-164D` "unsecured" | Whether PHI is unsecured — and therefore whether Subpart D applies at all — turns on encryption, which Subpart C makes addressable rather than required. |

Cross-references 1 and 2 are the chain the golden set must exercise. They are where a worker that retrieves the regulation and stops has the rule but not the burden of proof.

## Retrieval distractors

Queries whose naive keyword match lands on the wrong section. At least one golden case must be built on each of the first three.

| Term | Why it misleads | Where it appears |
|---|---|---|
| `risk assessment` | The **four-factor breach assessment** under § 164.402(2). One word away from an entirely different mandatory exercise | 52 total — `FR-2013` 48, `SEC-SERIES` 3, `CFR-164D` 1 |
| `risk analysis` | The **Security Rule risk analysis** under § 164.308(a)(1)(ii)(A). A different exercise, in a different subpart, on a different schedule, with a different output | 57 total — `SEC-SERIES` 54, `FORM-OCR` 2, `CFR-164C` 1 |
| `addressable` | Reads as optional and is not. § 164.306(d) requires an entity that skips an addressable specification to document why and what it did instead | 40 total — `CFR-164C` 26, `SEC-SERIES` 14 |
| `breach` | The single most overloaded term. It carries the § 164.402 term of art, the ordinary English sense, and the portal's field labels | 391 total — `FR-2013` 297, `FORM-OCR` 46, `CFR-164D` 45, and single mentions elsewhere |

**The first two are the sharpest pair in this corpus, and they are almost perfectly disjoint by document.** "risk assessment" lives in the breach documents; "risk analysis" lives in the security documents. A retriever that treats them as synonyms does not return a slightly wrong passage — it returns the wrong subpart, and answers a breach question with a security-programme obligation or the reverse. Build a golden case on each.

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
- Non-HIPAA: GDPR and data protection
- Non-HIPAA: Sarbanes-Oxley and financial audit
- Healthcare but not HIPAA: the anti-kickback statute
- Healthcare but not HIPAA: the Stark Law

> The last two are the useful ones. They sit inside healthcare compliance, an analyst could plausibly ask about either while working a breach, and neither appears anywhere in this corpus. A refusal on GDPR is easy; a refusal on anti-kickback is the one worth testing.

> **A third category must be refused for a different reason, and it needs care.** Nearly every state imposes its own breach notification law, often with a shorter clock and a broader definition of personal information than HIPAA's. **No state statute is carried here.** A question about what a particular state requires has no grounding and must be refused with the gap named — answering from the federal rule would be wrong in the direction that matters.
>
> The care is this: the phrase "state law" appears **12 times in `FR-2013`**, where the preamble discusses *preemption* — when HIPAA displaces a state requirement and when it does not. So the corpus can answer "how does HIPAA relate to state law" and cannot answer "what does my state require". A refusal case must be written against the second question, not the first, or it tests the wrong thing.

## Near-miss topics

Covered by the corpus but easy to over-refuse. At least one golden case must confirm these are answered, not refused. `fetch_corpus.py` fails the build if one of them goes missing, because a near-miss case built on an absent topic can never fail.

- Business associates — 265 occurrences; § 164.410 sets their notification duty and `FR-2013` discusses it at length
- Law enforcement delay — 7 occurrences; § 164.412 and `FR-2013`. Thin, and the thinnest of the four
- Notice of privacy practices — 4 occurrences, in `CFR-164D` and `FR-2013`. Not in `FORM-OCR`
- Limited data sets — 38 occurrences; `CFR-164D` § 164.514, `FR-2013`, and once in `DEID-GUID`

## Drift note

The breach rule has been stable since the Omnibus Rule took effect in 2013, and the eCFR pin reproduces Subparts C and D exactly.

Three cautions. The **guidance is old** — the Security Series papers are from 2005 with a 2007 revision, and the de-identification guidance from 2012; they explain specifications that have not changed, but they are not statements of current enforcement posture. **No state law is carried**, and state breach statutes are frequently stricter than HIPAA on both the clock and the definition of covered information. And the OCR **breach portal is a web application**, so the question set carried here is a snapshot of what it asked on the retrieval date rather than a stable form with an edition number.
