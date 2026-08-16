# Cohort 2026-07 Project 2 — Regulatory Determination Copilots

## Overview

Each two-person team is assigned one of **ten regulatory-determination projects**. Every project builds the same system against a different body of federal regulation: a multi-agent document analysis pipeline that cracks an incident packet, retrieves grounding evidence from a shipped public-domain corpus, applies published thresholds deterministically, and drafts a cited dossier for a human to approve.

The briefs share an identical technical specification, an identical acceptance checklist, and an identical architecture — only the regulatory domain changes. Teams cannot copy each other's work, and every team is graded against the same bar.

## The ten projects

| # | Product | Determination domain | Folder | Regulatory source |
|---|---|---|---|---|
| 01 | FieldSight | Workplace injury recordability and reporting | `project2-OSHA/` | OSHA · 29 CFR 1904, 1910.269 |
| 02 | Attestor | Employment eligibility verification | `project2-I9/` | USCIS · ICE · IER · 8 CFR 274a |
| 03 | Roadwatch | Driver hours of service and qualification | `project2-FMCSA/` | FMCSA · 49 CFR 395, 391 |
| 04 | Cradle | Hazardous waste determination and manifesting | `project2-RCRA/` | EPA · 40 CFR 261, 262, 268 |
| 05 | Perimeter | Protected health information breach notification | `project2-HIPAA/` | HHS OCR · 45 CFR 164 |
| 06 | Straighttime | Wage and hour exemption and regular rate | `project2-FLSA/` | DOL WHD · 29 CFR 541, 778, 785 |
| 07 | Ledgerline | Suspicious activity and currency transaction reporting | `project2-AML/` | FinCEN · FFIEC · OFAC · 31 CFR 1010, 1020 |
| 08 | Vigil | Medical device change control and adverse event reporting | `project2-FDA/` | FDA · 21 CFR 803, 806, 807 |
| 09 | Payline | Worker classification and payroll deposits | `project2-IRS/` | IRS · 26 CFR 31 |
| 10 | Claimpath | Medicare admission status and appeals | `project2-CMS/` | CMS · 42 CFR 412, 405 |

Team assignments are made by the instructor. Each folder is self-contained — a team is handed one folder and needs nothing outside it.

## What every project ships with

The knowledge base is not the learners' problem to source. Each folder contains:

| Path | What it is |
|---|---|
| `project2-requirements-2person.md` | The brief. Sixteen numbered sections ending in an acceptance checklist. |
| `packet-preparation.md` | How to build the four fictional incident packets, including which one must be handwritten and scanned. |
| `corpus/pdf/` | Six or seven excerpted public-domain documents, 70 to 93 pages, committed. The count follows the domain — most regulatory schemes fit in six. The FLSA needs seven because it splits across four separate CFR parts, and the IRS project needs seven because two regulations, two published guidance documents and two IRS publications each carry a different piece of the test. |
| `corpus/text/` | Plain-text extraction of each, committed so a diff reveals upstream drift. |
| `corpus/sources.json` | The URL manifest — source addresses, section lists, page ranges. |
| `corpus/fetch_corpus.py` | Rebuilds `pdf/` and `text/` from `sources.json` on a clean clone. Byte-identical across all ten projects. Requires reportlab 5.0.0 and pypdf 6.16.1 — a different renderer rewrites every PDF. |
| `corpus/MANIFEST.md` | Provenance and anchors per document, the verified cross-references, the retrieval distractors with occurrence counts, and the declared out-of-corpus and near-miss topic lists. |

What is still the team's to build: cracking those PDFs with Document Intelligence, chunking them, indexing them, tuning retrieval against them, and encoding their thresholds in Python.

## What is identical across the ten

The tech stack, the seven Azure services and their assigned jobs, the ingestion and retrieval requirements, persistence, the tool and MCP-server contract, the guardrail and escalation harness, security, the non-functional targets, deployment and the deliverables. Those sections are identical in substance brief to brief — what changes within them is the domain noun (incident, denial, worker file), the doc ids named in an example, and the occasional domain-specific clause, such as the extra seeding requirement in the IRS project's persistence section or the clinical-narrative redaction clause in the CMS project's security section.

## What varies

The regulatory domain, the corpus documents, the four incident packets, the three worker agents and their dispatch conditions, rules R1 through R4, the CLI verb, and the first adversarial evaluation case. R5 — the extraction confidence floor — is a pipeline parameter and is the same everywhere.

One project varies further. In the IRS project the conditional third leg fires on a predicate over the *fan-in result* — employee **and** no relief — rather than on a Coordinator conditional edge reading the packet, so its workflow graph carries a gate the other nine do not. That is a domain consequence, not an authoring accident: what is owed cannot be asked until both prior determinations have gone against the firm.

Every domain was selected against the same structural requirements, because each one carries a graded requirement:

- **Two determinations that can diverge**, so the workflow has something real to fan out over.
- **Hard numeric clocks and a closed enumerated list**, so the rules engine has boundaries to unit-test on both sides.
- **A narrow exclusion that carves back the general rule**, so one packet forces a Reviewer rejection and a narrowed re-dispatch.
- **A table-heavy document** reachable only by the conditional third worker, so table extraction is worth checking.
- **A real handwritable government form**, so at least one artifact reaching Document Intelligence is image-based.
- **Interpretation letters and a rulemaking preamble**, so multi-hop retrieval and the parametric-memory adversarial case have somewhere to land.

## Checking the briefs

`check_briefs.py` runs twenty structural checks over all ten projects at once:

```bash
python check_briefs.py            # all ten
python check_briefs.py OSHA IRS   # named projects only
```

It exits non-zero on failure, so it can gate a build. Every check is there because
the matching defect was found in a shipped brief at least once — page and word
arithmetic against the real corpus, the conditional worker's access to the rules
engine, cross-reference counts against the manifest's designated chain, golden-set
sums, workflow-diagram alignment, the `sources.json` verification lists, every §5
rule source resolving in its own corpus, the §3 phrases trainees are told to encode
verbatim, occurrence counts quoted in §3, outcome values named without a rule
qualifier, every file in the packet tree being described and exemplified, each
project naming one packet that clears every §9 trigger, the packet dates being
specified packet by packet, entitlements having a partition to be entitlements
over, the run record carrying what §12 measures from it, §16 grading the
near-boundary mechanism §9 requires everywhere, the multimodal step being pointed
only at images a packet actually ships, and markdown that breaks a list on GitHub.

One thing to know before trusting a failure or a pass: the corpus text is
hard-wrapped at 92 characters, so a multi-word phrase is routinely split across a
newline. Every search collapses whitespace first, as `fetch_corpus.py` does. A
plain `grep` over `corpus/text/` reports present phrases as missing — do not
correct a manifest on the strength of one.

## Shared brief structure

All ten briefs run the same sixteen sections in the same order: what the system does · tech stack · the corpus · agents and orchestration · the rules engine · ingestion and retrieval · persistence · tools and the MCP server · the harness · security · the CLI · non-functional targets · evaluation · deployment · deliverables · acceptance checklist.

## Deliverables

Per the brief's §15, every team delivers a repository, an architecture document, an evaluation report, five demonstration artifacts, and a rehearsed 5–7 minute live demo. Both team members must be able to answer questions about any part of the system.

## Assessment

There is no percentage rubric. §16 of each brief is an acceptance checklist of forty-odd single-assertion items grouped into corpus and packets, architecture, determinism and escalation, grounding and sessions, security, and delivery. A common core runs through all ten in the same order and the same words, with the domain noun substituted. On top of that each brief carries items naming its own documents, its own rules and the tests that prove them, so the totals differ by a few — currently thirty-nine to forty-six.

## Prerequisites

The project draws on Weeks 05 through 09 — agent construction, tool binding, multi-agent topologies, the MCP server, RAG over pgvector, Azure AI Foundry, and evaluation.

One deliberate discontinuity: the curriculum teaches LangChain and LangGraph, and the brief bans both from the orchestration, retrieval and write path. Teams build on the Microsoft Agent Framework instead. The concepts transfer; the API does not. That transfer is part of what the project tests, and it is why the brief requires pinned versions and a note in the architecture document recording them.
