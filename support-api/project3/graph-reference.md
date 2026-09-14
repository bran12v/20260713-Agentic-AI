# Graph Reference

Node by node, for someone building one. **[project3-requirements.md](project3-requirements.md) § 3.1
is the shape**; this is what happens inside each box. Read the section you are building, not the whole
file.

The rules this implements are § 3.3 of the brief; why they are those rules is in
[design-rationale.md](design-rationale.md).

---

## The three workers are not interchangeable

They share a loop — read-only tools, own agent thread, bounded iterations — and they differ in what
they can produce, which changes the shape of the lane underneath them.

| Worker | Produces | Reaches the policy gate? |
|---|---|---|
| **Identity** | Almost always an action set — unlock, reset MFA, revoke sessions, deactivate, delete | Yes |
| **Access** | Usually an answer about what someone has and whether they should. Sometimes a group-membership or license action | Only when it proposes actions |
| **Device** | An answer, always. **It mutates nothing, ever** | **Never** |

Drawing all three identically is wrong for two of them. A Device lane that passes through a policy
gate is a lane with a gate that can only ever say "nothing to gate".

## A lane has two output paths

```
  OWNING WORKER   loops on its own read-only tools · own agent thread · bounded
     │
     ├── needs to ask the requester something
     │        └─▶ interrupt + checkpoint · see "What a pause does" below
     │
     ├── produces an ANSWER
     │        └─▶ GROUNDING REVIEW ─▶ reply on the ticket ─▶ lane done: answered
     │
     └── proposes an ACTION SET
              └─▶ POLICY GATE ─▶ GROUNDING REVIEW ─▶ sort each action
                                                       ├─ ungated → execute now
                                                       └─ gated   → hold for the
                                                                    ticket's one
                                                                    approval
```

**Grounding review is on both paths.** An answer emailed to a requester and a justification shown to
an approver are both grounded claims, and both are fluent when wrong. The Device lane is the one most
exposed to this — a procedure from the wrong laptop's manual reads perfectly and cites a real page.

**The policy gate is on the action path only.** It is deterministic code: it checks the requester's
entitlement over the target, decides from the closed action enum whether each action falls in the
gated set, and enforces the verification steps the retrieved runbook requires.

**A lane holding a gated action has finished planning, not finished.** Its ungated actions have run;
its gated ones wait for § "After the join" below. It still counts as arrived for the join.

## The three bounded cycles

Each re-enters **that lane's own worker**, never another's, and each carries an independent hard cap
(§ 5) on top of its structured termination condition.

| # | Trigger | What the worker gets back |
|---|---|---|
| 1 | The policy gate rejects an action | A structured objection — which action, which rule |
| 2 | The grounding reviewer rejects | Which claim was unsupported, and by which chunk |
| 3 | An ungated action partially fails | The results so far, to continue, substitute or escalate |

**Re-validation is not a cycle.** It happens after the join, when the lane is already finished, and it
is deterministic: re-run the tool calls recorded in the action's `preconditions` and compare against
the values recorded there. It needs no worker and re-enters nothing.

## What a pause does to the rest of the graph

This is the most-asked question about the design, so it is worth being exact.

A lane pauses for one of two reasons — it needs information from the requester, or it needs an
approval. Both use the framework's human-in-the-loop primitive, and both **interrupt the run and
checkpoint it**.

**The run does not halt the instant a worker asks.** It keeps processing everything still runnable.
So when lane 2 asks a question thirty seconds in, lanes 1 and 3 carry on and **run to completion**.
Only when nothing else can progress does the run checkpoint and idle.

When the answer arrives — a requester's reply, or an approval decision — the run rehydrates from that
checkpoint and **the asking worker resumes with its own tool history intact**. It continues down the
path it was on; it does not start again and it does not replay work already done.

**The other lanes are not resumed, because they never stopped.** They finished before the run idled.
What the checkpoint preserves is their *results*, which is what the join needs.

Two consequences:

- **Resume is single-writer.** The callback can land on any replica. Two replicas rehydrating one
  checkpoint would fork the run and let both copies write the ticket. Take a row lock on the ticket
  before rehydrating and hold it until the run idles again.
- **A question that is never answered would hang the ticket**, and under a single per-ticket approval
  it would hang the approval too — a gated action in one lane waiting on an unanswered question in
  another. So **a question carries a deadline and escalates on expiry**, exactly as an approval does.
  The lane reaches `escalated`, the join completes, and the approval is raised for whatever else is
  pending.

## After the join

```
  JOIN — counts lane arrivals against the Coordinator's ordered SubRequest list
     │
     ▼
  Any gated actions anywhere on this ticket?
     │
     ├── no  ─▶ ticket update · close
     │
     └── yes ─▶ ONE approval card, listing every gated action
                  │
                  ├── rejected ─▶ escalate the whole set
                  │
                  └── approved ─▶ re-validate each action
                                    ├─ a precondition moved → withdraw, escalate
                                    └─ still holds          → execute
```

**One card per ticket, not per action.** An approver looking at one card sees everything the system
wants to do; fragmented cards are how someone approves "deactivate Bob" without seeing it is half of
an offboarding that also deletes an account.

**The card is all-or-nothing.** Power Automate offers Approve and Reject, so an approver who wants to
permit one action and refuse another rejects with a comment and the set escalates to a human. That is
a real limitation of the platform and not a design choice.

**Rejection does not re-plan.** A human looked at the proposal and said no, so a human takes it from
there. The comment is the handover, which is why § 6.3 refuses a rejection that carries none.

## Where the ticket ends up

A lane ends in exactly one of `executed`, `answered`, `declined` or `escalated`. The ticket then:

| Ticket outcome | Stage |
|---|---|
| Any lane escalated | Stays open in New, owner set, evidence in an internal note |
| Every lane declined | Unresolvable `954498199` |
| Anything else | Resolved `954564780` |

In-flight state lives on the run record, not on the ticket. HubSpot shows an open ticket and nothing
more while a run is in progress, which is why the internal note is the only window a human has into
one.
