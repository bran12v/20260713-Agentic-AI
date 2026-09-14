# Laptop Manuals — What They Answer, and What They Cannot

These documents ground the Device Worker so it can answer a user's question about their laptop.
§ 4.7 makes `device_model` a **required** filter on every query against them.

**All eight fleet models are covered, and they are not covered equally.** Three have a full service
manual with diagnostic procedures. Two have an engineering guidebook — specifications and views, no
procedures. One has a marketing spec sheet and nothing else. The MacBook Pro has no vendor PDF at all
and carries a curated index of Apple's own articles instead. The per-model depth is stated in each
file's header and in the coverage table below, and the Device Worker is expected to act on it: a
question the corpus cannot answer for a given model must refuse, not borrow an answer from a
different one.

Every file here was opened and read before being kept. That is not ceremony — three documents turned
out not to be what their filename or URL implied, and one of them was a different computer.

---

## What the team actually indexes

`text/` holds **one markdown file per model**, ~500 KB in total. That is the corpus — it is what
gets chunked and indexed. The fifteen vendor PDFs ship beside it (~178 MB) so nothing has to be
downloaded; `python fetch_manuals.py --verify-only` re-checks them against `sources.json`.

```
corpus/manuals/
├── sources.json          15 documents — URLs, regulatory models, per-document warnings
├── fetch_manuals.py      download + verify.  `python fetch_manuals.py --verify-only`
├── extract_text.py       PDF -> text/<model>.md.  `python extract_text.py 5521`
└── text/                 COMMITTED. This is what gets chunked and indexed.
    ├── apple-macbook-pro-14-inch-nov-2023.md    16 KB
    ├── dell-g15-5510.md                         49 KB
    ├── dell-latitude-5420.md                    76 KB
    ├── dell-latitude-5521.md                   110 KB
    ├── dell-latitude-5550.md                    68 KB
    ├── dell-latitude-7350.md                    57 KB
    ├── dell-precision-3460.md                   87 KB
    ├── hp-probook-635-aero-g7.md                52 KB
    └── dell-general-all-models.md               13 KB   <- device_model is null, deliberately
```

**Teardown chapters are excluded on purpose.** "Removing and installing components" is 90 pages of
screw sizes in the Latitude 5521 alone and answers nothing a user asks. What survives is
Troubleshooting, System Setup / BIOS, Views, Specifications, Drivers, and the HP diagnostics and
recovery chapters. Anyone who needs a teardown procedure has the full PDF a command away.

Every file opens with a provenance header — model, regulatory model, troubleshooting depth, and every
source document with its URL and what it answers. Chapter headings carry the source document and page
range, so a citation resolves to a page in a named vendor PDF rather than to "the manuals".

---

## Coverage

| Model | Troubleshooting | Documents | Source |
|---|---|---|---|
| Dell Latitude 5420 | **full** | Service Manual · Setup and Specifications | Dell |
| Dell Latitude 5521 | **full** | Service Manual · Setup and Specifications · re-imaging guide | Dell · archive |
| Dell G15 5510 | **full** | Service Manual · Setup and Specifications | Dell · archive |
| HP ProBook 635 Aero G7 | **full** | Maintenance and Service Guide | HP |
| Dell Latitude 7350 (2024) | partial | Technical Guidebook | archive |
| Dell Precision 3460 | partial | Technical Guidebook · spec sheet | archive · Dell |
| Dell Latitude 5550 | **none** | Spec sheet only | archive |
| Apple MacBook Pro 14-inch (Nov 2023) | pointers | 2 Info sheets · index of 10 Apple articles | Apple |

`partial` means specifications, views and some diagnostic-LED behaviour, but no troubleshooting
procedures. `none` means specifications only. `pointers` means the file routes a symptom to a vendor
URL rather than containing the answer.

---

## What a user asks, and which models can answer

The map into the corpus, and the honest ceiling on it. A blank cell is a refusal, not a gap to paper
over with a neighbouring model's manual.

| The user says | Section | Models that answer |
|---|---|---|
| "The power light is blinking amber" | Troubleshooting → System diagnostic lights | 5420 · 5521 · G15 |
| "My screen is black or flickering" | Troubleshooting → Built-in self-test (LCD-BIST, L-BIST) | 5420 · 5521 |
| "The case is bulging / it rocks on the desk" | Troubleshooting → Handling swollen Li-ion batteries | 5420 · 5521 · G15 |
| "Wi-Fi won't connect" | Troubleshooting → Wi-Fi power cycle | 5420 · 5521 · G15 |
| "It won't turn on at all" | Troubleshooting → Drain residual flea power | 5420 · 5521 · G15 |
| "The clock keeps resetting" | Troubleshooting → Real-Time Clock (RTC) reset | 5521 |
| "How do I run diagnostics?" | SupportAssist pre-boot · HP PC Hardware Diagnostics · Apple Diagnostics | 5420 · 5521 · G15 · HP · MacBook *(pointer)* |
| "I need to reinstall Windows / macOS" | Recovering the operating system · HP backup and recovery · the 5521 re-imaging guide for driver order | 5420 · 5521 · G15 · HP · MacBook *(pointer)* |
| "How do I boot from a USB stick?" | System setup → One Time Boot menu, Boot Sequence | 5420 · 5521 · G15 · HP · MacBook *(pointer)* |
| "I forgot the BIOS password" | System setup → Clearing system and setup passwords | 5420 · 5521 · G15 |
| "What ports does it have?" | Views · HP → Components | 5420 · 5521 · G15 · 7350 · 3460 · HP |
| "Where is the serial number?" | Views · HP → Labels | every model except the MacBook |
| "How much memory can it take?" | Specifications → Memory | every model except the MacBook |
| "Can I put a bigger SSD in it?" | Specifications → Storage | every model except the MacBook |

**Swollen batteries deserve their own note.** Every Dell service manual leads its Troubleshooting
chapter with handling instructions for swollen lithium-ion batteries, including *do not attempt to
repair* and *do not puncture*. A ticket describing a bulging case or a laptop that no longer sits flat
is a safety issue before it is a hardware issue, and the corpus says so.

**Diagnostic LED codes extract in two different shapes**, which matters to whoever writes the chunker.
The G15 5510 renders them as `2,3 No memory or RAM detected` on one line. The 5420 and 5521 render the
same table as split columns — a bare `2`, a bare `8`, then `LCD Power Rail Failure`. A chunker that
strips short numeric lines as page furniture deletes the second form entirely, and that is not a
hypothetical: it happened here, and `extract_text.py` carries a comment explaining why the
page-number rule was removed.

---

## Two hazards in the source material

**The Latitude 5550 spec sheet is a three-column comparison.** Dell publishes one PDF covering the
5350, 5450 and 5550. Extraction keeps the row labels and loses the column headers, so a `MEMORY
OPTIONS` chunk contains all three models' values back to back with nothing marking which is which —
the 13-inch 5350's soldered LPDDR5 sits directly above the 5550's upgradeable DDR5. A model-filtered
query for "how much memory can my 5550 take" retrieves a chunk that is technically about the right
document and possibly about the wrong machine.

This is the strongest argument in the corpus for Document Intelligence. Layout-aware extraction
recovers the column association that a text extractor drops, and the committed text gives a ground
truth to measure that against. Until then, the 5550 file should be treated as read-only evidence that
a specification exists, not as a quotable figure.

**"Latitude 5550" also matches the Latitude E5550**, a 2014 Broadwell machine. Same family name, ten
years apart. `device_model` filtering is what keeps them separate, which is why § 4.7 requires it.

---

## The Internet Archive route, and why it is legitimate

Five documents were pulled from the Wayback Machine rather than the vendor. Dell removed them from its
live site, and the alternative was leaving three models uncovered.

**This is Dell's own file, not a mirror's copy of it.** The method:

1. Ask the CDX index what Dell ever published under a path:
   `http://web.archive.org/cdx/search/cdx?url=dl.dell.com/topicspdf*&fl=original&collapse=urlkey&filter=original:.*5521.*`
2. Take a snapshot whose `statuscode` is `200` — a `301` row is a redirect to Dell's "not found" page
   and downloads as nothing.
3. Fetch the **`id_` raw form**: `https://web.archive.org/web/<timestamp>id_/<original-url>`. The
   `id_` suffix returns the archived bytes unmodified. Without it you get an archive-wrapped HTML
   page, which passes a naive existence check and extracts to nothing.
4. Verify it like any other document. The archived files go through the same `verify_text`,
   page-count and regulatory-model checks, and that is what makes the route acceptable — provenance is
   asserted by the file's own title page, not by where it was downloaded from.

Each archived document carries a `wayback` block in `sources.json` recording the snapshot timestamp
and the original vendor URL, because a document that exists only in an archive has different
durability from one the vendor still serves.

**Settled with evidence rather than assumption:** no Dell `topicspdf` PDF has *ever* existed for the
2024 Latitude 5550, the 2024 Latitude 7350 or the Precision 3460 — checked against 4,353 archived
`dl.dell.com/topicspdf` URLs. Those three come from `delltechnologies.com` asset PDFs instead.

**No third-party mirrors, and no crawler spoofing.** ManualsLib and similar carry some of these
manuals with unverifiable provenance and no guaranteed edition. Dell's and Apple's live portals are
JavaScript-rendered and bot-protected; they were not fetched by pretending to be a search engine. A
fluent answer with a citation that resolves, about the wrong machine, is the exact failure this
corpus exists to prevent.

---

## The MacBook Pro is the honest exception

Apple publishes no service manual PDF and its repair manual is HTML only. Its file carries the text of
both Info sheets — safety, battery and power-adapter handling, regulatory information — plus an index
of ten Apple support articles: symptom on the left, the canonical Apple URL on the right.

**That index is marked POINTERS, NOT QUOTATIONS in the file itself.** The authoritative text lives at
each URL. Rendering those articles and presenting a paraphrase as a vendor quote is precisely the
grounding failure § 4.7 exists to prevent, so the corpus routes rather than answers. Every URL was
opened and confirmed to return the article it claims; one candidate resolved to the generic Mac User
Guide landing page and was dropped.

`support.apple.com` is unreachable by `curl` from some networks, so these ten URLs are **not**
machine-checkable by `fetch_manuals.py`. If they need re-verifying, that is a person with a browser.

---

## What these documents cannot answer

This half matters as much as the first. § 4.7 requires a declared out-of-corpus list, and the manuals
draw the sharpest boundary in the whole corpus.

**Not here, and a query about any of it should refuse rather than improvise:**

VPN and network access · email and Outlook · **account lockouts and password resets** · software
installation and licensing · "my laptop is slow" · disk-space and storage-usage questions · printer
setup · anything about a SkillStorm application.

**The account lockout case is the dangerous one.** It sits one word away from questions these
documents *do* answer — a BIOS password is in the manual, an Entra ID password is not, and the two are
entirely different things resolved by entirely different procedures. Conflating them routes a user to
a hardware procedure for an identity problem. That belongs in the identity runbook, and § 7 should
carry a paired case proving the two do not bleed.

**And anything about a model not in the fleet.** A question about a Latitude 7420 must refuse rather
than answer from the 7350 — the near-miss boundary § 7 needs, enforceable only because `device_model`
is a required filter.

**Within the fleet, three more refusals are required**, and they are the ones most likely to be got
wrong because the model *is* in the corpus:

- **No troubleshooting procedure exists for the Latitude 5550.** Not in this corpus and not in any
  Dell PDF. "My 5550 won't turn on" must escalate, not borrow the 5521's flea-power procedure.
- **No BIOS setup content exists for the Latitude 5550 or the Precision 3460.**
- **No diagnostic LED code table exists for the 7350, the 3460 or the 5550.** The 7350 guidebook
  describes battery-charge LED behaviour only, which reads similar and answers a different question.

---

## Three documents that were not what they claimed

Kept here because each is a live example of the problem § 4.7 describes, and each was caught only by
opening the file.

**`latitude-14-5420-laptop` is the Latitude 5420 _Rugged_** — regulatory model P85G, a different
computer with a different chassis, different parts and a different disassembly order. 145 pages of
confident, entirely wrong procedure. The standard 5420 is P137G. **The model-name check does not catch
this**, because the Rugged manual also says "Latitude 5420"; only the regulatory model separates them,
which is why `fetch_manuals.py` verifies it. A guidebook covering two chassis prints both — the
Latitude 7350 title page reads `P179G/P178G` — so the check compares sets, not strings.

**`g-series-15-5510-laptop_reference-guide` is "Me and My Dell"** — a generic guide covering Inspiron,
G-Series, XPS and Alienware. It is genuinely useful and it is kept, but with **`device_model` set to
null**, and it is the one file in `text/` that no model-filtered query will ever return. Tagging it to
the G15 5510 would let a question about that specific machine be answered from content written for
four product families.

**`latitude-15-5521-laptop_reference-guide` is a Windows re-imaging guide**, not a reference guide. It
is useful — it gives the driver installation order after a clean image — but a filename taken from the
URL would have misdescribed it in every citation.

---

## One open scope question

**The Precision 3460 is a small-form-factor desktop**, not a laptop. There is no Precision 3460
laptop — the mobile Precisions in that range are the 3470, 3480 and 3490. Either § 4.4 widens to
desktops, or the fleet list meant one of those. The guidebook is indexed as a desktop until someone
says otherwise.

**A ready-made distractor, if § 7 wants one.** The 2015 Latitude 13 7350 has a downloadable Dell PDF
and the 2024 Latitude 7350 does not. Index the 2015 document under a `device_model` the fleet does not
contain and assert that a 7350 query never returns it. It must never be tagged as the fleet's 7350.
