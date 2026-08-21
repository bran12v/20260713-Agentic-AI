# Incident Severity Matrix

**Doc id:** SEV-MTX
**Doc type:** matrix
**Owner:** Service Operations
**Effective:** 2026-02-15

## 1. How severity is assigned

Severity is assigned by the incident commander at declaration and reassessed at
every status update. Severity is a function of client impact, not of engineering
effort: a difficult repair with no client impact is not a Severity 1.

Where two levels could apply, the higher applies. Severity may be lowered during
an incident only by the incident commander, and the reason is recorded.

## 2. The four levels

### Severity 1

Complete loss of a client-facing service, or confirmed unauthorised access to
client data. Any number of clients affected.

- **Declaration:** immediate, by any engineer, without waiting for confirmation.
- **Commander:** on-call incident commander, paged automatically.
- **Client communication:** initial notice within 30 minutes of declaration, then
  **every 60 minutes** until service is restored.
- **Internal status update:** every 30 minutes.

### Severity 2

Substantial degradation of a client-facing service, or complete loss of a
non-client-facing service on which a client-facing service depends. Workaround may
exist but is not acceptable as a steady state.

- **Declaration:** by any engineer.
- **Commander:** on-call engineer for the owning team.
- **Client communication:** initial notice within 2 hours, then **every 24 hours**
  until resolution.
- **Internal status update:** every 4 hours.

### Severity 3

Degradation with an acceptable workaround, or loss of a non-client-facing service
with no client-facing dependency.

- **Declaration:** by the owning team.
- **Client communication:** on resolution only, unless a client has raised it.
- **Internal status update:** daily.

### Severity 4

Cosmetic defect, or a fault with no service impact.

- **Declaration:** through the normal defect queue.
- **Client communication:** none required.

## 3. Severity and change classification

Severity 1 and Severity 2 are the only levels that justify an emergency change
under section 3.1 of EXC-PROC. A Severity 3 incident does not, however
inconvenient the workaround. This is the most common misuse of the emergency route
and it is checked at retrospective review.

Declaring a higher severity to obtain an emergency change is a control failure and
is recorded against the declaring engineer's team.

## 4. Escalation

Escalation paths, paging targets, and the out-of-hours rota are in the On-Call and
Escalation Runbook (ONC-RUN). This matrix defines *what* a severity is; the
runbook defines *who* is woken and in what order.

## 5. Post-incident review

Every Severity 1 and Severity 2 incident carries a post-incident review. The
review is a separate obligation from the retrospective review of any emergency
change made during the incident, and the two are not satisfied by a single
document — the change review examines the change, the incident review examines the
failure.

Post-incident review records are retained under RET-SCH.
