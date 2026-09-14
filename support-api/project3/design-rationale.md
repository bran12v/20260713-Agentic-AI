# Design Rationale

Why the architecture is shaped the way it is. **[project3-requirements.md](project3-requirements.md)
§ 3.3 states seventeen rules; this file argues each of them.** Every section names the rule it
defends. Read it once at the start — you do not need it open while you build, and nothing in it is a
requirement.

It exists because the rules in § 3.3 look arbitrary until you know what each one is defending
against, and a team that does not know will relax one of them under schedule pressure on day 6.

---

## Why the sub-request is the unit of work

> **Defends Rule 1.**

One email can hold several unrelated asks — a lockout, an access question and a full laptop. Treating
the ticket as the unit forces all three through one state, so the whole ticket waits on the slowest
lane and an approval on one blocks a reply on another.

Cutting them apart at the Coordinator means each carries its own policy gate, grounding review,
approval record, re-validation and terminal state. One lane can be finished while a second waits on an
approver. There is no single point where the ticket "is", and the ticket update at the end is a
summary of N independent outcomes rather than one verdict.

This is also what makes the graph divisible across sixteen people: the lane is the seam.

## Why investigation, not classification

> **Defends Rule 2.**

A HelpDesk ticket is a symptom, not an instruction. "Jane can't log in" does not say whether her
account is locked, her password expired, her MFA registration is broken, her account was disabled by an
offboarding job, or a license lapsed — and the correct response to the last of those is not an unlock.

So a worker is given a goal and read-only tools, not a label set. The number of tool calls varies by
sub-request, and two tickets of different shape must produce visibly different run records. A fixed
one-call-each shape is a classifier wearing an agent's clothes, and it does not meet the requirement.

## Why the width is the model's and the routing is not

> **Defends Rule 3.**

The Coordinator emits a typed plan naming the workers it wants and why. A selection function then
routes deterministically on that object.

The split matters in both directions. Planning has to be the model's, because deciding how many
distinct requests an arbitrary email contains is not expressible as a rule. Routing has to be code,
because a mis-route is invisible at runtime and a pure function over a typed plan can be unit tested
with no model in the loop — which is the single cheapest test in the project.

## Why the join is hand-written, and why it sits after execution

> **Defends Rules 4 and 5.**

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

> **Defends Rule 7.**

Three operations change whether a person can work, and those three are what the flow covers.

Deletion is irreversible. Deactivation and reactivation are the pair an attacker would aim at, because
one locks an employee out and the other restores an account that was closed on purpose. The remaining
operations are recoverable, immediately visible to the affected user, and slow the desk to a crawl if
each one waits on a human — which is the failure mode that gets an automation switched off.

Gating on "risk" in the abstract produces an argument every sprint. Gating on reversibility produces a
list.

## Why approval is permission, not an instruction

> **Defends Rule 10.**

Approval arrives minutes or hours later. In that gap the account can be deleted by someone else, the
license can lapse, the user can fix it themselves, or a second ticket can already have acted.

So on re-entry the **owning worker** — not a generic resumption step — re-validates its approved action
against live state. It has the tools and the context to know what "still holds" means for the action it
proposed; a generic step would have to re-derive both.

Only the gated set carries this risk, because only the gated set has a gap between decision and
execution.

## Why the approval record binds the action type, not just the subject

> **Defends Rule 10, and § 5 of the brief.**

Re-validation may narrow an action. Without a binding on action type, `deactivate(jane)` approved and
narrowed to `revoke_sessions(jane)` passes a subject check and executes something the approver never
saw. The approval record therefore names `(decision_id, subject, action_type)`, and narrowing may
withdraw but never substitute.

This is the kind of hole that only appears when someone implements "matching approval record" the
obvious way.

## Why identity is resolved server-side

> **Defends Rule 13.**

The entitlement-scoped reads sit behind an MCP server that takes the subject from authenticated caller
context rather than from a tool argument.

This is the only place § 4.3's per-call entitlement check and § 5's "no tool takes its subject from
model output" can actually be enforced. An in-process tool can always be handed whatever the model
produced — the check becomes a convention, and conventions are what prompt injection is for. Putting a
process boundary there makes the guarantee structural.

Retrieval tools stay in-process by the same logic inverted: runbooks and manuals are not
entitlement-scoped, so a server in front of them adds a hop without adding a control.

## Why the model never reaches an executor

> **Defends Rule 6.**

The model decides *what* should happen; the graph routes it; code does it. Every action is a member of
a closed enum, and every executor is a typed function the model cannot call.

The reason is not that the model would compose a malicious call. It is that a system where the model
can reach a directory has no reviewable boundary: you cannot point at a line and say "nothing past
here is model output". With a closed enum you can, and the § 7 gated-set test is writable because the
set is enumerable.

## Why gating is per action and not per lane

> **Defends Rule 8.** This is the one most likely to be simplified away on day 6.

A lane proposes an action *set*, and a set can hold both kinds: "unlock Jane and revoke her sessions"
is ungated; "and deactivate the contractor account she's been using" is not. § 4.2 requires the
ungated members to run while the gated ones wait.

Gate the lane instead of the action and you get one of two wrong behaviours: either the whole lane
waits on an approver who is only needed for one of its actions, which is the delay that gets
automation switched off, or the whole lane executes on one approval, which is the approver agreeing to
something they were never shown.

The cost is a second fan-out inside the lane, and it is real work. It is also why the lane's terminal
state is not reached until every action it proposed has one.

## Why a pause is a checkpoint and not a new run

> **Defends Rule 9.** The other one most likely to be simplified away.

When a lane needs an approval or needs information from the requester, the run interrupts and
checkpoints, and the same run resumes when the answer arrives.

The tempting shortcut is to treat the answer as a fresh trigger: take the callback, look up the
record, start a new run seeded with what you know. It works for the simple case and then fails on
everything the project is actually about — the worker's own investigation context is gone, so
re-validation has to re-derive what "still holds" means; the other lanes on the ticket belong to a run
that is still parked; and there is no longer one place that knows how many lanes the Coordinator
ordered, which is what the join counts against.

Both pauses use one mechanism deliberately. A clarifying question and an approval are the same shape —
the lane stops, something outside the system answers, the lane continues — and building two mechanisms
means maintaining two sets of resume, timeout and replay semantics.

## Why the approval card comes from the typed object

> **Defends Rule 11.**

What the approver reads and what executes are rendered from the same structure. Not from model prose
describing the action.

If the card is prose, the approver is agreeing to a description, and nothing binds the description to
the action. That is not a hypothetical failure: it is how a narrowed or substituted action passes a
human check, which is the same hole Rule 10 closes from the other side.

## Why retrieval blocks rather than degrades

> **Defends Rule 12.**

The runbook decides what verification an action requires. When retrieval falls below the reranker
threshold the lane escalates; it never answers from what the model happens to know.

A model that has read the internet knows how password resets usually work. It does not know how
SkillStorm's policy says they work, and the difference is invisible in the output — the ungrounded
answer is fluent, plausible and specific. Degrading to model knowledge does not produce a worse
answer, it produces an unreviewable one.

## Why the entitlement check is inside the tool

> **Defends Rule 14.**

Every call checks that the requester has a grant over the target. Not the plan, not the gate — the
tool, on every call.

With approval gated to three lifecycle operations, everything else executes on this check alone. It is
the only thing between a spoofed email and a colleague's password, and § 2.3 is explicit that sender
identity is only as good as SPF, DKIM and DMARC. A check that lives in the planning layer is a check
an injected instruction can plan around; a check inside the tool is one it cannot.

It also has to deny loudly. A denial that returns an empty result set is indistinguishable from "found
nothing", and a worker will reason onward from the wrong premise.

## Why a lane owns its own thread

> **Defends Rule 15.** Silent when it breaks.

A lane is `(run_id, sub_request_id)` and owns its own agent thread, budget counters and durable row.

Two identity sub-requests in one email — the brief's own example — route to the same Identity worker.
If that worker is one agent with one conversation thread, lane 1's evidence is in lane 2's context, and
lane 2 reasons about an account it was never asked about. Nothing errors. The run record looks
plausible. The only symptom is an occasional answer that is subtly about the wrong person.

It is also what makes "the lanes are independent" a testable claim rather than a description, and what
keeps the design on the `WorkflowBuilder` side of § 3.4's Magentic line.

## Why idempotency is everywhere, and least privilege underneath it

> **Defends Rules 16 and 17.**

HubSpot retries a webhook whose handler throws, with a byte-identical body. Power Automate can post a
decision twice. A partially failed lane gets re-entered. None of these are edge cases; they are the
normal operation of the systems this one sits between, which is why every write is keyed and every
executor safe to run twice.

Least privilege is the same argument applied to blast radius rather than repetition. Each executor
gets narrowly scoped Graph permissions, and a gated executor refuses to run without a matching
approval record **regardless of what the graph handed it** — because the graph is code the team is
writing for the first time, under time pressure, and the executor is the last place to catch a bug in
it.

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
