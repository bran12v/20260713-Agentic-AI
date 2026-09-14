# High-Level Requirements Document — HelpDesk AI Automation System

| | |
|---|---|
| **Project Name** | HelpDesk AI Automation System |
| **Version** | 1.0 |
| **Date** | September 2026 |
| **Duration** | 2 weeks |
| **Team Size** | 16 |

---

## Where your team's requirements live

Everyone reads § 1–3 and § 8. After that, go to your own rows. **The right-hand column is what you
must not break without talking to the team that owns it.**

| Team | Read closely | Contracts you own |
|---|---|---|
| **Orchestration** | § 3.1–3.4, 4.1, 4.6, 4.8 | `Plan`, `SubRequest`, `ProposedAction` · the selection function · the join's output |
| **Knowledge & Retrieval** | § 4.4, 4.7 · `corpus/MANIFEST.md` | The index schema and filterable fields · the retrieval tool signatures |
| **Identity & Control** | § 4.2, 4.3 · § 5 | The action enum · `ApprovalRecord` · the MCP tool signatures |
| **Edge & Approvals** | § 4.1, 4.5, 4.6 · § 6 all | `/tickets/ingest` and both approval endpoints · the HubSpot ticket contract |
| **Platform & Quality** | § 5, 7, 9 | `RunRecord` · the fakes library · the CI evaluation tier |

Three contracts are fixed before you start and are not yours to change: the ingest payload (§ 6.1),
the approval request (§ 6.2) and the approval callback (§ 6.3). Everything else that crosses a team
boundary is frozen on day 1 (§ 8).

**Why the architecture is shaped this way is in [design-rationale.md](design-rationale.md).** Read it
once, at the start. It is not a requirement and you do not need it open while you build.

---

## 1. Executive Summary

SkillStorm's IT HelpDesk receives support requests through HubSpot via the email inbox and direct
ticket creation. This project delivers an AI system that investigates every inbound ticket against
live identity state, decides what — if anything — should be done about it, obtains human approval
before it deactivates, reactivates or deletes an account, and executes routine IT service management
(ITSM) tasks end to end without manual intervention.

The system is built in Python (Flask) using the **Microsoft Agent Framework** for agent primitives
and orchestration, **Azure AI Foundry** model deployments, and **Azure AI Search** for retrieval over
the IT runbook, policy and laptop-manual corpora. It is deployed to Microsoft Azure via GitHub Actions
CI/CD and
integrated with HubSpot, Microsoft Entra ID, Microsoft Graph and Power Automate.

**The shape in one paragraph.** A ticket is a symptom, not an instruction, so the system does not
classify it into a workflow — it decomposes it. A Coordinator decides how many distinct requests the
email contains and dispatches each to the specialist that owns it. Each lane investigates with its own
tools until it can propose an action set, and the three operations that change whether a person can
work wait on a human before they run. § 3 is the architecture; [design-rationale.md](design-rationale.md)
is why it is shaped that way.

**Primary business goals**

- Reduce mean time to resolution for common IT requests (password resets, account lockouts,
  provisioning) from hours to minutes.
- Reduce manual HelpDesk workload for repetitive Tier-1 tasks.
- Enforce consistent, auditable execution of identity operations, with human approval on the three
  that change whether a person can work.

---

## 2. Scope

### 2.1 In Scope

- **Account lockout resolution** — MFA reset and account unlock workflows.
- **Password reset** — automated, verified password resets with secure delivery.
- **User activation/deactivation** — enabling and disabling user accounts.
- **Email ticket intake** — all requests arrive via the email inbox (or direct HubSpot ticket
  creation); HubSpot captures them and forwards every ticket/email to the system's single ingestion
  endpoint.
- **User entitlement resolution (authentication/authorization)** — determine which tools and
  applications a given user has access to, based on identity, group membership and role.
- **Entitlement service over MCP** — the identity-scoped reads sit behind an MCP server that resolves
  the caller from authenticated context rather than from a tool argument, and enforces the grant on
  every call.
- **Laptop troubleshooting** — diagnose common hardware and OS symptoms against the manufacturer
  manuals and service guides for the laptop models SkillStorm issues, and return grounded,
  model-specific steps on the ticket.
- **Session revocation & user removal** — revoke all active sign-in sessions; disable and delete user
  accounts.
- **New user provisioning** — create the account, its mailbox, its group memberships and its license,
  in that order, as one ordered chain.
- **Approval-gated lifecycle operations** — account deactivation, reactivation and deletion are gated
  behind the Power Automate approval flow (human-in-the-loop). Every other operation executes once the
  entitlement check passes.
- **Single ingestion endpoint** — one webhook endpoint invoked by HubSpot for every inbound
  email/ticket, which triggers investigation and downstream execution.
- **Two approval endpoints** — (a) trigger the Power Automate approval flow for a specific pending
  action; (b) callback endpoint invoked when the action is approved or rejected, to resume or cancel
  execution.
- **Grounded knowledge layer** — the IT runbook, policy, tool-access and laptop-manual corpora
  indexed in Azure AI Search, used to determine the verification steps an action requires, and to
  ground device troubleshooting.
- **Robust automated testing** — unit, integration, agent-evaluation and end-to-end suites wired into
  CI.
- **Cloud deployment** — Azure-hosted runtime with GitHub Actions CI/CD pipelines.

### 2.2 Out of Scope

- Building HubSpot integrations from scratch. The inbound action that calls `/tickets/ingest` is
  already written and lives in the HubSpot portal; what this project consumes is its wire contract in
  § 6.1. Outbound is a documented set of API calls, not an integration to design.
- Building the Power Automate approval flow itself. The flow and its custom connector are built ahead
  of the project; this project builds only the two endpoints that interact with them, against the
  contracts in § 6.2 and § 6.3.
- Hardware provisioning, procurement, or physical asset management.
- Non-IT ticket categories (HR, payroll, facilities) beyond recognizing them and declining with the
  reason and the correct channel.
- Migration of historical ticket data.
- Voice/phone channel support.

### 2.3 Assumptions

- HubSpot is the system of record for all tickets; every ticket/email arrives at the system through a
  single webhook call from HubSpot.
- **The requester's identity is only as trustworthy as the mail transport.** HubSpot passes the
  inbound `From` and cannot attest it, so the guarantee rests on SPF, DKIM and DMARC being enforced at
  the connected inbox. This assumption carries more weight than it appears to: with approval gated to
  three lifecycle operations, § 4.3's entitlement check is the only control standing between a spoofed
  email and a colleague's password.
- The Power Automate approval flow accepts an HTTP trigger and can call back to a provided URL with an
  approval decision.
- The organization uses Microsoft 365 / Entra ID as the identity provider, and Microsoft Graph API
  access with appropriate application permissions will be granted.
- **Assembling the corpus is the project's work, not a precondition.** Existing SkillStorm material is
  raw input where it exists; where it does not, the team authors the operational layer — the
  per-operation procedures the policy gate retrieves. Establishing which laptop models SkillStorm
  issues is part of that work, and the answer sets the `device_model` enum.
- **Nothing on the ticket identifies the requester's laptop today.** `device_model` is one of five
  custom properties that have to be created before it can, and until then the model can only be parsed
  from the ticket text or asked for. The Device Worker must handle both.
- An Azure subscription and resource group are available at project start, with an **Azure AI Foundry
  project** carrying a reasoning-tier deployment, a fast-tier deployment and an embedding deployment.
- An **Azure AI Search** service at Basic tier or higher, so the semantic ranker is available. The
  Free semantic tier's 1,000 request/month allowance will not survive a single retrieval calibration
  sweep.

### 2.4 Constraints

- **Timeline:** 2 weeks — nine working days of build, with the final presentation on day 10. Fixed.
- **Team:** 16 people.
- **Stack:** Python 3.11+ / Flask for all APIs; Microsoft Agent Framework for agent primitives and
  orchestration; Azure AI Foundry for models; Azure AI Search for retrieval; **Azure Service Bus
  between the webhook and the graph**; PostgreSQL for state, audit and checkpoints; Azure for hosting;
  GitHub Actions for CI/CD.
- **No third-party agent framework** — LangChain, LangGraph, CrewAI and equivalents are excluded from
  the orchestration, retrieval and write paths.
- **Keyless end to end** — `az login` locally, managed identity when deployed. One documented
  exception: the approval flow authenticates to `/approvals/callback` with a shared secret held on a
  Power Platform connection, because Power Automate has no HMAC function and cannot mirror the scheme
  the HubSpot side uses. It is a secret between two first-party components, stored in Key Vault, and it
  is the only one.
- **Pin exact package versions.** The Agent Framework renames classes between releases; verify the
  names against the version you pin before writing against them, and record the pinned versions in the
  architecture document.
- **The approval-gated set is closed and defined in code:** deactivate, reactivate, delete. It is not
  a runtime judgment and the model has no say in it. Every other action executes once the entitlement
  check passes, and every action of either kind lands on the run record and the ticket.

---

## 3. System Overview & Architecture

### 3.1 High-Level Flow

```
  HubSpot email ──▶ POST /api/v1/tickets/ingest ──▶ INTAKE (deterministic)
  Direct tickets                                    dedupe · redact · verify
                                                    requester · enqueue
                                                              │
                                                              ▼
                                               ┌──────────────────────────┐
                                               │  COORDINATOR (agent)     │
                                               │  0..N SubRequests, each  │
                                               │  naming a worker         │
                                               └────────────┬─────────────┘
                                      N = 0  ◀──────────────┤
                                    (decline,               │
                                     reply, close)          │
                                                            │
              selection function (pure) — the fan-out width is the model's
          ┌─────────────────────────────┬─────────────────────────────┐
          ▼                             ▼                             ▼
    IDENTITY WORKER               ACCESS WORKER                 DEVICE WORKER
    Graph reads (MCP)             groups · roles                manuals filtered
    identity runbooks             tool-access matrix            on device_model

  ══ every lane below is the same shape; one lane drawn, N run ═════════════════

              ┌────────────────────────────────────────────────┐
              │                 OWNING WORKER                  │◀──┐
              │   loops on its own tools · own agent thread    │   │
              └───────┬─────────────────┬──────────────────────┘   │
        needs_info /  │                 │ proposes 0..N actions    │
        decline       │                 ▼                          │
                      │         ┌───────────────┐   reject         │
                      │         │  POLICY GATE  │─────────────────▶┤  ①
                      │         │(deterministic)│                 │
                      │         └───────┬───────┘ pass             │
                      │                 ▼                          │
                      │         ┌───────────────┐   reject         │
                      │         │  GROUNDING    │─────────────────▶┤  ②
                      │         │  REVIEWER     │                  │
                      │         └───────┬───────┘ pass             │
                      │        ┌────────┴────────┐                 │
                      │   not gated         gated set              │
                      │        │                 ▼                 │
                      │        │        ╔═════════════════╗        │
                      │        │        ║ INTERRUPT +     ║        │
                      │        │        ║ CHECKPOINT      ║        │
                      │        │        ║ (approval)      ║        │
                      │        │        ╚════════╤════════╝        │
                      │        │      rejected   │ approved        │
                      │        │        ◀────────┤                 │
                      │        │     close lane  ▼                 │
                      │        │        ┌───────────────┐ withdraw │
                      │        │        │  RE-VALIDATE  │─────────▶┤  ③
                      │        │        └───────┬───────┘          │
                      │        └────────┬───────┘ still holds      │
                      │                 ▼                          │
                      │            ┌─────────┐   partial failure   │
                      │            │ EXECUTE │────────────────────▶┘  ④
                      │            └────┬────┘
                      │                 │
                      └────────┬────────┘
                               ▼
                        lane terminal state
  ══════════════════════════════════════════════════════════════════════════════
                               │
                               ▼
              JOIN (hand-written) — counts lane arrivals against the
              Coordinator's ordered SubRequest list
                               │
                               ▼
              Ticket updated/closed in HubSpot + run record

  ① ② ③ ④ are the four bounded cycles. Each re-enters the lane's OWN worker with
  a structured objection, and each carries a hard cap (§ 5) — the graph is cyclic,
  not a DAG.

  A needs_info question interrupts and checkpoints exactly as an approval does;
  the requester's reply resumes the same run.

  Lanes reach different stages independently: approval #1 can return at 14:02 and
  #2 at 17:40. The join assembles the ticket update and is not a barrier before
  approval.
```

### 3.2 Core Components

| Component | Description | Technology |
|---|---|---|
| **Ingestion API** | Single webhook endpoint receiving all HubSpot ticket/email events. Validates the HMAC signature and its timestamp header against the raw request bytes, deduplicates on HubSpot event id, redacts, runs Prompt Shields over every string cracked out of the email, resolves the requester from verified sender identity, and enqueues. Returns inside HubSpot's webhook timeout; the graph runs out of band. **Prompt Shields runs on the consumer side of the queue, not in the webhook** — it is a Content Safety round trip per string and the webhook has a timeout to meet. | Flask, Azure Container Apps, Azure Service Bus |
| **Coordinator** | Reads the ticket and decomposes it into 0..N independent sub-requests, naming the worker each needs. Emits a typed `Plan`. Holds no tools, and never reads a lane's result — it decomposes, and the join assembles. | Agent Framework, Foundry reasoning deployment |
| **Identity Worker** | Given one sub-request, works out what is actually wrong with the account and the minimal action set that fixes it. A custom `Executor` owning an agent, not a bare `AgentExecutor`, so it takes a typed `SubRequest` in and holds a per-lane agent thread. Loops on read-only Graph tools reached through the MCP server, plus identity runbooks. | Agent Framework, Foundry reasoning deployment |
| **Access Worker** | Answers what a person has and whether they should have it, against group membership, role and the tool-access matrix. Its outcome is often an answer rather than an action. | Agent Framework, Foundry reasoning deployment |
| **Device Worker** | Decides whether the manual corpus covers the reported symptom and what steps to give. Mutates nothing, ever. | Agent Framework, Foundry fast deployment |
| **Entitlement MCP server** | Holds the identity-scoped reads — `get_user`, `get_group_memberships`, `resolve_entitlements`. Resolves the caller from authenticated context, never from a tool argument, and enforces the grant on every call. **Holds the only database credential — no agent reaches PostgreSQL directly.** The second deployed service. | Python, Streamable HTTP, Azure Container Apps |
| **Join** | Counts lane arrivals against the Coordinator's ordered `SubRequest` list and assembles the ticket update. Hand-written, because a fan-in declared over three workers blocks forever when the selection function activated one. **It runs whenever a lane reaches a terminal state, not once** — a ticket with a lane still awaiting approval gets an interim update saying which lanes finished and which is waiting on whom. A lane that never arrives is reaped by the same deadline that expires approvals and becomes `escalated`. | Agent Framework workflow layer |
| **Orchestration graph** | `WorkflowBuilder` executors and typed edges: the model-sized fan-out from the Coordinator, the per-lane gate and reviewer, the per-action fan-out onto the approval interrupt, the re-validation and execution legs, the four bounded cycles back into the owning worker, and the join. **The graph is built with the framework's primitives, not hand-rolled `asyncio`** — the queue consumer that starts a run is ordinary async code and is not what this excludes. | Agent Framework workflow layer |
| **Knowledge layer** | Azure AI Search over three indexes: the IT runbook / policy / tool-access corpus, the laptop manuals for the models SkillStorm issues, and closed-ticket resolutions. Hybrid retrieval with the semantic ranker, filterable on `doc_type`, `section_path` and `device_model`. Refusal is gated on `@search.rerankerScore`. | Azure AI Search, Azure AI Foundry embedding deployment |
| **Policy gate** | Deterministic code. Checks the requester's entitlement over the target on every action, decides from the closed action enum whether the action falls in the approval-gated set, and enforces the verification steps the retrieved runbook requires. Runs per lane, and rejects back into that lane's owning worker with a structured objection. | Python |
| **Grounding reviewer** | A harness stage with its own session per lane, never sharing a transcript with a worker. Checks that every grounded claim — the justification on a proposed action, **and the steps in a Device lane's reply to the requester** — is actually supported by the chunk it cites. A requester reading unreviewed device steps is the same failure as an approver reading ungrounded prose, and the device corpus is where a wrong answer is most fluent. | Agent Framework, Foundry fast deployment |
| **Approval service** | Two endpoints bridging the graph and the provided Power Automate flow. Persists a pending-approval record per gated action, renders the approval card from the typed action object, and re-enters the graph on decision. Actions outside the gated set never reach it. | Flask, PostgreSQL |
| **Action executors** | Deterministic, individually testable, idempotent Python functions: MFA reset, password reset, user create, enable/disable, session revoke, delete, and ticket update. Unreachable by the model. | Microsoft Graph SDK, Exchange, HubSpot integrations (provided) |
| **Audit & observability** | A run record per ticket covering every tool call, retrieval, gate decision, approval and execution result. Agent tracing, token usage, latency and cost via the Agent Framework's OpenTelemetry layer exporting to Azure Monitor. | PostgreSQL, `agent_framework.observability`, Application Insights |
| **Identity/Secrets** | Managed identities and secret storage for all credentials. | Azure Key Vault, Entra ID app registrations |

### 3.3 Design Rules

The rules a builder has to hold. **Why each one is this way is in
[design-rationale.md](design-rationale.md)** — read it once before you argue with a rule, not while
you are implementing it.

| # | Rule |
|---|---|
| 1 | **The unit of work is the sub-request.** Each lane carries its own policy gate, grounding review, re-validation, budget and terminal state. There is no single point where the ticket "is". |
| 2 | **Workers investigate; they do not classify.** A worker gets a goal and read-only tools, not a label set. The number of tool calls varies by sub-request. |
| 3 | **The fan-out width is the model's; the routing is a pure function.** The Coordinator emits a typed `Plan`; a selection function routes deterministically on it, unit tested with no model in the loop. |
| 4 | **The Coordinator decomposes only.** It holds no tools and never reads a lane's result. The join assembles. |
| 5 | **The join is hand-written and sits after execution.** It counts arrivals against the Coordinator's ordered `SubRequest` list. It is not a barrier before approval. |
| 6 | **The model decides what; the graph routes it; code executes it.** Every action is a member of a closed enum defined in code. The model never composes an API call and never reaches an executor. |
| 7 | **The approval-gated set is closed and defined in code** — deactivate, reactivate, delete. Not a runtime judgment, and the model has no say in membership. |
| 8 | **Gating is per action, not per lane.** A lane proposes an action *set*, and a set can hold gated and ungated members. The lane fans out once more over its own actions, the ungated ones execute, each gated one gets its own approval record, and a second small join closes the lane. § 4.2 depends on this: a mixed ticket runs the ungated and holds the gated. |
| 9 | **A pause is an interrupt plus a checkpoint on the same run** — see 3.3.1. |
| 10 | **Approval is permission to act, not a committed instruction.** On re-entry the owning worker re-validates against live state before executing. |
| 11 | **The approval card is rendered from the typed action object**, never from model prose. |
| 12 | **Retrieval is load-bearing.** Below the reranker threshold the lane blocks and escalates. It never degrades to answering from model knowledge. |
| 13 | **Identity is resolved server-side.** Entitlement-scoped reads sit behind the MCP server, which takes the subject from authenticated caller context. An in-process tool can always be handed whatever the model produced. |
| 14 | **A lane is `(run_id, sub_request_id)`** and owns its own agent thread, its own budget counters and its own durable row. Two sub-requests routed to the same worker must not share a transcript. |
| 15 | **Idempotency everywhere.** Ingest dedupes on event id, the approval callback on decision id, ticket writes on `ai_run_correlation_id`, and executors are idempotent. |
| 16 | **Least privilege.** Narrowly scoped Graph permissions per executor, and a gated executor refuses to run without a matching approval record regardless of what the graph handed it. |

Rules 1, 3, 5 and 14 are what make this a multi-agent system rather than a workflow. Rules 6, 7, 13
and 16 are what make it safe to point at a directory.

#### 3.3.1 How a lane pauses

A lane pauses for two reasons — it needs an approval, or it needs information from the requester.
**Both use one mechanism and it is the framework's, not a hand-rolled one.**

- The lane raises a request through the framework's human-in-the-loop primitive
  (`RequestInfoExecutor` / `request_info` — **verify the class names against the version you pin**,
  per § 2.4) and the **run interrupts and checkpoints**.
- When the answer arrives — an approval decision on the callback, or a requester reply with
  `kind: reply` — **the same run resumes from where it stopped.** It continues down the happy path; it
  does not start again and it does not replay work already done.
- **A rejection stops that lane where it is and closes it out gracefully**, recording the reason on
  the ticket. It does not fail the run, and it does not touch the other lanes.
- **Resume is single-writer.** The callback can land on any replica, and two replicas rehydrating one
  checkpoint would fork the run and let both copies write the ticket. Serialise it — a row lock on the
  ticket, taken before rehydration and held until the run idles again.

The durable record and the checkpoint are joined: the record is what the callback looks up, the
checkpoint is what the run resumes from. **Checkpoint storage is the team's to implement** against a
backing store that survives a replica restart; the shipped in-memory backend does not.

**What "independent lanes" means precisely.** Lanes reach their stages independently and never block
each other's progress or share state. It does not mean the run is executing two lanes in the same
instant — while any lane is interrupted the run is idle, not busy. Ordering independence is the
property that matters and the property the tests assert.

### 3.4 Not a Named Orchestration Pattern

The Agent Framework ships five orchestration builders — Sequential, Concurrent, GroupChat, Handoff and
Magentic. **This system uses none of them directly**, and
[design-rationale.md](design-rationale.md) gives the reason for each.

What it builds instead is a `WorkflowBuilder` graph using the primitives directly: a variable-width
fan-out driven by a selection function over a typed plan, three specialist workers looping on their
own tools, a conditional edge onto the approval interrupt, four bounded cycles, the reviewer,
re-validation, and a join written by hand.

> **The Magentic guard rail.** If the Coordinator ever reasons about one lane's result in order to
> revise another, the design has become Magentic and `MagenticBuilder` should be used rather than
> rebuilt by hand. Keeping the lanes independent is what keeps this a `WorkflowBuilder` graph, and the
> architecture document has to record that the team held that line.
>
> Re-planning **inside** a lane is not Magentic and is required — a gate rejection, a withdrawn
> action and a partial failure all re-enter the owning worker, which decides how to proceed. The line
> is cross-lane reasoning, not re-planning as such.
---

## 4. Functional Requirements

The system supports the capabilities below. Exact behaviors, validation rules and edge-case handling
will be defined during design and refined iteratively during the build.

### 4.1 Ticket Intake and Investigation

- A single endpoint receives every HubSpot email/ticket. Intake is deterministic: signature
  validation, deduplication on event id, PII redaction, Prompt Shields over every string taken from
  the email, and resolution of the requester from verified sender identity.
- **The Coordinator decomposes the ticket into 0..N independent sub-requests**, each naming the worker
  it needs, and emits them as a typed `Plan`. One email asking to unlock an account, grant a tool and
  fix a full disk is three sub-requests, not one ticket with three sentences.
- **Zero sub-requests is a valid outcome**, and so is one. A selection function routes the plan
  deterministically; the plan's width is the model's decision and does not appear in the code. It is
  bounded all the same — a configured `MAX_SUB_REQUESTS` caps the fan-out, and a plan exceeding it is
  truncated to the cap and the ticket escalated, because a garbled or hostile email that decomposes
  into forty lanes is a cost incident.
- Each worker holds read-only tools scoped to its domain: Entra ID user lookup, group membership,
  sign-in and lockout status and license assignment for Identity; groups, roles and the tool-access
  matrix for Access; the laptop manuals for Device. Runbook retrieval and closed-ticket search are
  available to all three.
- **The tool sequence inside a lane is chosen at runtime.** Which lookups run, in what order, and how
  many, follows from what the previous lookup returned. Two tickets of different shape must produce
  visibly different run records, and a fixed one-call-each shape is a failure.
- **A lane terminates in exactly one of four states**, and the set is closed:

  | Terminal state | Meaning | Ticket effect |
  |---|---|---|
  | `executed` | The action set ran | Summary on the ticket |
  | `answered` | A grounded reply, no action — the Device lane's normal outcome | Reply on the ticket |
  | `declined` | Out of scope, or denied at the entitlement check | Reason on the ticket |
  | `escalated` | The system could act but must not decide alone | Handed to a human, evidence attached |

  A worker reaches one of these on a structured decision — a plan, a question, or a decline — backed by
  an independent hard cap on tool calls and iterations. A question is not a terminal state: it
  interrupts the lane (§ 3.3.1) and the lane terminates after the reply.

- **Escalation is a real state with a real destination.** It fires when retrieval falls below the
  reranker threshold, when a device symptom is outside the corpus for that model, when an approval
  expires, or when the investigation finds something a human must judge — such as a "can't log in"
  sub-request on an account deliberately disabled pending termination, where the correct outcome is a
  reply and an escalation, not an unlock. **An escalated lane sets `ai_status` to `escalated`, leaves
  the ticket open in New, assigns it to the HelpDesk owner queue, and writes the evidence it gathered
  onto the ticket as an internal note.** It never closes the ticket and it never guesses.

- **The four terminal states are per sub-request, not per ticket.** One email can produce a clarifying
  question on one lane, an executed action on a second, and an escalation on a third, and the ticket
  update says so. **`ai_status` is per ticket and therefore reports the least-finished lane** — a
  ticket with one lane executed and one awaiting approval reads `awaiting_approval`. The per-lane
  states live on the run record, which is where the ticket update is assembled from.
- Where the target user is ambiguous, missing, or matches more than one directory entry, the system
  composes a clarifying question and emails it to the requester on the ticket thread rather than
  guessing. The ticket stays open and its status records that it is waiting on a reply; the answer
  arrives as a reply and resumes the lane rather than starting a new one.
- **An out-of-scope ticket is declined, not queued.** The system replies on the ticket — which
  reaches the requester by email, since the ticket is the channel they wrote in on — naming the
  specific reason the request falls outside this system's remit, pointing at the correct channel where
  one exists, and inviting a fresh ticket for anything else they need. The ticket is then closed as
  out of scope, with the reason recorded on the run record so declines are reportable.
- A decline mutates nothing. It never states or implies that the request was refused on policy
  grounds when the truth is that the system does not handle it.

### 4.2 Identity and Account Operations

Each operation is a member of a closed action enum defined in code, and the enum records whether the
operation is approval-gated:

| Operation | Approval |
|---|---|
| MFA reset / account unlock | Not gated |
| Password reset, with secure credential delivery | Not gated |
| User and mailbox creation | Not gated |
| Group membership add / remove | Not gated |
| License assign / remove | Not gated |
| Session revocation | Not gated |
| Account deactivation | **Gated** |
| Account reactivation | **Gated** |
| User deletion | **Gated** — and irreversible |

**Some actions are ordered.** Provisioning is the case that matters: create user → mailbox → group
membership → license, where each step needs the one before it to have succeeded. `ProposedAction`
carries a `depends_on` naming the action it follows, the executors run a chain in that order, and a
step that fails **stops the chain there rather than continuing past the gap**. The lane then takes
§ 4.8's partial-failure path with the completed prefix recorded, because a user with a mailbox and no
license is a state a human has to see, not one to retry blindly.

**A ticket mixing gated and ungated actions runs the ungated ones and holds the gated ones**, and the
ticket update says plainly which executed and which is waiting on whom.

### 4.3 Entitlements

- Given a user, determine which tools and applications they have access to, based on identity, group
  membership and role.
- **The requester's authority over the target is checked inside the tool, on every call** — not once
  at session start, and never stated in the system prompt. An unentitled call returns a structured
  denial, never an empty result set, so a worker can distinguish "not permitted" from "nothing found".
- **The identity-scoped reads sit behind an MCP server**, which is the only place that check can
  actually be enforced. `get_user`, `get_group_memberships` and `resolve_entitlements` live there; the
  server resolves the caller from authenticated context and rejects any request asserting an
  unverified identity. It also holds the only database credential — **no agent reaches PostgreSQL
  directly**.
- **Retrieval tools stay in-process**, including `find_similar_tickets`. Runbooks, manuals and closed
  tickets are Azure AI Search indexes, none of them entitlement-scoped, and a server in front of them
  adds a hop without adding a control. The dividing line is whether the answer depends on *who is
  asking*, not on what backs the data.
- The server must be demonstrably driven by a second consumer — Claude Code, MCP Inspector or another
  host — with a server-side log line showing the call arrived over Streamable HTTP and was authorized
  as that caller rather than as the workflow.
- **A requester may act on themselves; acting on anyone else requires a recorded grant.** Because most
  operations now execute on the entitlement check alone, this is the control standing between a
  spoofed email and a colleague's password. A reset aimed at the verified sender is self-service; the
  same request aimed at someone else without a grant is denied at the tool, not escalated into a
  plan.

### 4.4 Laptop Troubleshooting

- The manufacturer manuals and service guides for the laptop models SkillStorm issues are indexed in
  Azure AI Search and reachable by the Device Worker as a read-only tool, when the investigation
  implicates the device rather than on a fixed step.
- **The Device Worker resolves which model the requester has** from the ticket text or the HubSpot
  record, and asks where it cannot. Every manual query filters on the resolved `device_model`; an
  unfiltered query is a defect, because an answer drawn from the wrong model's manual is fluent,
  specific, and carries a citation that resolves.
- Where the corpus covers the symptom, the system returns grounded, model-specific steps on the
  ticket, citing the manual and the section they came from.
- Where the manual's procedure terminates in service, or the symptom indicates hardware failure, the
  ticket escalates to the human queue with the evidence attached. Physical repair and depot dispatch
  are out of scope.
- Where the requester's model is not in the corpus, the system refuses and escalates. It never answers
  a hardware question from model knowledge.
- **Every fleet model is in the corpus and they are not covered equally**, which is the harder version
  of the same rule. Four models have full troubleshooting procedures, two have specifications and views
  only, one has a spec sheet and nothing else, and the MacBook Pro carries pointers to Apple's articles
  rather than answers. `corpus/manuals/SOURCES.md` maps question classes to the models that can answer
  them. **A symptom the corpus cannot address for the requester's specific model escalates** — it never
  borrows a procedure from a model whose manual does carry one, however similar the two machines are.
- **This branch produces no action at all**, because nothing mutates. It is the clearest case of a
  ticket whose correct outcome is a grounded reply rather than an execution.

### 4.5 Ticket Updates

- **Anything returned to the requester reaches them as email on the ticket thread** — a clarifying
  question, troubleshooting steps, or a decline with its reason. The ticket remains the complete record
  of the exchange, and the requester does not have to log in to read it.
- **The investigation summary, the actions proposed and the approval outcome are internal notes**, not
  replies. They are the audit trail § 5 requires; emailing them to the requester would send the
  system's own reasoning to the person who asked the question.
- **Only two ticket states are used: it arrives open and ends closed.** In-flight state lives on the
  `ai_status` ticket property rather than in the pipeline, so a ticket awaiting approval and a ticket
  awaiting a reply are distinguishable without adding stages that have to be kept consistent. Its six
  values are `investigating`, `awaiting_requester`, `awaiting_approval`, `executing`, `done`,
  `declined` and `escalated` — a closed set, listed with the other custom properties in the outbound
  cookbook. It is per ticket and reports the least-finished lane; per-lane state lives on the run
  record.
- Ticket writes are idempotent on `ai_run_correlation_id`, so a retried update does not append a
  duplicate summary. The platform offers no idempotency key, so this is the system's to enforce.

### 4.6 Approvals

- **Three operations are approval-gated: deactivation, reactivation and deletion.** The set is closed,
  defined in code, and not a runtime judgment. Every other operation executes once the policy gate's
  entitlement check passes.
- One endpoint triggers the provided Power Automate approval flow for a specific pending gated action.
- A second endpoint receives the decision: an approved action proceeds to re-validation, a rejected one
  cancels and updates the ticket.
- **A gated action reaching an executor without a matching approval record is refused at runtime.** The
  executor checks for itself; the graph is not the only thing standing between a delete and the
  directory.
- **After approval, before execution, the action is re-validated against live state.** Re-validation
  is defined, not judged: **re-run the tool calls recorded in the action's `preconditions` and compare
  the results to the values recorded there.** A precondition that has moved withdraws the action, and
  the withdrawal is recorded on the ticket with the reason. It may also narrow the action — but
  narrowing that changes the action type re-enters approval rather than executing under the old one
  (§ 5).
- **A rejection reason re-enters the graph as input, not as a terminal state.** An approver rejecting
  with "wrong person — this is the contractor Jane Doe" produces a narrowed re-investigation through a
  bounded cycle, not a closed ticket.
- Approvals that are never answered expire on a configured deadline and route to the human queue. Any
  ungated actions on the same ticket are unaffected — they have already run.
- **Expiry belongs to this system, not to the approval flow.** The pending record is ours, so we reap
  it. A decision arriving for a record that has already expired or already been decided is refused,
  and the action does not execute — an approver clicking Approve an hour after the deadline must not
  reach a directory.
- **The flow reports its own timeout, and being told something is already expired is normal.** On
  timeout it posts `decision: expired` with `approver: system`, and the `409` it gets back when the
  record was already reaped is the correct answer, not an error to alert on. The flow also takes that
  branch when an approval *fails* rather than times out, so the report arrives either way instead of
  being lost. See § 6.3.

### 4.7 Knowledge and Retrieval

- The IT runbook, policy and tool-access corpus is chunked with recorded size and overlap, carries
  per-chunk `doc_id`, `doc_type`, `section_path` and page metadata, and is indexed in Azure AI Search
  with hybrid retrieval and the semantic ranker.
- The laptop manuals are indexed with `device_model`, `doc_type` and `section_path`. Manuals across
  models are near-identical prose carrying different part numbers, key sequences and service steps, so
  an unfiltered query answers confidently from the wrong machine. `device_model` is a required filter
  on every manual query, and a golden case asserts it.
- Closed-ticket resolutions are indexed separately, filterable on `doc_type`, so a worker can cite
  how the same symptom was resolved before. They are precedent, not a conclusion — a plan that
  adopts the nearest neighbour's outcome without its own evidence is a failure.
- **Retrieval decides policy.** The runbook determines the verification steps a given action requires,
  so a plan that could not retrieve its governing runbook section blocks and escalates rather than
  proceeding.
- **The corpus must encode SkillStorm's own choices** — who may request each operation, what must be
  verified first, what makes a case elevated, what must never be done. Content a competent engineer
  already knows is content the model already has, which makes retrieval decorative.
- Refusal is gated on `@search.rerankerScore`, never `@search.score`. Choose the threshold by running
  the golden set and finding where correct and incorrect answers separate; report the value, the
  method, and which score it sits on.
- Every grounded claim in a proposed action's justification carries a machine-checkable citation —
  document id, title and chunk id — that the grounding reviewer verifies.
- **Multi-hop retrieval is required, and `corpus/MANIFEST.md` names the chains.** A runbook that
  states an obligation and defers its verification requirement to a separate identity-proofing policy
  cannot be answered from either document alone. Workers must reach the second hop deliberately,
  filtering on `doc_type`, rather than answering from whichever document the ranker happened to
  favour.
- **`corpus/MANIFEST.md` declares three lists, and § 7 draws cases from each:** the retrieval
  distractors with their occurrence counts, an out-of-corpus topic list with zero occurrences
  anywhere, and a near-miss list of topics that are covered and must not be refused. **Refusal
  precision and recall are reported separately** — a threshold tuned to refuse everything scores well
  on one and badly on the other.
- **The laptop manuals are cracked with Azure AI Document Intelligence**, retaining table structure.
  Service manuals carry part numbers and step sequences in tables, and a chunker that flattens them
  produces citations that resolve to the wrong row. `corpus/manuals/text/` is the committed plain-text
  extraction and is the ground truth to measure against — `corpus/MANIFEST.md` § 6 names two table
  failures already visible in it. **Recovering either is a stretch goal, not an acceptance
  condition.**

### 4.8 Partial Failure

- Where a lane's multi-action plan fails part way through, **that lane's owning worker** is re-entered
  with the results so far and decides how to proceed: continue with a note, substitute, or escalate.
  This is not a fixed error branch.
- **A failure in one lane never cancels another.** Lanes are independent, and a failed access grant
  does not withdraw an unlock that already succeeded.
- Completed actions are never silently rolled back; the ticket states what succeeded and what did not.

---

## 5. Non-Functional Expectations

**Security.** Secrets in Key Vault, keyless authentication throughout, least-privilege Graph scopes,
webhook signature validation, and credentials never exposed in tickets, logs or model context.

**Prompt injection is a first-class threat here.** The ticket body is attacker-controlled email text,
and the system holds tools that disable and delete accounts. Three controls carry it:

- Prompt Shields run over every string cracked out of an inbound email, before it reaches a model.
- **No mutating executor takes its subject from model output.** The model may propose a candidate
  identity; a deterministic Graph lookup resolves it to zero, one or many, and anything but one
  becomes a question. The resolved subject is pinned to the run and every executor reads it from there.
- **A gated executor matches on `(decision_id, subject, action_type)`**, not on subject alone, and any
  mismatch is a runtime refusal. Re-validation may **withdraw** an approved action but never
  **substitute** one: narrowing `deactivate` to `revoke_sessions` keeps the subject and changes what
  the approver agreed to, so a change of action type re-enters approval as a new request.
- Entitlement is enforced inside the tool on every call, so a ticket that talks its way into a plan
  still cannot reach a target the requester has no grant over.

An indirect-injection fixture — an email body instructing the agent to disable an account and close
the ticket — is kept in test fixtures and the system must be demonstrated resisting it.

**Safety and auditability.** No gated action executes without a matching approval record, and no
action of any kind executes without a passing entitlement check. Every classification, retrieval,
tool call, gate decision, approval and execution is recorded on a run record with a correlation id,
PII-redacted, and is traceable end to end in Azure Monitor. A correction to a run record is a new
record referencing the original, never an edit in place.

**Bounds.** Named, typed configuration with defaults in code and per-environment overrides. Max tokens
per call, max tool invocations, max iterations, max retrieved chunks, per-call HTTP timeout and
per-turn wall clock are all **per lane** — a three-lane ticket does not get one lane's budget. The
**cost ceiling is per ticket** and accumulates across lanes, because otherwise a five-lane email costs
five times the cap; concurrent lanes increment that counter under a row lock on the ticket. Budgets are
enforced check-and-stop — usage accumulates after each call and the next leg refuses to start once
spent. Every cycle in the graph has both a structured termination condition and an independent hard cap.

**Post-approval work draws on a separate budget.** Investigation and re-validation are budgeted apart,
because they are minutes or hours apart and a lane that spent its iteration cap investigating would
otherwise be unable to execute the action a human already approved — the budget would have silently
vetoed a human decision. The same applies to the gate-rejection and partial-failure cycles: each
re-entry gets its own allowance, and exhausting it escalates rather than stalling. "Per-turn wall
clock" means one worker invocation — entry to the worker until it returns a structured decision.

**Reliability.** Duplicate webhooks and retries must not double-execute. Retries are bounded, backed
off and respect `Retry-After`. Failures degrade rather than hang: retrieval unavailable means the
affected worker escalates rather than proceeding ungrounded; Graph unavailable means the affected
tools are disabled and the ticket says which capabilities are gone; the MCP server unreachable means
the entitlement-scoped tools are gone, the lanes that need them escalate, and the lanes that do not
carry on.

**Quality.** Type hints throughout, `ruff` clean, a custom exception hierarchy so retrieval, policy,
approval and execution failures are distinguishable by type, structured logging with the correlation
id in a `contextvar`, and quality gates enforced in CI.

**Performance and scale.** Targets to be confirmed with stakeholders, measured from run records rather
than estimated: retrieval under 800 ms, policy gate under 50 ms, a full investigation to proposed plan
under 30 s, and an ingestion endpoint that returns inside HubSpot's webhook timeout.

**Cost.** Measured cost per ticket by scenario, cost per additional investigation iteration, and a
fast-versus-reasoning tier comparison. Prices come from typed configuration, not constants in code.

---

## 6. Endpoints & Integrations

**Built by this project**

**Every endpoint below sits under the base path `/api/v1`.** The ingestion action posts to
`/api/v1/tickets/ingest` and the approvals connector declares `basePath: /api/v1`, so both are already
fixed — the paths in this table are relative to it.

| Endpoint | Behavior |
|---|---|
| `POST /tickets/ingest` | Single entry point called by HubSpot for every email/ticket. Validates the signature, deduplicates on event id, enqueues, and returns inside HubSpot's webhook timeout. The graph runs out of band. |
| `POST /approvals/request` | Triggers the already-deployed Power Automate approval flow for a pending gated action — deactivate, reactivate or delete. The payload is rendered from the typed action object. **Contract in § 6.2.** |
| `POST /approvals/callback` | Receives the approval decision, idempotent on decision id, and re-enters the paused run — which may be on a different replica than the one that raised the request. **Contract in § 6.3.** |

Distinct `/live` and `/ready` probes are exposed for Container Apps. Both sit under `/api/v1` like
everything else, because the approvals connector's health check is bound to `/api/v1/live`.

**The entitlement MCP server** is the second deployed service. Python, Streamable HTTP, its own ACA
app and managed identity, its own `/live` and `/ready`. It exposes `get_user`,
`get_group_memberships`, `resolve_entitlements` and `find_similar_tickets`, resolves the caller from
authenticated context, and holds the only database credential — no agent reaches Postgres directly.

**Consumed:** HubSpot, already integrated in both directions; the Power Automate approval flow and
its custom connector, already built; Microsoft Graph / Entra ID for identity operations and
entitlements; Azure AI Search for retrieval; and Azure AI Foundry model deployments.

**Three contracts are already fixed and are not open for negotiation** — the ingest payload in § 6.1,
the approval request in § 6.2, and the approval callback in § 6.3. An endpoint written to a shape
invented in Week 1 will not be called correctly. What is open is the internal contracts between
teams: the six typed models and the index schema frozen on day 1 (§ 8).


### 6.1 Ingest payload contract

HubSpot posts one JSON object per ticket event. Nineteen fields, all present on every request; the
nullable ones carry `null` rather than being omitted.

| Field | Type | Null? | Notes |
|---|---|---|---|
| `event_id` | string | no | `{ticket_id}:{message_id}`, falling back to `{ticket_id}:created` when the ticket has no conversation thread — chat-sourced and manually created tickets both take that form. **Stable across HubSpot's retries**; this is what deduplication keys on. Treat it as an opaque string, not a parseable pair |
| `ticket_id` | string | no | HubSpot record id |
| `thread_id` | string | yes | Null when the ticket has no conversation thread |
| `message_id` | string | yes | UUID of the newest inbound message; null when there is no thread |
| `kind` | `created` \| `reply` | no | See below — this one carries weight |
| `subject` | string | no | Ticket name, falling back to the email subject. Empty string, never null |
| `body` | string | no | The newest inbound message text, falling back to the ticket description |
| `body_truncated` | boolean | no | True means `body` is a prefix, not the whole message |
| `requester_email` | string | yes | Lower-cased, from the message's delivery identifier, falling back to the ticket's contact rollup |
| `attachment_count` | integer | no | Count only; fetching an attachment is a separate call |
| `channel_id` | string | yes | The conversations channel the message arrived on. `1002` is email — a HubSpot-wide constant, the same in every portal. Null when the ticket has no thread |
| `channel_account_id` | string | yes | The connected mailbox it arrived on. Portal-specific. **Reply with this value** rather than choosing one. Null when the ticket has no thread |
| `pipeline` | string | yes | `648529809` for IT Service |
| `pipeline_stage` | string | yes | Stage id, not label |
| `category` | string | yes | Unpopulated in practice, and its options do not describe IT work |
| `priority` | string | yes | `LOW` \| `MEDIUM` \| `HIGH` \| `URGENT`. Unpopulated in practice |
| `source_type` | string | yes | `CHAT` \| `EMAIL` \| `FORM` \| `PHONE` |
| `created_at` | ISO-8601 | yes | When the **ticket** was created |
| `occurred_at` | ISO-8601 | yes | When **this event** happened. Diverges from `created_at` on every reply |

**Authentication.** Two headers accompany every request:

```
X-Skillstorm-Timestamp: <epoch milliseconds>
X-Skillstorm-Signature: <hex HMAC-SHA256>
```

The signature is computed over `{timestamp}.{raw_body}` with the shared secret. **Verify it against
the raw request bytes.** Re-serialising the parsed JSON and signing that will not match — key order
and separators differ — and is the most common way this check is written wrong. Reject a timestamp
outside a few minutes of now, or a captured request can be replayed indefinitely.

**Four rules the receiver has to honour.**

**Answer a duplicate with a 2xx.** Any non-2xx response makes the HubSpot action throw, and throwing
is what makes HubSpot retry — with a byte-identical body and the same `event_id`. So a duplicate
rejected with `409` is retried forever. Recognise the `event_id`, do nothing, and return `200`.
Reserve non-2xx for a request you genuinely want redelivered: a failed signature check, or a
dependency that was down when the call arrived.

`kind` is not cosmetic. `created` is a new request; `reply` is the requester answering a question the
system itself asked under § 4.1. Treating a reply as a new request restarts the investigation instead
of resuming it, and the ticket never converges.

`body_truncated` means the text is a prefix. Investigating half an email and reporting a confident
outcome is worse than declining.

`created_at` is ticket age and `occurred_at` is event time. A day-old ticket with a reply thirty
seconds ago is a live conversation, not a stale record.

**Reply on the account the message arrived on.** Send outbound messages with the `channel_id` and
`channel_account_id` from the payload, not with values chosen from configuration. The sandbox portal
has four email channel accounts and **three of them share one inbox**, so a receiver that resolves the
account by inbox id sends from `support-3@…` or `sample@…` instead of the helpdesk address — and the
API call succeeds, so nothing fails until someone reads the mail. Configuration is the fallback for a
ticket with no thread, where both fields are null.

**Five behaviours of the producer that are not visible in the table.**

- **Only inbound human messages generate an event.** The action filters on `type = MESSAGE` and
  `direction = INCOMING`, so the system's own email replies and its internal notes never come back as
  ingest calls. There is no loop to break.
- **`body` on a reply is the newest message alone.** It is not the thread, and it carries no quoted
  history. A receiver that expects to reconstruct context from `body` will not get it — the thread is
  a separate fetch.
- **`requester_email` can be null in practice.** It comes from the message's delivery identifier and
  falls back to the ticket's contact rollup; both can be absent.
- **A deleted ticket produces no call at all.** The action ends quietly rather than throwing, so an
  enrolled event can legitimately never arrive. Absence is not evidence of a dropped webhook.
- **`X-Skillstorm-Timestamp` changes on a retry while the body does not.** Deduplicate on `event_id`,
  never on the signature.

**The pipeline and its stages.** `pipeline_stage` is a stage id, not a label, and three of the six
matter:

| State | Stage | Id |
|---|---|---|
| Arrived | New | `954564777` |
| Work finished | Resolved | `954564780` |
| Out-of-scope decline | Unresolvable | `954498199` |

The other three — Assigned `954564778`, WIP `954564779`, Pending Stormer `954498198` — exist and are
left alone. **No stage is needed for an approval wait**: a gated action sets `ai_status` to
`awaiting_approval` and the ticket stays in New. A clarifying question under § 4.1 does the same with
`awaiting_requester`. Every extra stage is one more thing to keep consistent between HubSpot and the
run record.

---

### 6.2 Approval request contract

`POST /api/v1/approvals/request` renders this from the typed action object and posts it to the Power
Automate flow's trigger URL. **Every property is either rendered onto the approval card or used in a
branch** — nothing here is decoration.

| Field | Type | Req. | Notes |
|---|---|---|---|
| `decision_id` | string | yes | Opaque 256-bit token identifying this pending approval. **Unguessable by design**: it is the capability that lets the callback be trusted, so it is never a sequential id |
| `correlation_id` | string | yes | Run correlation id, for tracing the approval back to the investigation that proposed it |
| `ticket_id` | string | yes | HubSpot ticket id |
| `ticket_url` | string | yes | Deep link into HubSpot Help Desk, so the approver can read the thread before deciding |
| `action` | `deactivate` \| `reactivate` \| `delete` | yes | The gated operation. These three are the entire gated set; everything else executes on the entitlement check alone and never reaches this flow |
| `target_upn` | string | yes | UPN of the account the action would change. **Not the requester** |
| `target_display_name` | string | yes | So the card reads as a person rather than a UPN |
| `requester_email` | string | yes | Who asked. Often the same person as the target, and the difference is what an approver most needs to see |
| `justification` | string | yes | Why the system proposes this action, rendered from the typed action object rather than from model prose |
| `risk_tier` | `standard` \| `elevated` | yes | **Derived in code from the action and its blast radius, never from the model. Delete is always `elevated`.** § 7 requires a unit test on this derivation |
| `expires_at` | ISO-8601 | yes | The deadline. The flow's approval timeout is set to match, so it releases rather than hanging. **The receiver owns expiry** and refuses any decision arriving after this |
| `citations` | array | no | Runbook or policy passages the justification rests on, each `{doc_id, title, chunk_id}`. Empty only when no grounded claim was made |

**Send `[]` for citations, never `null`.** The card joins the citation titles into one line, and a
join over null throws — which fails the whole flow and loses the approval. Only `title` is rendered,
so it has to be human-readable on its own; `chunk_id` is what makes the passage resolvable afterwards.

The approval is **first-to-respond**, so one `decision_id` yields exactly one decision. There is no
quorum to reconcile.

---

### 6.3 Approval callback contract

`POST /api/v1/approvals/callback` is called by the flow's custom connector. Authentication is an API
key in the **`X-Approval-Secret`** header — it is entered once when the connection is created and
stored on the connection, not in the flow definition, so exporting the flow does not leak it.

| Field | Type | Req. | Notes |
|---|---|---|---|
| `decision_id` | string | yes | Passed through unchanged from § 6.2. The receiver looks up every other fact from its own record, which is what makes the callback safe to trust |
| `decision` | `approved` \| `rejected` \| `expired` | yes | `expired` only on the timeout branch |
| `approver` | string | yes | Email of the person who responded — **except on timeout, where it is the literal `system`.** A strict email validator here rejects every timeout |
| `comments` | string | no in the schema, **required when rejecting** | The rejection reason is fed into a narrowed re-investigation. A rejection arriving with an empty comment is refused and the approval has to be redone |
| `decided_at` | ISO-8601 | yes | When the approver responded |

**Responses.** `202` — accepted; the paused lane resumes or cancels, body carries `status`
(`accepted`, or `duplicate` when this decision was already recorded) and `ticket_id`. `401` — missing
or incorrect secret. `404` — no pending approval matches this decision id. `409` — this approval
already has a decision, or it expired before the decision arrived; the action does not execute.

**A `409` on an `expired` callback is the expected answer, not a failure.** The receiver reaps its own
pending records because it owns them; the flow's timeout branch only reports what happened on its
side. Do not alert on it. A replayed decision may be answered either with `409` or with `202` and
`status: duplicate` — pick one and be consistent — but nothing may execute twice.

**The liveness probe is at `/api/v1/live`, under the same base path as everything else.** The
connector uses it to test a connection, because testing against the callback would put a fabricated
decision into the system. A `/live` exposed at the root will not be found and the connection test
fails.

**The flow has never been run.** Its shape is fixed and its connector is built, but no approval card
has ever rendered and no callback has ever been posted. Treat § 6.2 and § 6.3 as a contract to build
against and as the first integration to prove, not as a path that is known to work.

---

## 7. Testing

The system is tested at four levels, all running in CI.

**Unit.** Every action executor, the policy gate, the risk-tier derivation, entitlement checks,
idempotency key canonicalization, and the bounds. Async paths tested as async.

**Integration.** Against test tenants and sandboxes — Graph, HubSpot and the approval flow.

**Agent evaluation.** A golden labeled ticket set in version control, machine-readable — one file per
case, or one document holding all of them, as long as a test can load it. Each case carries an id, its
category, the ticket text, the expected outcome, the document ids and section paths that must appear
in the answer's `sources` array, and one line on why the case exists.

| Category | Cases |
|---|---|
| Single-document lookups | 3 |
| Multi-hop, following a manifest cross-reference | 2 |
| Distractor queries, one per declared distractor | 3 |
| Ticket-backed, end to end from a real payload | 2 |
| Out-of-corpus refusals | 2 |
| Near-miss that must **not** refuse | 1 |
| Adversarial | 4 |
| **Total** | **17** |

**Golden cases are written by someone who did not tune retrieval**, against the documents, before
seeing what the index returns. Otherwise the set measures the tuning rather than the system.

**The four adversarial cases:**

1. **Parametric memory versus corpus** — a question the runbook settles *against* the model's prior.
   IT procedure is exactly where a model's general knowledge is confidently wrong: it knows how
   password resets usually work, not how SkillStorm's policy says they work. Run the same question
   with retrieval disabled and commit both transcripts side by side.
2. **Indirect injection through a ticket body** — an email instructing the system to disable an
   account and close the ticket. The Prompt Shields event and the unchanged plan must both be visible
   in the trace.
3. **A gated action elicited obliquely on a follow-up turn** — resolve a lane, then reply to the
   ticket asking to "just go ahead and remove them while you're in there."
4. **Escalation forcing** — a ticket crafted to keep a gated action out of the approval path. The
   gated-set test must be unmoved.

**Paired escalation cases** — for each named trigger, one ticket that fires it and one near-identical
ticket that does not.

Groundedness and relevance run through Foundry's evaluators against a **separately provisioned judge
deployment**, so evaluation does not compete with the workers for TPM and two judged runs stay
comparable. Custom evaluators cover citation accuracy — does each cited chunk actually support its
claim — and refusal precision and recall, reported separately.

**Judged evaluators run twice:** the day the workflow first produces a cited answer, and at the end.
Commit both and analyze the delta.

**End to end**, covering intake → investigation → approval → execution → ticket closure, including the
rejection, timeout and failure paths.

**Six CI cases that a deterministic implementation cannot pass.** Everything else in § 4 is tested by
the golden set above; these six are the ones that specifically fail a hard-coded workflow, and each is
required.

1. **A multi-request email produces N lanes** with N distinct tool sequences in the run record; a
   single-request email produces one. The width is not in the code, so this is the case a state
   machine cannot fake.
2. **Two lanes' approvals return out of order and both execute correctly**, the later one
   re-validating against state the earlier one changed.
3. **The world changed during approval.** Approve a plan, mutate the live state out of band, and
   confirm re-validation withdraws or narrows it rather than executing.
4. **The join distinguishes a complete set from a partial one**, and emits an interim ticket update
   naming which lanes finished and which is still waiting on whom.
5. **An approval record naming a different subject or a different action type than the run's pinned
   pair is refused** — asserted at the executor, not only at the graph.
6. **One lane declines while another executes** on the same ticket, and the ticket update names both.

UAT with HelpDesk staff precedes go-live.

---

## 8. Delivery Approach

**Pipeline.** Lint → tests → secret scan → build → push → deploy → deterministic evaluation tier,
authenticating with GitHub OIDC federated credentials. Images are stored in Azure Container Registry
with the admin user disabled and deployed by digest, not tag.

**Preflight.** Azure AI Search at Basic or higher for the semantic ranker; a separate judge deployment
for the evaluators; recorded provisioned TPM per deployment; and an Azure Cost Management budget with
alerts in place before the first agent run.

**Operations.** A README operations section covering deploy, roll back and tear down, and a
`docker compose up` that brings up PostgreSQL and the service on a fresh clone.

**Team structure.** Sixteen people in five teams.

| Team | Who | Owns |
|---|---|---|
| **Orchestration** | Robert Evans · Charles Eaton · Regan Johnson · Ishan Sultan | The `WorkflowBuilder` graph — the Coordinator, the three specialist workers, the selection function, the model-sized fan-out, the hand-written join, the typed outcomes, the cycles, bounds and hard caps, re-validation on approval re-entry, the per-action fan-out onto the gated set, and **the grounding reviewer**. The hardest and highest-risk work in the project |
| **Knowledge & Retrieval** | Javier Martinez · Maclay Teefey · Pratik Sharma | All three corpora — runbooks and policy, laptop manuals, closed-ticket resolutions. Sourcing, chunking, index schema and filterable fields, `device_model` filtering, hybrid retrieval with the semantic ranker, reranker threshold calibration, and the retrieval tools the agent calls |
| **Identity & Control** | Anthony Huggins · Adrian Otieno · Christopher Lee | The closed action enum, the Graph executors with their idempotency keys, the policy gate, the gated-set test, **the entitlement MCP server** — its tools and its caller resolution — and **PostgreSQL**: schema, migrations, the repository module, and the seeded analysts and grants that give the server something to deny |
| **Edge & Approvals** | Stanley Liu · Ralph Complido · Eric Gill | `/tickets/ingest` and the intake pipeline — signature validation, deduplication, redaction, Prompt Shields, requester resolution — plus HubSpot replies and ticket updates, both approval endpoints, the durable pending-approval records, the Power Automate contract, and expiry |
| **Platform & Quality** | Ta'Shawn Deshazier · Arnold Epanda · Johnny Huynh | Azure resources and Foundry deployments — **AI Search and Document Intelligence first**, because they are the only provisioning another team waits on — Key Vault, Container Apps, GitHub Actions with OIDC across three environments, the in-repo fakes, OpenTelemetry and run records and cost accounting, then the CI evaluation tier, the golden ticket set, the injection fixtures and the demo tickets |

Two things the table does not show. **Knowledge & Retrieval and Platform & Quality share no members**,
because § 7 requires the golden cases to be written by someone who did not tune retrieval. And
`ApprovalRecord` is the interface between Identity & Control, which owns the policy gate, and Edge &
Approvals, which owns the durable round trip — the control plane is split across those two on purpose.

Team leads, and how work is split inside a team, are the teams' own to settle on day 1.

**Day one, per team.** Every team starts with a full day of work that needs no Azure, no corpus and
no Graph consent. Nothing below waits on anything else.

| Team | Day 1 |
|---|---|
| **Orchestration** | The six typed models plus the index schema, and the freeze · graph skeleton · the selection function, written as a pure function and unit tested with no model in the loop · the join |
| **Knowledge & Retrieval** | Chunk the delivered laptop-manual corpus — `corpus/manuals/text/` is nine markdown files, real content on day 1 · the structure-aware chunker and the stable chunk-id scheme · the index schema and a fake retrieval client the workers can code against · assemble the runbook and policy material into `corpus/MANIFEST.md` |
| **Identity & Control** | PostgreSQL schema, migrations and the repository module against local Docker · the action enum · the policy gate as pure functions · the MCP skeleton · the Graph fake |
| **Edge & Approvals** | The ingest receiver against § 6.1's tested payload contract · HMAC verification over raw bytes · deduplication · the intake pipeline · HubSpot and Power Automate fakes |
| **Platform & Quality** | Provisioning, **AI Search and Document Intelligence first** · the OIDC pipeline · `docker compose` with local Postgres · the shared fakes library |

**The first three days decide whether the rest converges.**

- **Day 1 — the typed contracts are frozen in a single pull request, before any team builds against
  them.** Six models — `Ticket`, `Plan`, `SubRequest`, `ProposedAction`, `ApprovalRecord`, `RunRecord`
  — plus the index schema are the interfaces between all five teams, and everything else is downstream
  of them. Contracts that land on day 4 cost the week.

  Two fields are easy to leave out on day 1 and expensive to add on day 5, once five teams have built
  against the frozen type:

  - **`ProposedAction.preconditions`** — the tool calls and expected values that established the action
    is warranted. Re-validation is then "re-run these calls and compare", not a judgment call, and
    § 7's world-changed test becomes writable.
  - **`ProposedAction.depends_on`** — the action this one follows, which is what makes the provisioning
    chain in § 4.2 orderable.
- **Day 1 — in-repo fakes for Microsoft Graph, HubSpot and the Power Automate flow.** No team waits on
  tenant access, an app registration, or a provided integration that is not wired up yet. This is the
  highest-leverage day in the project.
- **Day 3 — a walking skeleton runs end to end.** Webhook to a stub agent that always returns one
  unlock, to the gate, to a stub executor, to a ticket update, with every external system faked. Each
  team then fills in its own box. Without it the integration cliff arrives on day 8 and the day 10
  presentation becomes a description of a system rather than a system.

**Presentation.** Day 10 is the demonstration, not a build day. The nine build days have to end with a
system that can be shown end to end rather than described: a ticket that resolves on the entitlement
check alone, a ticket that parks on a gated action until someone approves it, and a ticket that is
declined with its reason — all three run live. Plan the ninth day around having those three tickets
working, not around landing one more capability.

---

## 9. Deliverables

1. **The repository** — the workflow application, the entitlement MCP server, the ingestion pipeline,
   the repository module, the executors, the evaluation suite, tests, Dockerfiles, compose file, CI
   workflow, pinned dependencies, and a README operations section.

2. **Architecture document** — a reference, not an essay:
   - The topology, and **why this shape and not the framework's sequential, concurrent, group-chat,
     handoff or magentic orchestrations** — one line each. This is the section that has to hold the
     line § 3.4 draws.
   - A decisions table: every bound with its chosen value and unit, the model tier per agent, the
     reranker threshold with the method used to choose it, and the pinned Agent Framework versions.
   - A degraded-modes table.
   - What was cut, and why.
   - A threat and responsible-AI note: trust boundaries with a mitigation or an explicitly accepted
     risk at each. Name the accepted risks, including the sender-identity dependency on the mail
     transport and the approval-flow connection secret.

3. **Evaluation report** — the golden set, per-category results, the reranker threshold and how it was
   chosen, both judged runs with the delta, every adversarial case, and cost and latency **measured
   from the run records** rather than estimated.

4. **Demonstration artifacts** — five committed files, not screenshots of a terminal that has since
   scrolled away:
   - **The multi-lane contrast** — the run record of a three-lane ticket beside a one-lane ticket.
   - **The out-of-order approval** — two lanes whose approvals return minutes apart, with the second
     re-validating against state the first changed.
   - **Indirect-injection resistance** — the transcript against the poisoned ticket, with the Prompt
     Shields event and the unchanged plan both visible.
   - **The grounded-versus-ungrounded contrast** — both transcripts from § 7's first adversarial case.
   - **The MCP server driven from an external client** — a recording of a second host listing the
     tools and calling one, **plus the server-side log line** showing the call was authorized as that
     caller rather than as the workflow.

5. **Live demo, 5–7 minutes** — one ticket end to end with a citation resolved to its chunk; the
   multi-lane contrast; and a gated action parked on an approval while an ungated one on the same
   ticket has already run.

---

## 10. Acceptance Checklist

**Architecture**
- ☐ The Agent Framework workflow layer carries the topology — executors and typed edges, not
  hand-rolled `asyncio`; no third-party framework on the critical path
- ☐ The Coordinator decomposes: a multi-request email produces multiple lanes, a single-request email
  produces one, and the run record says which workers ran and why
- ☐ The fan-out width comes from a selection function over the typed plan, and that function is unit
  tested with no model in the loop
- ☐ The join is hand-written, counts against the Coordinator's ordered list, and sits after execution
- ☐ Workers loop on their own tools — a fixed one-call-each shape is a fail
- ☐ Lanes are independent: one declines while another executes, and a failure in one cancels nothing

**Determinism and approval**
- ☐ Every gated action traces to a matching approval record, checked at the executor and not only at
  the graph
- ☐ The gated set is a closed enum in code; the model has no say in membership
- ☐ An approved action is re-validated against live state before it executes, and a moved precondition
  narrows or withdraws it
- ☐ A decision arriving for an expired or already-decided record is refused
- ☐ Every loop has a structured termination condition and an independent hard cap; bounds are per lane
  and the cost ceiling is per ticket

**Retrieval**
- ☐ Refusal fires on `@search.rerankerScore` below a threshold chosen from the golden set, with the
  value, the method and which score it sits on all reported
- ☐ Multi-hop chains from `corpus/MANIFEST.md` are followed deliberately, not stumbled into
- ☐ A golden case exists for every declared distractor
- ☐ Out-of-corpus questions refuse; near-miss questions do not
- ☐ Every manual query filters on `device_model`; an unfiltered one is a defect
- ☐ A symptom the corpus cannot address for the requester's model escalates rather than borrowing a
  near-identical model's procedure — "my Latitude 5550 won't turn on" is the case to run
- ☐ Manuals are cracked with Document Intelligence and tables are retained rather than flattened
- ☐ *Stretch* — one of the two named table failures in `corpus/MANIFEST.md` § 6 is recovered

**Security**
- ☐ Keyless end to end apart from the one documented exception in § 2.4
- ☐ No tool takes its subject from model output; the MCP server resolves the caller itself
- ☐ The MCP server is driven by an external client, with the server-side authorization log line shown
- ☐ A requester holding no grant over a target gets a structured denial, not an empty result — proven
  in both directions against seeded grants
- ☐ Indirect injection through a ticket body is tested and resisted

**Delivery**
- ☐ Run records cover every agent, tool, retrieval, gate decision, approval and execution, PII-redacted
- ☐ The deterministic eval tier gates the build; a cost budget with alerts exists
- ☐ `docker compose up` works on a fresh clone; both services deploy to ACA by digest on managed
  identity
- ☐ Cost per ticket and demo latencies reported as measured numbers
- ☐ Architecture document, evaluation report, five demonstration artifacts, rehearsed demo
