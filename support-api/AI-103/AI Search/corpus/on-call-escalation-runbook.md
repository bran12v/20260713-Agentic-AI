# On-Call and Escalation Runbook

**Doc id:** ONC-RUN
**Doc type:** runbook
**Owner:** Service Operations
**Effective:** 2026-02-15

## 1. Rotas

Three rotas run in parallel, each in weekly shifts handed over at 09:00 UTC on
Monday.

- **Service on-call** — one engineer per owning team, first responder for that
  team's services.
- **Incident commander** — one per week across all teams, paged automatically on
  Severity 1 declaration.
- **Duty Change Authority** — one CAB member per week, authorises emergency
  changes under EXC-PROC section 2. Published alongside the other two.

An individual may hold at most one rota in a given week. The Duty Change Authority
is deliberately not the incident commander: the person authorising an emergency
change should not be the person running the incident that motivates it.

## 2. Paging

### 2.1 Who is paged, and when

| Trigger | Paged | Response time |
|---|---|---|
| Severity 1 declared | Incident commander + service on-call | 5 minutes |
| Severity 2 declared | Service on-call | 15 minutes |
| Severity 3 declared | Team queue, not a page | Next business day |
| Automated alert, service down | Service on-call | 15 minutes |
| Automated alert, degradation | Service on-call | 30 minutes |

### 2.2 Out of hours

Out of hours means outside 08:00–18:00 UTC on a working day. Severity 1 and
Severity 2 page out of hours. Severity 3 and Severity 4 never do — an engineer
woken for a Severity 3 has been paged in error, and the misrouting is reviewed.

### 2.3 If nobody answers

Paging escalates automatically on no acknowledgement:

1. Service on-call — page again after the response time above.
2. Team lead — immediately after the second unacknowledged page.
3. Engineering manager — 10 minutes later.
4. Sponsoring director — 15 minutes after that.

Escalation is automatic and requires no decision. An engineer who cannot take a
shift arranges cover in advance; there is no mechanism for declining a page.

## 3. Handover

Shift handover is a live conversation, not a written note. The outgoing engineer
covers open incidents, changes in flight, any standard-change suspension affecting
the team, and anything expected to page during the incoming shift.

An unhandover-ed shift is a control failure recorded against the outgoing
engineer's team.

## 4. What on-call may do without further approval

The service on-call engineer may, during an active incident:

- Initiate backout of any change under section 5 of RBK-STD.
- Restart, drain, or scale a service within its recorded capacity bounds.
- Request break-glass access from the Duty Change Authority under ACC-POL.

The on-call engineer may **not** self-authorise an emergency change. That
authorisation comes from the Duty Change Authority, and the separation is the
point of running the third rota.

## 5. Records

Page records, acknowledgements, and escalations are retained with the incident
record under RET-SCH, on the incident's retention period rather than a separate
one.
