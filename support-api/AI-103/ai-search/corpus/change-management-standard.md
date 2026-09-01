# Production Change Management Standard

**Doc id:** CHG-STD
**Doc type:** standard
**Owner:** Delivery Engineering Council
**Effective:** 2026-03-01
**Supersedes:** CHG-STD rev 3 (2025-06-14)

## 1. Purpose and scope

This standard governs every change to a production system operated by Delivery
Engineering, including application deployments, infrastructure modifications,
database schema changes, configuration edits, and certificate operations.

It applies to all engineers, contractors, and vendor personnel with the ability to
alter a production system, regardless of employment arrangement.

## 2. Definitions

- **Production system** — any system serving external clients or holding client
  data, including pre-production environments that hold copies of client data.
- **Change** — any modification to the configuration, code, schema, or
  infrastructure of a production system.
- **CAB** — the Change Advisory Board, convened twice weekly, quorum of three.
- **Standard change** — a change type pre-authorised by the CAB and enumerated in
  the Standard Change Catalog. See section 4.1.
- **Emergency change** — a change required to restore service or to close an
  actively exploited security exposure. See section 4.2.

## 3. Change classification

Every change is classified before submission. The classification determines the
approval route and cannot be altered after the change is submitted.

| Class | Definition | Approval route |
|---|---|---|
| Standard | Listed in the Standard Change Catalog | Pre-authorised; no CAB review |
| Normal | Any change not standard and not emergency | Full CAB review |
| Emergency | Restores service or closes an active exposure | Exception procedure |

Misclassification is itself a control failure. A change submitted as standard that
does not appear in the catalog is rejected at intake and must be resubmitted as a
normal change.

## 4. Approval

### 4.1 The general rule and its exception

**Every production change requires CAB approval before implementation, except for
standard changes enumerated in the Standard Change Catalog (CHG-CAT).**

Standard changes carry pre-authorisation because the CAB has already reviewed the
change type, its blast radius, and its backout path. Pre-authorisation attaches to
the *change type as described in the catalog entry*, not to the person performing
it and not to a superficially similar change. Where a proposed change resembles a
catalog entry but differs in scope, target, or backout path, it is a normal change
and requires CAB approval.

The catalog is the sole authority on which change types are standard. This
standard does not restate the catalog contents, and an engineer must consult
CHG-CAT to determine whether a specific change is pre-authorised.

### 4.2 Emergency changes

An emergency change may proceed before approval. Authorisation is granted by the
Duty Change Authority under the Exception Request Procedure (EXC-PROC), section 3,
which also sets the retrospective review deadline.

An emergency change that has not completed retrospective review by its deadline is
recorded as a control failure against the implementing team, and the team's
standard-change pre-authorisation is suspended until the review closes.

### 4.3 Approval is not delegable

CAB approval is granted by the board, not by an individual member. A member cannot
approve a change outside a convened session, and no member may approve a change
they authored.

## 5. Implementation windows

Changes are implemented only inside an approved implementation window. Windows are
constrained by the release freeze calendar (FRZ-CAL); a change approved by the CAB
still may not proceed during a declared freeze without a freeze exception.

## 6. Backout

Every change carries a documented backout path before approval is sought. The
requirements for that path, including verification and time bounds, are set by the
Rollback and Backout Standard (RBK-STD). A change whose backout path has not been
verified is not approvable, irrespective of classification.

## 7. Records

Change records are retained under the Records Retention Schedule (RET-SCH). The
retention period runs from change closure, not from change submission.
