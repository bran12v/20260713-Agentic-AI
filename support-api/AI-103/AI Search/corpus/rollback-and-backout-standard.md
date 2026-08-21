# Rollback and Backout Standard

**Doc id:** RBK-STD
**Doc type:** standard
**Owner:** Delivery Engineering Council
**Effective:** 2026-03-01

## 1. Requirement

Every production change carries a documented and verified backout path before
approval is sought. This applies to standard, normal, and emergency changes alike.
For emergency changes the verification may be performed concurrently with
implementation, but it is performed, and its absence is a finding at retrospective
review.

A change without a verified backout path is not approvable under section 6 of
CHG-STD, and the CAB rejects it at intake rather than deferring it.

## 2. What "verified" means

A backout path is verified when it has been executed end to end against an
environment that matches production in schema and configuration, and the resulting
state has been confirmed equivalent to the pre-change state.

Three things do not constitute verification:

- A written description of what would be done.
- A previous execution of a similar backout for a different change.
- Confidence that the deployment tool supports rollback.

The distinction matters because the most common backout failure is not that the
path was wrong but that it was never run.

## 3. Time bound

The backout path must complete within 30 minutes of the decision to back out. A
path that cannot meet this bound is not acceptable, and the change must be
restructured — typically by decomposing it into smaller changes each with its own
path.

The 30-minute bound is measured from decision, not from the start of execution.
Time spent locating a runbook counts against it.

## 4. Irreversible changes

Some changes cannot be backed out — a destructive schema migration, a data
deletion, an external notification already sent. These are handled by forward
recovery rather than backout, and the standard's requirement is met by a
documented and verified *forward recovery* path meeting the same 30-minute bound.

An irreversible change is flagged as such at submission. The CAB reviews
irreversible changes as a distinct category and may require a staged approach,
additional approval, or a rehearsal.

## 5. The decision to back out

The implementing engineer may initiate backout at any point without further
approval. Backout is never blocked pending a decision from the CAB, the Duty
Change Authority, or a service owner.

This is deliberate. Requiring approval to back out converts a recoverable
situation into an incident while the approval is sought.

## 6. Recording

A backout is recorded on the original change record, with the trigger, the time
from decision to completion, and the confirmed post-backout state. A change that
was backed out is closed as backed out, not as implemented, and its retention
period runs from that closure under RET-SCH.

Where a change is backed out and later resubmitted, it is a new change with a new
record. The original record is not reopened.
