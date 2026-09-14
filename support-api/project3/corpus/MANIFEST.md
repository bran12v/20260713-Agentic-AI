# Corpus Manifest

The knowledge base the system retrieves against. § 4.7 makes retrieval load-bearing — the runbook
determines the verification steps an action requires, and a lane that cannot retrieve its governing
section blocks and escalates. That only works if this file is accurate.

**The laptop manuals are sourced, verified and committed as text. Everything else is a specification
with its content unfilled.** The runbook, policy and tool-access material exists and is being handed
over. Nothing below is invented — the empty tables carry the shape each entry must take, and filling
them is the first task of Knowledge & Retrieval, done by reading the real documents rather than by
guessing at them. The manual rows show what a filled row looks like.

---

## 1. Documents

One row per document. `doc_id` is stable and is what citations resolve against, so it is chosen once
and never renamed.

| `doc_id` | Document | `doc_type` | `device_model` | Pages |
|---|---|---|---|---|
| | | `runbook` | — | |
| | | `policy` | — | |
| | | `access_matrix` | — | |
| `MANUAL-G15-5510-SVC` | Dell G15 5510 Service Manual (P105F) | `manual` | Dell G15 5510 | 73 |
| `MANUAL-G15-5510-SPEC` | Dell G15 5510 Setup and Specifications (P105F) | `manual` | Dell G15 5510 | 21 |
| `MANUAL-LAT-5420-SVC` | Latitude 5420 Service Manual (P137G) | `manual` | Dell Latitude 5420 | 109 |
| `MANUAL-LAT-5420-SPEC` | Latitude 5420 Setup and Specifications (P137G) | `manual` | Dell Latitude 5420 | 25 |
| `MANUAL-LAT-5521-SVC` | Latitude 5521 Service Manual (P104F) | `manual` | Dell Latitude 5521 | 125 |
| `MANUAL-LAT-5521-SPEC` | Latitude 5521 Setup and Specifications (P104F) | `manual` | Dell Latitude 5521 | 31 |
| `MANUAL-LAT-5521-REIMAGE` | Latitude 5521 Re-imaging guide for Windows 10 (P104F) | `manual` | Dell Latitude 5521 | 16 |
| `MANUAL-LAT-5550-SPEC` | Latitude 5350/5450/5550 Spec Sheet | `manual` | Dell Latitude 5550 | 17 |
| `MANUAL-LAT-7350-GUIDE` | Latitude 7350 Technical Guidebook (P179G/P178G) | `manual` | Dell Latitude 7350 | 50 |
| `MANUAL-PREC-3460-GUIDE` | Precision 3460 SFF Technical Guidebook (D17S) | `manual` | Dell Precision 3460 | 49 |
| `MANUAL-PREC-3460-SPEC` | Precision 3460 SFF Spec Sheet | `manual` | Dell Precision 3460 | 9 |
| `MANUAL-HP-635-AERO-G7` | HP ProBook 635 Aero G7 Maintenance and Service Guide | `manual` | HP ProBook 635 Aero G7 | 106 |
| `INFO-MBP14-M3` | MacBook Pro (14-inch, M3, Nov 2023) — Info | `manual` | Apple MacBook Pro (14-inch, Nov 2023) | 1 |
| `INFO-MBP14-M3PRO-MAX` | MacBook Pro (14-inch, M3 Pro / M3 Max, Nov 2023) — Info | `manual` | Apple MacBook Pro (14-inch, Nov 2023) | 1 |
| `GUIDE-ME-AND-MY-DELL` | Me and My Dell — generic Dell usage guide | `general` | **null, deliberately** | 60 |

**All eight fleet models are covered. What gets indexed is `manuals/text/` — one markdown file
per model, ~500 KB in total, already extracted from these fifteen documents.** The fifteen vendor
PDFs ship alongside them in `manuals/`, so Document Intelligence can crack the originals without
fetching anything. `python manuals/fetch_manuals.py --verify-only` re-checks them against
`manuals/sources.json`, and `python manuals/extract_text.py` regenerates the text.

**Coverage is not uniform, and the difference is load-bearing.** Each model file states its
troubleshooting depth in its header: `full` for the Latitude 5420, 5521, G15 5510 and HP ProBook;
`partial` for the Latitude 7350 and Precision 3460 — specifications and views, no procedures; `none`
for the Latitude 5550, which has a spec sheet and nothing else; `pointers` for the MacBook Pro, whose
file routes symptoms to Apple's own articles rather than containing the answer. A question the corpus
cannot answer for a given model must refuse, not borrow the answer from a different one.
[`manuals/SOURCES.md`](manuals/SOURCES.md) maps question classes to the models that can answer them.

`GUIDE-ME-AND-MY-DELL` carries a null `device_model` on purpose — it covers Inspiron, G-Series, XPS
and Alienware generically, so tagging it to one model would let a model-filtered query about a
specific machine be answered from content written for four product families. It is the one file in
`text/` that no model-filtered query will ever return.

The runbook, policy and access-matrix rows above are still the project's to fill.

`doc_type` is a closed set: `runbook`, `policy`, `access_matrix`, `manual`, `closed_ticket`. It is a
filterable field at index-creation time, and the multi-hop requirement depends on it — reaching a
second document deliberately means filtering on what kind of document it is.

`manual` rows additionally carry `device_model`, which § 4.7 makes a **required** filter on every
manual query.

---

## 2. Cross-references — the multi-hop chains

§ 4.7 requires workers to follow these deliberately. Each must be **verified present at both ends**:
the section that defers, and the section it defers to. A chain that only exists in one direction is
not a chain.

| # | From | To | Why one document cannot answer it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

The shape to look for: a runbook states an obligation and defers its verification requirement to a
separate identity-proofing policy. Neither document answers "may I reset this password" alone — the
runbook says a reset requires verification, and only the policy says what verification means for a
privileged account.

**At least two chains, and § 7 requires a golden case on each.**

---

## 3. Retrieval distractors

Terms where the highest-scoring chunk is not the right one. Record the occurrence count per document,
because the count is the evidence — a term appearing four times in the wrong document and twice in the
right one is what actually defeats a naive query.

| Term | Occurrences by document | Why it misleads |
|---|---|---|
| `reset` | | Spans password reset, MFA reset and device reset — three different procedures, three different runbooks |
| `Latitude 5420` | | **Found while sourcing.** The Latitude 5420 Rugged (P85G) is a different computer that shares the marketing name, and its manual is 145 pages of confident, entirely wrong procedure. Matching on the model name alone does not separate them — only the regulatory model does |
| `memory` on the Latitude 5550 | | **Found while sourcing.** The 5550 spec sheet is a three-column comparison of the 5350, 5450 and 5550. Extraction keeps the row labels and loses the column headers, so one `MEMORY OPTIONS` chunk holds all three models' values with nothing marking which is which — the 13-inch 5350's soldered LPDDR5 sits directly above the 5550's upgradeable DDR5. `device_model` filtering does not help: the chunk is in the right document and about the wrong machine |
| `power light blinking` | | The Latitude 7350 guidebook describes battery-**charge** LED behaviour — "blinking yellow, battery charge is critical" — and carries no diagnostic blink-code table. It reads like an answer to "the power light is blinking" and answers a different question. The 5420, 5521 and G15 carry the real code table |
| | | |

**Three distractors minimum, and § 7 requires a golden case built on each.**

The dangerous kind is not an obviously ambiguous word. It is near-identical wording across two
operations, where the wrong answer is fluent, specific, and carries a citation that resolves. The
laptop manuals are the known example: § 4.7 already records that manuals across models are
near-identical prose carrying different part numbers and key sequences, so an unfiltered query answers
confidently from the wrong machine.

---

## 4. Out-of-corpus topics

Topics confirmed to have **zero** occurrences anywhere in the corpus. § 7 draws its refusal cases from
this list, and a refusal is only a fair test if the answer genuinely is not present.

| Topic | Confirmed absent |
|---|---|
| VPN and remote network access | ☐ |
| Email and Outlook | ☐ |
| **Entra ID account lockouts and password resets** | ☐ |
| Software installation and licensing | ☐ |
| "My laptop is slow" | ☐ |
| Disk-space and storage-usage questions | ☐ |
| Printer setup | ☐ |
| Any SkillStorm line-of-business application | ☐ |
| Any laptop model not in the fleet | ☐ |

The manuals draw the sharpest out-of-corpus boundary in this corpus, and **the account-lockout row is
the dangerous one**. It sits one word from something the manuals *do* answer: a BIOS password is in
the manual, an Entra ID password is not, and they are different things resolved by different
procedures. § 7 should carry a paired case proving the two do not bleed into each other.

The last row is the near-miss boundary — a question about a Latitude 7420 must refuse rather than
answer from the 7350, which is only enforceable because `device_model` is a required filter.

**Three refusals are required *inside* the fleet**, and they are the ones most likely to be got wrong,
because the model genuinely is in the corpus:

| Topic | Confirmed absent |
|---|---|
| Any troubleshooting procedure for the **Latitude 5550** — it has a spec sheet and nothing else | ☑ |
| BIOS setup content for the **Latitude 5550** or the **Precision 3460** | ☑ |
| A diagnostic LED blink-code table for the **7350**, **3460** or **5550** | ☑ |

"My 5550 won't turn on" must escalate, not borrow the 5521's flea-power procedure. These three are
already verified against the committed text; the rows above them are not.

**Eight minimum.** Verify by search, not by assumption — a topic that turns out to be covered makes a
passing refusal test into a false negative that hides a real failure.

---

## 5. Near-miss topics

Topics that **are** covered and must not be refused. These catch the opposite failure: a refusal
threshold tuned so high that the system declines things it can actually answer.

| Topic | Where it is covered |
|---|---|
| A forgotten **BIOS** password on a 5420, 5521 or G15 | `MANUAL-*-SVC` → System setup → Clearing system and setup passwords. Pairs with the Entra ID lockout row above — same word, different machine, different procedure |
| A laptop that will not power on at all | `MANUAL-*-SVC` → Troubleshooting → Drain residual flea power. Pairs with "my laptop is slow", which is not covered |
| A bulging case or a laptop that rocks on the desk | `MANUAL-*-SVC` → Troubleshooting → Handling swollen Li-ion batteries. A safety answer that must never be refused |
| Reinstalling Windows and the order drivers go back in | `MANUAL-LAT-5521-REIMAGE`. Pairs with software installation and licensing, which is not covered |
| | |

**Four minimum**, each adjacent to something on the out-of-corpus list, so the pair genuinely tests the
boundary rather than two unrelated questions. The four above come from the manuals and are verified
present; at least one more should come from the runbook or policy once those are indexed.

---

## 6. Chunking and index

Record what was chosen, because the reranker threshold in § 4.7 is only reproducible against a known
chunking.

| Setting | Value |
|---|---|
| Chunk size | |
| Overlap | |
| Split strategy | Structure-aware on headings, falling back to size |
| Filterable fields | `doc_type`, `section_path`, `device_model` |
| Chunk id scheme | Stable and deterministic — a citation must resolve after a re-index |

**Manuals are cracked with Azure AI Document Intelligence, retaining table structure.** Service
manuals carry their part numbers and step sequences in tables; a chunker that flattens them produces
citations that resolve to the wrong row, which is worse than not resolving at all. The committed
`manuals/text/` is the ground truth to measure that extraction against — two known table failures are
already visible in it, and recovering either is a concrete, checkable win:

- **The Latitude 5550's three-column comparison collapses into one column**, which is § 3's second
  distractor. Layout-aware extraction is what restores the model-to-value association.
- **Diagnostic LED codes extract in two shapes.** The G15 renders `2,3 No memory or RAM detected` on
  one line; the 5420 and 5521 render the same table as split columns — a bare `2`, a bare `8`, then
  `LCD Power Rail Failure`. **A chunker that strips short numeric lines as page furniture deletes the
  second form entirely.** That is not hypothetical; it happened while building this corpus, and
  `extract_text.py` carries a comment saying why the page-number rule was removed.

---

## 7. Provenance

Per document: where it came from, when it was retrieved, and which sections were excerpted. A corpus
whose provenance is unrecorded cannot be rebuilt, and a corpus that cannot be rebuilt cannot be
re-evaluated after it drifts.

| `doc_id` | Source | Retrieved | Sections |
|---|---|---|---|
| every `MANUAL-*` and `INFO-*` row | [`manuals/sources.json`](manuals/sources.json) — vendor URL, regulatory model, revision, page count, and a `wayback` block on the five pulled from the Internet Archive | recorded per document | Troubleshooting · System Setup / BIOS · Views · Specifications · Drivers · HP diagnostics and recovery. **Teardown chapters are excluded** — 90 pages of screw sizes in the 5521 alone, answering nothing a user asks |
| | | | |

`sources.json` is the manuals' provenance record and the rebuild script reads it, so the two cannot
drift: `python manuals/fetch_manuals.py --verify-only` re-checks every document against its recorded
page count, expected title text and regulatory model. That last check is the one that matters — it is
what caught a 145-page manual for the wrong computer.

Five documents come from the Internet Archive rather than the vendor, because Dell removed them from
its live site. They are Dell's own bytes, fetched through the Wayback `id_` raw form, and they pass
the same verification as everything else. `SOURCES.md` records the method; it is reusable.
