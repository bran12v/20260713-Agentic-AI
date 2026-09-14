# Design Rationale

Why the architecture is shaped the way it is. **[project3-requirements.md](project3-requirements.md)
§ 3.3 states the rules; this file argues them.** Read it once at the start. You do not need it open
while you build, and nothing in it is a requirement.

It exists because the rules in § 3.3 look arbitrary until you know what each one is defending
against, and a team that does not know will relax one of them under schedule pressure on day 6.

---

## Why the sub-request is the unit of work

One email can hold several unrelated asks — a lockout, an access question and a full laptop. Treating
the ticket as the unit forces all three through one state, so the whole ticket waits on the slowest
lane and an approval on one blocks a reply on another.

Cutting them apart at the Coordinator means each carries its own policy gate, grounding review,
approval record, re-validation and terminal state. One lane can be finished while a second waits on an
approver. There is no single point where the ticket "is", and the ticket update at the end is a
summary of N independent outcomes rather than one verdict.

This is also what makes the graph divisible across sixteen people: the lane is the seam.

## Why investigation, not classification

A HelpDesk ticket is a symptom, not an instruction. "Jane can't log in" does not say whether her
account is locked, her password expired, her MFA registration is broken, her account was disabled by an
offboarding job, or a license lapsed — and the correct response to the last of those is not an unlock.

So a worker is given a goal and read-only tools, not a label set. The number of tool calls varies by
sub-request, and two tickets of different shape must produce visibly different run records. A fixed
one-call-each shape is a classifier wearing an agent's clothes, and it does not meet the requirement.

## Why the width is the model's and the routing is not

The Coordinator emits a typed plan naming the workers it wants and why. A selection function then
routes deterministically on that object.

The split matters in both directions. Planning has to be the model's, because deciding how many
distinct requests an arbitrary email contains is not expressible as a rule. Routing has to be code,
because a mis-route is invisible at runtime and a pure function over a typed plan can be unit tested
with no model in the loop — which is the single cheapest test in the project.

## Why the join is hand-written, and why it sits after execution

`WorkflowBuilder`'s fan-out targets are a static list declared at build time; what varies at runtime is
which subset the selection function activates. Fan-in likewise declares a static source list and fires
when all *declared* sources deliver.

So the accurate problem is not "a fan-out the framework did not size" — the framework sizes it at
three. It is that **a fan-in declared over three sources blocks forever when the selection function
activated one.** That is why the join is yours: the Coordinator records what it ordered into workflow
state and the join counts arrivals against that list.

It sits *after* execution and only assembles the ticket update. A join placed before approval would
make every lane wait on the slowest approver and collapse the design back into a chain.

## Why approval is gated on reversibility

Three operations change whether a person can work, and those three are what the flow covers.

Deletion is irreversible. Deactivation and reactivation are the pair an attacker would aim at, because
one locks an employee out and the other restores an account that was closed on purpose. The remaining
operations are recoverable, immediately visible to the affected user, and slow the desk to a crawl if
each one waits on a human — which is the failure mode that gets an automation switched off.

Gating on "risk" in the abstract produces an argument every sprint. Gating on reversibility produces a
list.

## Why approval is permission, not an instruction

Approval arrives minutes or hours later. In that gap the account can be deleted by someone else, the
license can lapse, the user can fix it themselves, or a second ticket can already have acted.

So on re-entry the **owning worker** — not a generic resumption step — re-validates its approved action
against live state. It has the tools and the context to know what "still holds" means for the action it
proposed; a generic step would have to re-derive both.

Only the gated set carries this risk, because only the gated set has a gap between decision and
execution.

## Why the approval record binds the action type, not just the subject

Re-validation may narrow an action. Without a binding on action type, `deactivate(jane)` approved and
narrowed to `revoke_sessions(jane)` passes a subject check and executes something the approver never
saw. The approval record therefore names `(decision_id, subject, action_type)`, and narrowing may
withdraw but never substitute.

This is the kind of hole that only appears when someone implements "matching approval record" the
obvious way.

## Why identity is resolved server-side

The entitlement-scoped reads sit behind an MCP server that takes the subject from authenticated caller
context rather than from a tool argument.

This is the only place § 4.3's per-call entitlement check and § 5's "no tool takes its subject from
model output" can actually be enforced. An in-process tool can always be handed whatever the model
produced — the check becomes a convention, and conventions are what prompt injection is for. Putting a
process boundary there makes the guarantee structural.

Retrieval tools stay in-process by the same logic inverted: runbooks and manuals are not
entitlement-scoped, so a server in front of them adds a hop without adding a control.

---

## Why none of the five named orchestrations

Each builder answers one question. None of them asks the question this system asks.

| Builder | Question it answers | Why not here |
|---|---|---|
| **Sequential** | What are the steps? | The steps are not known before the ticket is read. One lockout resolves in a single Graph lookup; another needs sign-in logs, group membership, license state and a runbook before it is even clear an action is warranted. *The inside of a lane — gate, reviewer, approval, re-validate, execute — is a fixed sequence, and is built as one.* |
| **Concurrent** | Who all looks at this? | Every participant sees the same input and converges on one fan-in. Here each worker sees a *different* sub-request, and the lanes never converge on a decision — only on a ticket update. |
| **GroupChat** | Who speaks next? | Nothing here is settled by discussion. The disputed questions are entitlement and policy, and both must be decided by code an auditor can read. |
| **Handoff** | Who owns this? | Ownership transfers to one owner at a time. Here several workers own several different things at once. |
| **Magentic** | What is the plan, and what is the new plan? | Magentic plans, dispatches, critiques and replans toward **one** goal. Here the lanes are independent from the moment they are cut, each with its own approver and its own terminal state, and the Coordinator never reasons across them. |

**The Handoff row deserves a caveat.** One sub-request is a valid outcome, and for a single-lane ticket
this system *is* one owner at a time — which is the canonical handoff shape. The whole justification
for the custom graph rests on N>1 being common enough to matter. If it turns out that nearly every real
ticket is one lane, the honest conclusion is that the fan-out was over-built, and the architecture
document should say so rather than defend it.

**The Magentic row deserves the opposite caveat.** Re-planning inside a lane — after a gate rejection,
a withdrawn action or a partial failure — is required, and it is not Magentic. The line is cross-lane
reasoning. § 3.4's guard rail states the falsifiable version: if the Coordinator ever revises one lane
because of another lane's result, switch to `MagenticBuilder` rather than rebuilding it by hand.
