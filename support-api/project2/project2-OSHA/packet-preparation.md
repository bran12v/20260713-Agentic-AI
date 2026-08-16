# Preparing the incident packets

The regulatory corpus ships with the project. The incident packets do not — you build them, and they are the input your system reads. Four packets, in `packets/`, outside `corpus/`.

Build these first. Everything downstream — extraction confidence, the readiness gate, which workers the Coordinator dispatches, whether the Reviewer rejects — is determined by what is in these folders. A packet built carelessly produces a system that appears to work and cannot be demonstrated.

---

## What a packet is

A folder of artifacts representing one submitted incident, exactly as an analyst would hand it over.

```
packets/
├── inc-0411/
│   ├── osha-301.pdf          the completed Form 301
│   ├── photo-01.jpg          scene evidence
│   └── supervisor-note.txt   supporting narrative
├── inc-0412/
├── inc-0413/
└── inc-0414/
```

The blank Form 301 is page 7 of `corpus/pdf/FORM-301.pdf`, or download the fillable package from https://www.osha.gov/recordkeeping/forms.

Form 301 gives you these fields, and the four packets differ almost entirely in how they are filled:

| Field | Why it matters |
|---|---|
| Case number, date of injury, time of event | Drives R4 day counting and the 180-day cap |
| Time employee began work | Distinguishes work-relatedness edge cases |
| What the employee was doing just before / what happened | The narrative the photo either corroborates or contradicts |
| What was the injury or illness | R1 recordability |
| Treatment given, and whether treated in an emergency room | R3 against the closed first-aid list |
| **Was employee hospitalized overnight as an in-patient?** | R2, and the single most important checkbox in the whole exercise |
| Date of death, if any | R2's 8-hour clock |

> **The in-patient checkbox is the trap the system exists to catch.** Form 301 asks whether the employee was "hospitalized overnight as an in-patient". §1904.39(b)(10) says an admission for **observation or diagnostic testing only** is not an in-patient hospitalization. An employee held overnight for observation produces a checked box and a *non-reportable* outcome. Packet P4 is built on exactly this gap.

---

## The four packets

### P1 — `inc-0411` — happy path

Every field complete and legible. No hospitalization, nothing electrical.

| Field | Value |
|---|---|
| Injury | Laceration to the left forearm, tool-related |
| Treatment | Sutures, treated in emergency room, released same day |
| Hospitalized overnight as in-patient | No |
| Days away from work | 0 |
| Job transfer or restriction | None |
| Equipment involved | Hand tool, not energized |

**Expected outcome.** Sutures are not on the §1904.7(b)(5)(ii) first-aid list, so this is medical treatment beyond first aid and the case is recordable, Column J. No hospitalization means no reportability leg. Nothing for `CFR-269` to ground, so no hazard-control leg. **Recordability worker only.**

Type this one or fill it neatly. It exists to prove the clean path works end to end.

### P2 — `inc-0412` — in-patient admission, energized equipment

| Field | Value |
|---|---|
| Injury | Second-degree burns to both hands and forearms, arc flash |
| What happened | Employee was racking a 12.47 kV breaker into an energized switchgear cubicle |
| Treatment | Emergency room, then **formally admitted as an in-patient for treatment**, three days |
| Hospitalized overnight as in-patient | Yes — admitted for care and treatment |
| Days away from work | Set the return-to-work date so the running count sits near, but not over, 180 calendar days |
| Equipment involved | Energized switchgear |

**Expected outcome.** Recordable, Column H, with the day count approaching the 180-day cap. Reportable — a formal in-patient admission for care or treatment fires the 24-hour clock under §1904.39. Energized equipment means `CFR-269` can ground a control, so the hazard-control leg is dispatchable. **All three workers, with the recordability and reportability legs running concurrently.**

This is the packet that proves the plan varies and that concurrent legs actually run concurrently.

### P3 — `inc-0413` — illegible date of injury

**This packet must be printed, filled in by hand, and scanned.** No exceptions, and it cannot be the only handwritten one you attempt — leave time to redo it.

Typed PDF text returns roughly uniform 0.99 confidence from Document Intelligence and will never fall below the 0.60 floor. If every packet is typed, R5 never fires, the readiness gate never triggers, and a fifth of your acceptance criteria becomes undemonstrable.

Fill the date-of-injury field so it is genuinely ambiguous to a reader: overwrite a digit, let ink bleed, or write the day and month so they could be read two ways. Everything else on the form should be legible — you want *one* field below the floor, not a form that fails wholesale.

**Expected outcome.** Date of injury extracts below 0.60. The readiness gate routes to human determination **before any worker is dispatched**. The dossier names the field that failed and asks the analyst for it. **No workers run at all.**

Check your scan before relying on it: crack it with Document Intelligence and confirm the date field's confidence is actually under 0.60 and the neighbouring fields are over it. Adjust and re-scan until it is.

### P4 — `inc-0414` — observation-only overnight stay

The packet the whole architecture is built to get right.

| Field | Value |
|---|---|
| Injury | Chest pain and dizziness after exertion in a hot substation yard |
| Treatment | Emergency room, **held overnight for observation and diagnostic testing, discharged the following morning with no admission for care or treatment** |
| Hospitalized overnight as in-patient | Yes — and the narrative must make clear it was observation only |
| Days away from work | 1 |

Word the narrative so both readings are available. A worker that stops at the §1904.39 24-hour clock will call this a reportable in-patient hospitalization. The exclusion at §1904.39(b)(10) says otherwise.

**P4 also carries two extra artifacts:**

1. **A malformed artifact.** Add a file that cannot be cracked — a `.pdf` extension on a text file, a zero-byte image, or a truncated JPEG. The ingestion pipeline must skip and log it, not die, and the dossier must state what failed.
2. **A photograph that contradicts the narrative.** The narrative describes exertion in the heat; the photograph shows something inconsistent with it, so the multimodal corroboration check returns a non-corroborating verdict and the escalation trigger fires.

**Expected outcome.** Recordable. **Not** reportable — the reportability leg must find the exclusion, not just the clock. This is the packet required to produce a Reviewer rejection and a narrowed re-dispatch: the first pass asserts a reportable hospitalization citing the 24-hour clock, the Reviewer rejects the claim as unsupported by the chunk it cited, and the Coordinator re-dispatches with a narrowed goal that surfaces §1904.39(b)(10). **Recordability and reportability, with at least two reportability iterations.**

---

## Photographs

Every packet needs at least one photograph. P4 needs one that contradicts its narrative.

**Constraints, without exception:**

- **No people, no faces, no body parts.**
- No licence plates, no street addresses, no signage identifying a real company or site.
- No identifiable premises — nothing a viewer could geolocate.

**Where to get them.** Federal image libraries are public domain and are the intended source:

| Source | URL |
|---|---|
| NIOSH image gallery and Science Blog | https://www.cdc.gov/niosh/ |
| CDC Public Health Image Library | https://phil.cdc.gov/ |
| Department of Energy | https://www.energy.gov/photos |
| OSHA newsroom and publications imagery | https://www.osha.gov/ |

Photographing your own subjects is fine and often faster — a scuffed hand tool on a bench, a length of cable, a scorched panel cover, an empty equipment yard. Just observe the constraints above.

Record where each photograph came from in a `packets/SOURCES.md` file, so provenance is answerable during the demo.

---

## The injection fixture does not live here

The prompt-injection test — a poisoned artifact designed to make an agent skip the readiness gate or assert a classification — belongs in **test fixtures**, not in `packets/` and not in `corpus/`.

If it sits in `packets/`, an ordinary `submit` run ingests it, and the adversarial case stops being adversarial: you can no longer demonstrate a clean run and an attacked run as separate things.

---

## Before you move on

- [ ] Four packet folders exist under `packets/`, outside `corpus/`
- [ ] All four use the real OSHA Form 301
- [ ] At least one form is handwritten and scanned, and its date-of-injury field cracks below 0.60 — confirmed by actually running it through Document Intelligence
- [ ] P2's day count sits near but under 180 calendar days
- [ ] P4's narrative supports both the naive reading and the correct one
- [ ] P4 contains a malformed artifact and a non-corroborating photograph
- [ ] No photograph contains a person, plate, address, or identifiable premises
- [ ] `packets/SOURCES.md` records where every photograph came from
- [ ] The injection fixture is in test fixtures, not in `packets/`
