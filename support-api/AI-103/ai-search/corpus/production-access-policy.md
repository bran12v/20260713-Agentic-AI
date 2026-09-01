# Production Access Policy

**Doc id:** ACC-POL
**Doc type:** policy
**Owner:** Information Security
**Effective:** 2026-01-10

## 1. Principle

Access to production is granted on the narrowest scope that permits the work, for
the shortest period that permits the work, and only to an identity that can be
attributed to a named individual. Shared accounts are prohibited without
exception.

## 2. Access tiers

| Tier | Grants | Duration | Approval |
|---|---|---|---|
| Read | Logs, metrics, traces; no client data | Standing | Line manager |
| Operate | Restart, scale, drain; no data reads | Standing | Line manager + service owner |
| Elevated | Client data reads, schema operations | Time-boxed, 4 hours | Service owner + Information Security |
| Break-glass | Full administrative control | Time-boxed, 2 hours | Duty Change Authority, during a declared incident only |

Approval at every tier is recorded against the named individual. Approval of an
access request is a distinct decision from approval of a change: holding Elevated
access does not authorise a change, and CAB approval of a change does not grant
the access needed to implement it. Engineers routinely conflate the two and are
blocked at implementation.

## 3. Contractors and vendor personnel

Contractors and vendor personnel may hold Read and Operate access on the same
terms as employees, subject to a current background check and a signed
confidentiality undertaking.

Elevated access requires, in addition, the sponsoring director's approval and a
named employee supervisor for the duration of the grant. Break-glass access is not
available to contractors or vendor personnel under any circumstance; where
break-glass is required during an incident, an employee performs the action.

Vendor personnel are additionally subject to the vendor security review (VND-SOP)
before any access is granted, and access lapses automatically when the vendor's
review expires.

## 4. Time-boxed grants

Elevated and break-glass grants expire automatically at the end of their window.
There is no renewal in place; a further period requires a fresh request and fresh
approval. An engineer who anticipates needing four hours requests four hours — a
grant cannot be extended once running.

Sessions are terminated at expiry, including in-flight work. This is deliberate:
work that cannot survive a session termination has no verified backout path and
should not be running against production.

## 5. Review and revocation

Standing access is reviewed quarterly by the service owner. Access is revoked
within one business day of a change of role and immediately on termination.

Access held by an engineer whose team is under standard-change suspension is not
itself affected — suspension changes the approval route for changes, not the
access tiers of individuals.

## 6. Logging

Every production session is logged with the individual identity, the tier, the
approving parties, and the commands issued at Elevated and break-glass tiers.
Access logs are retained under RET-SCH and are read-only to their subjects.
