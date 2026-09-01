"""Financial-crime alert desk, built on WorkflowBuilder.

Every edge carries a type declared in this module.

WHAT THIS IS
    A cyclic multi-agent graph that works one monitoring alert. Five nodes, one loop:

        triage --(multi-selection edge)--> sanctions --+
              ^                            history   --+--> review --> output
              |                            kyc_check --+       |
              +------------------ cycle ---------------------- +

    triage       decides WHICH specialists this alert warrants - a SUBSET, chosen
                 per alert by the model, so the fan-out width is not in the code.
    specialists  run in parallel inside one superstep, each answering the same
                 focus question from its own angle with its own tool.
    review       owns the join (it counts arrivals against what triage ordered),
                 owns the loop's memory, and picks one of three exits:
                     "more"    -> a follow-up prompt back to triage (the cycle)
                     "approve" -> park the graph and wait for a HUMAN
                     "done"    -> yield the disposition and stop
                 MAX_ROUNDS is the backstop behind all three.

THE FOUR THINGS A NAMED BUILDER CANNOT SAY, AND WHERE THEY LIVE HERE
    a fan-out the model sizes    select_checks + TriagePlan.checks
    a join over a dynamic width  Review.handle, counting against state
    an edge that points back     builder.add_edge(review, triage)
    a pause for a person         ctx.request_info + @response_handler

THREE MEMORIES, THREE LIFETIMES - conflating them is the classic mistake
    the AGENT's    AgentSession(session_id=f"alert:{id}"), compacted by the
                   framework's compaction_strategy. Triage's own thread.
    the WORKFLOW's ctx.set_state(f"alert:{id}:summary"), namespaced by alert id,
                   carried into the checkpoint.
    the LOOP's     Review._window / _l1 / _l2 - the ladder in _remember(), which
                   is code no framework writes for you, because findings from
                   three specialists on three threads are not a conversation.
    And one rule over all of them: compress content, NEVER compress control state.
    _consulted and Finding.available stay structural because branches read them.

READING ORDER - the file is the four steps of building a graph
    Step 1  DECLARE the types that travel the edges
    Step 2  WRITE the executors that consume and emit those types
    Step 3  WIRE them into a graph
    Step 4  BUILD it - and run it from run_desk.py / hold.py / resume.py
    Everything above Step 1 is plumbing: the corpus, the tools, the tool guard.

    NOTE: this file must not use `from __future__ import annotations`. The
    framework resolves @response_handler's annotations at runtime, and with that
    import they are strings - `WorkflowContext[Never, str]` then fails at import.
"""

import difflib
import json
import os
import sys
from dataclasses import dataclass
from functools import wraps
from pathlib import Path
from typing import Any, Literal, Never

from agent_framework import (
    AgentSession,
    ContextWindowCompactionStrategy,
    Executor,
    FileCheckpointStorage,
    FileSessionStore,
    Message,
    SummarizationStrategy,
    WorkflowBuilder,
    WorkflowContext,
    executor,
    handler,
    response_handler,
    tool,
)
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv
from pydantic import BaseModel

# Windows consoles default to cp1252 and gpt-5 emits en-dashes and non-breaking
# hyphens. Without this, print() dies AFTER a successful API call. Note it cannot
# reach inside the checkpoint writer - that one needs PYTHONUTF8=1 in the env.
sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

# The entire corpus - alerts, watchlist, transactions, customers - is one static
# JSON file read once at import. There is no external system behind these tools,
# which is exactly why REVIEWER_INSTRUCTIONS has to say so in words.
DATA = json.loads((Path(__file__).parent / "alerts.json").read_text(encoding="utf-8"))

# The checks this desk can order. The review node needs this set in Part 3.
SPECIALISTS = {"sanctions", "history", "kyc_check"}

# Tools append here when they cannot complete. The specialist reads it after the
# agent run, so an outage is a fact we OBSERVED rather than a phrase we hoped to
# spot in the model's prose.
TOOL_ERRORS: list[str] = []

# The loop's own budget. Distinct from WorkflowBuilder(max_iterations=...), which
# is a superstep backstop for the whole graph, not a decision this desk makes.
MAX_ROUNDS = 4

# How many findings the review node keeps verbatim before compressing older ones.
WINDOW = 2
# How many level-1 notes accumulate before they are folded into one level-2 summary.
# Both numbers are deliberately aggressive so both tiers fire inside four rounds;
# in production a window of 2 would summarise findings the reviewer still needs.
L1_BEFORE_L2 = 1

# Two stores, two questions: "what has this workflow done" and "what does this
# agent remember saying". Kept beside the file rather than in a system temp dir so
# `ls checkpoints` and `ls sessions` are one command away during the demo.
CHECKPOINT_DIR = Path(__file__).parent / "checkpoints"
SESSION_DIR = Path(__file__).parent / "sessions"


def guarded(fn):
    """Catch a tool's failure, record it, and hand the model a plain explanation."""

    @wraps(fn)  # keeps name/signature/docstring, so @tool's generated schema is still correct
    def wrapper(*args: Any, **kwargs: Any) -> str:
        try:
            return fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001 - a tool outage is data, not a crash
            # One failure, two audiences: TOOL_ERRORS is read by our code to set
            # Finding.available, the returned string is read by the model so it
            # describes the outage instead of inventing a result. Without this the
            # framework's own handling makes an outage a log line and nothing else.
            TOOL_ERRORS.append(f"{fn.__name__}: {exc}")
            return f"TOOL ERROR - {fn.__name__} is unavailable: {exc}"

    return wrapper


# The four tools. @tool reads the signature and the DOCSTRING to generate the JSON
# schema the model reasons over - so the docstring is not documentation, it is the
# description. Decorator order matters: @tool outside, @guarded underneath, so
# @tool describes the real function rather than the wrapper.
# Our own code calls the undecorated function through .func - use the tool when the
# MODEL should decide whether to call it, .func when WE have already decided.
@tool
@guarded
def get_alert(alert_id: str) -> str:
    """Return the raw monitoring alert for an alert id."""
    for a in DATA["alerts"]:
        if a["alert_id"] == alert_id:
            return json.dumps(a)
    return f"No alert {alert_id}."


@tool
@guarded
def screen_watchlist(name: str) -> str:
    """Screen a counterparty name against sanctions and watchlists. Returns fuzzy matches."""
    # An empty name is a sentence, not an exception. Some alerts have no
    # counterparty at all, and the interesting behaviour is a triage agent that
    # DECLINES to order this check - not a tool that copes with a pointless question.
    if not name:
        return "No name supplied - the monitoring system did not resolve a counterparty."
    hits = []
    for w in DATA["watchlist"]:
        # Name screening in the wild is fuzzy matching against a list, and the
        # interesting cases score ~0.90: high enough to stop you, not high enough
        # to act on. This corpus is built to produce that band.
        score = difflib.SequenceMatcher(None, name.lower(), w["name"].lower()).ratio()
        if score > 0.80:
            hits.append({"name": w["name"], "list": w["list"], "program": w["program"],
                         "score": round(score, 3)})
    hits.sort(key=lambda h: -h["score"])
    return json.dumps(hits[:5]) if hits else f"No watchlist match above 0.80 for {name!r}."


@tool
@guarded
def transaction_history(customer_id: str) -> str:
    """Return prior transactions for a customer id."""
    rows = [t for t in DATA["transactions"] if t["customer_id"] == customer_id]
    return json.dumps(rows[:12]) if rows else f"No prior transactions for {customer_id}."


@tool
@guarded
def kyc_record(customer_id: str) -> str:
    """Return the KYC record for a customer id. Fields may be missing or stale."""
    for c in DATA["customers"]:
        if c["customer_id"] == customer_id:
            return json.dumps(c)
    return f"No KYC record for {customer_id}."


#####
# Step 1, DECLARE the types that will travel your graph
#
# Own your edge types. Every message crossing an edge is declared here, and three
# things follow: routing code compares plain fields with no model in the loop, so
# it is unit-testable; the graph reads as data flow; and the checkpointer can
# serialise the message queue, because nothing on it is somebody else's SDK object.
#
# Two shapes, two jobs. A BaseModel is an AGENT's output contract - it becomes the
# JSON schema the model is constrained to. A @dataclass is a MESSAGE on an edge -
# nothing validates it and no model ever sees it.
#####
class TriagePlan(BaseModel):
    """Structured output from the triage agent: WHICH checks this alert warrants."""

    # The model picks a SUBSET, and the `list` is the whole point: a bare Literal
    # would be a ROUTER - one choice, one target. A list of literals is a
    # SELECTION. That is the difference between routing and fan-out, and it is one
    # word in a type annotation. This field is the fan-out width, and it is not in
    # the code.
    checks: list[Literal["sanctions", "history", "kyc_check"]]
    # One question the ordered specialists each answer from their own angle.
    focus: str
    rationale: str


class ReviewDecision(BaseModel):
    """Structured output from the review agent."""

    #             re-triage    HitL        output
    next: Literal["more", "approve", "done"]
    rationale: str
    # Only meaningful when next == "approve": the irreversible step a human signs.
    action: str = ""


@dataclass
class Plan:
    # travels triage -> specialists
    alert_id: str
    checks: list[str]
    focus: str


@dataclass
class Finding:
    # travels specialist -> review
    alert_id: str
    source: str
    text: str
    # False when the specialist could not complete its check. The review node
    # routes on this field rather than on the prose - anything the control flow
    # depends on must be structural.
    available: bool = True


@dataclass
class ApprovalRequest:
    # travels review -> human, via ctx.request_info
    alert_id: str
    action: str
    rationale: str


@dataclass
class ApprovalDecision:
    # travels human -> review, via run(responses=...), landing in Review.on_human
    approved: bool
    note: str


#####
# Step 2, WRITE the executors that consume and emit those types
#
# An executor is a node. A @executor function is one input type and no state.
# Subclass Executor when the node needs multiple handlers, instance fields, or the
# checkpoint hooks: TriageNode is a class because it takes two input types, Review
# because it must remember, the specialists are functions because they need neither.
# A @handler is selected by the TYPE of its first parameter.
#####
class TriageNode(Executor):
    """Decide which checks this alert warrants, and emit them as a Plan."""

    def __init__(self, agent, alert_id: str, session):
        # The id is the node's identity in the graph: it appears in every error
        # message, and it is what a checkpoint matches against when a DIFFERENT
        # process rebuilds the graph. Change an id and old checkpoints stop loading.
        super().__init__(id="triage")
        self._agent = agent
        self._alert_id = alert_id
        self._session = session

    @handler
    async def from_prompt(self, prompt: str, ctx: WorkflowContext[Plan]) -> None:
        # ctx state is the GRAPH's shared scratchpad, and it is SYNCHRONOUS - no
        # await. Everything else on the context is awaited; get this wrong and you
        # store a coroutine as your state, which fails much later somewhere else.
        ctx.set_state("alert_id", self._alert_id)
        # Read the case summary back out of state. THIS is what makes the namespace
        # load-bearing: get the key wrong and you read another case's summary
        # straight into this case's reasoning. Written by Review._remember, one
        # superstep earlier - state crosses the barrier, not the same step.
        carried = ctx.get_state(f"alert:{self._alert_id}:summary")
        if carried:
            prompt = f"{prompt}\n\nWhat this desk already knows: {carried}"
        # The agent's own thread for this case. The executor keeps no conversation
        # of its own, so this session is what makes round 2 remember round 1.
        out = await self._agent.run(prompt, session=self._session)
        plan = TriagePlan.model_validate_json(out.text)
        # Not defensive clutter: an empty list means no specialist runs, no Finding
        # is ever delivered, and the workflow goes quietly idle with no output and
        # no error. The framework will not stop you, so the guarantee is made here,
        # where the list is produced - and again in select_checks. Two belts.
        checks = [c for c in plan.checks if c in SPECIALISTS] or ["kyc_check"]
        # The join needs to know what was ordered or it cannot tell a complete round
        # from a partial one. State is how Review finds out.
        ctx.set_state(f"alert:{self._alert_id}:ordered", checks)
        print(f"  [triage] ordered {checks} - {plan.rationale[:80]}")
        print(f"           focus: {plan.focus}")
        await ctx.send_message(Plan(self._alert_id, checks, plan.focus))

    @handler
    async def from_messages(self, messages: list[Message], ctx: WorkflowContext[Plan]) -> None:
        # An executor declares one handler per input type it accepts. The review
        # node sends a str; Workflow.as_agent() (see desk_as_agent.py) sends
        # list[Message], and the start executor has to accept it or as_agent()
        # raises at build time. Not speculative - it is what Part 7 runs on.
        await self.from_prompt(messages[-1].text or "", ctx)


def make_specialist(node_id: str, agent):
    """One specialist node: answer the round's focus question, emit a Finding."""

    @executor(id=node_id)
    async def specialist(p: Plan, ctx: WorkflowContext[Finding]) -> None:
        # Clear before the run so what we read afterwards belongs to THIS round.
        # A module-level list is enough because each specialist awaits its own
        # agent; where that is not true, key it by executor id.
        TOOL_ERRORS.clear()
        alert = json.loads(get_alert.func(p.alert_id))
        # Hand the ids over RESOLVED. Extracting them from a JSON blob is a
        # string-parsing task, and a model that gets it wrong asks the tool a
        # question nobody wanted answered - and gets a clean, confident, wrong
        # answer back that nothing in the system can detect.
        out = await agent.run(
            f"Alert {p.alert_id}.\n"
            f"customer_id = {alert['customer_id']}\n"
            f"counterparty = {alert.get('counterparty')!r}\n"
            f"Full record: {json.dumps(alert)}\n\n"
            f"Question: {p.focus}"
        )
        text = out.text.strip()
        # Did any tool actually fail during that run? A specialist whose tool was
        # down has not answered its question, however confident its prose sounds.
        available = not TOOL_ERRORS
        if not available:
            # Say it in the finding text too, so the reviewer's context carries the
            # outage rather than reading a thin answer as a clean result.
            text = f"TOOL UNAVAILABLE - {'; '.join(TOOL_ERRORS)}. Agent said: {text}"
        print(f"  [{node_id}] {text[:110]}")
        await ctx.send_message(Finding(p.alert_id, node_id, text, available=available))

    return specialist  # factory: the same function, a different agent bound


class Review(Executor):
    """Holds the loop's memory and decides whether to continue, escalate, or stop.

    A function executor has nowhere to keep state across rounds, which is why this
    one is a class. It also owns the join, the memory ladder, and the human gate.
    """

    def __init__(self, decide_agent, summarize_agent, max_rounds: int = MAX_ROUNDS):
        super().__init__(id="review")
        self._decide = decide_agent
        self._summarize = summarize_agent
        self._max = max_rounds
        self._round = 0
        # Tier 1 - findings kept VERBATIM, capped at WINDOW. The reviewer needs
        # detail to judge what just arrived.
        self._window: list[str] = []
        # Tier 2 - one sentence per evicted finding.
        self._l1: list[str] = []
        # Tier 3 - one paragraph folded from the L1 notes, and the only tier that
        # outlives the run: it goes to state, triage reads it back, it survives
        # into the checkpoint. Whatever the summariser drops is genuinely forgotten.
        self._l2: str = ""
        # Findings arriving this round, held until every ordered specialist reports.
        self._batch: list[Finding] = []
        # Which specialists have reported. Kept STRUCTURALLY, not in prose. It looks
        # redundant next to _window - the source is right there in the string - and
        # it is not: the moment findings are summarized, the prose survives and the
        # list of who spoke dissolves into it. Control flow reads this. Never
        # summarize it.
        self._consulted: set[str] = set()
        # Which of them could not complete. Same reason: "sanctions errored" must
        # never reach the reviewer as "sanctions is clear".
        self._unavailable: set[str] = set()

    def _context(self) -> str:
        """Assemble the reviewer's prompt: the ladder, bottom tier first."""
        # Naming what is LEFT is what stops the reviewer choosing "more" forever.
        # Paired with the reviewer's "once all three have reported you must choose",
        # this line is what actually terminates the loop in the normal case.
        remaining = sorted(SPECIALISTS - self._consulted)
        parts = [
            f"Specialists already consulted: {', '.join(sorted(self._consulted)) or 'none'}.",
            f"Specialists not yet consulted: {', '.join(remaining) or 'NONE - all are spent, you must decide now'}.",
        ]
        if self._unavailable:
            parts.append(f"Specialists whose tools were UNAVAILABLE: {', '.join(sorted(self._unavailable))}.")
        # Oldest and most compressed first, freshest and most detailed last.
        if self._l2:
            parts.append(f"Case summary so far: {self._l2}")
        if self._l1:
            parts.append("Earlier notes:\n" + "\n".join(f"- {n}" for n in self._l1))
        parts.append("Most recent findings:\n" + "\n".join(self._window))
        return "\n\n".join(parts)

    async def _remember(self, ctx: WorkflowContext, alert_id: str, f: Finding) -> None:
        """Record one finding, and pay the compression cost when a tier overflows."""
        self._window.append(f"[{f.source}] {f.text}")
        self._consulted.add(f.source)
        # Evict past the window: each evicted finding becomes one sentence.
        while len(self._window) > WINDOW:
            evicted = self._window.pop(0)
            note = await self._summarize.run(f"Compress to one sentence:\n{evicted}")
            self._l1.append(note.text.strip())
            print(f"  [memory] evicted 1 finding -> L1 note ({len(self._l1)} held)")
        # Fold the sentences into the paragraph. Note "Existing summary:" below -
        # L2 is regenerated from ITSELF plus the new notes, which is what makes this
        # hierarchical summarization rather than a rolling digest.
        if len(self._l1) > L1_BEFORE_L2:
            rolled = await self._summarize.run(
                "Fold these notes into one paragraph, keeping every concrete fact:\n"
                + (f"Existing summary: {self._l2}\n" if self._l2 else "")
                + "\n".join(f"- {n}" for n in self._l1)
            )
            self._l2 = rolled.text.strip()
            self._l1 = []
            print(f"  [memory] L1 notes folded -> L2 case summary ({len(self._l2)} chars)")
        # Namespaced by alert id. This prefix is the whole of context-bleed
        # prevention - no feature, no API, just a string. Triage reads this key back.
        ctx.set_state(f"alert:{alert_id}:summary", self._l2 or " ".join(self._l1))
        ctx.set_state(f"alert:{alert_id}:rounds", self._round)

    @handler
    async def handle(self, f: Finding, ctx: WorkflowContext[str, str]) -> None:
        # WorkflowContext[str, str]: the first type is what this node may
        # send_message (a str, back to triage), the second what it may yield_output.
        # Two parameters because this node is interior or terminal depending on what
        # the model decides. The framework validates both at build time.
        #
        # THE JOIN. Called once per Finding; every ordered specialist sends here.
        # add_fan_in_edges cannot do this: it flushes only when EVERY declared
        # source has produced, and our fan-out activates a subset, so a specialist
        # that never ran never fills its buffer, the predicate is never true, and
        # the workflow goes idle with no output and no error. A dynamic fan-out
        # needs a join you own - so we count against the list triage wrote to state.
        self._batch.append(f)
        ordered = ctx.get_state(f"alert:{f.alert_id}:ordered") or []
        if len(self._batch) < len(ordered):
            print(f"  [review] holding {len(self._batch)}/{len(ordered)}")
            return

        # Round complete: take the batch, reset the buffer for the next lap.
        batch, self._batch = self._batch, []
        self._round += 1
        for finding in batch:
            # Pass `finding`, NOT `f`. On a multi-specialist round `f` is whichever
            # finding happened to arrive last, so using it here records one finding
            # twice and drops the other - and _consulted then reports a specialist
            # as unconsulted after it has already answered.
            await self._remember(ctx, finding.alert_id, finding)
            if not finding.available:
                self._unavailable.add(finding.source)
        context = self._context()
        print(f"  [review] round {self._round}/{self._max} closed on "
              f"{sorted(x.source for x in batch)}, context {len(context)} chars")

        if self._round >= self._max:
            # Termination as a decision we make, not a crash we allow. This exits
            # with a disposition an analyst can file and exit code 0; letting
            # max_iterations fire instead raises WorkflowConvergenceException -
            # exit 1, no disposition, and a failed event whose data is None.
            await ctx.yield_output(
                f"{f.alert_id}: HALTED at the round budget after {self._round} rounds.\n{context}"
            )
            return

        out = await self._decide.run(f"{context}\n\nDecide the next step for alert {f.alert_id}.")
        d = ReviewDecision.model_validate_json(out.text)
        print(f"  [review] next={d.next} - {d.rationale[:90]}")

        # The three exits. Only "more" sends a message onward; the other two end
        # this branch - one by parking for a person, one by yielding a disposition.
        if d.next == "approve":
            # request_info does NOT block. This executor returns, the workflow emits
            # a request_info event and goes idle with a pending request recorded.
            # Nothing holds a thread, a connection or a coroutine open: an idle
            # workflow with a pending request is a STATE, not a PROCESS - which is
            # exactly what makes hold.py / resume.py possible.
            await ctx.request_info(
                request_data=ApprovalRequest(f.alert_id, d.action or "release funds", d.rationale),
                response_type=ApprovalDecision,
            )
        elif d.next == "more":
            # The cycle. The follow-up names what is already known and what is still
            # open, so triage orders a NARROWER second round rather than repeating
            # the first. Deliberately weaker than a blocklist: sometimes the right
            # second round IS the same specialist with a different question - a near
            # miss at 0.978 is answered by asking sanctions about aliases, and that
            # question does not exist until the first answer arrives.
            await ctx.send_message(
                f"Follow-up round for alert {f.alert_id}. Already reported: "
                f"{', '.join(sorted(self._consulted))}. "
                f"Order only the checks that can still close this gap: {d.rationale}"
            )
        else:
            await ctx.yield_output(f"{f.alert_id}: CLOSED after {self._round} round(s). {d.rationale}")

    @response_handler
    async def on_human(
        self,
        original_request: ApprovalRequest,
        response: ApprovalDecision,
        ctx: WorkflowContext[Never, str],
    ) -> None:
        # Where the run RESUMES after request_info parked it - possibly in another
        # process, days later. Matched by TYPE ANNOTATIONS, not by name: the
        # framework reads ApprovalRequest/ApprovalDecision and routes the reply
        # here, so several gates in one executor each get their own handler.
        # WorkflowContext[Never, str] says "I never send, I only yield" - Never in
        # the first slot declares this node terminal on this path.
        #
        # Fail-safe: anything that is not an explicit approval is a denial. A
        # malformed reply, a missing field, a None - all deny. The failure mode of
        # an approval gate must be REFUSE, and refuse by construction rather than
        # because the happy path happened to be taken.
        approved = bool(getattr(response, "approved", False))
        verdict = "APPROVED" if approved else "DENIED"
        await ctx.yield_output(
            f"{original_request.alert_id}: {verdict} - {original_request.action}. "
            f"Reviewer note: {response.note}"
        )

    async def on_checkpoint_save(self) -> dict[str, Any]:
        # A checkpoint captures workflow state and the message queue. It does NOT
        # reach inside your executors. Without these two hooks a resumed graph
        # starts at round 0 with an empty window and re-investigates a case it has
        # already finished - and nothing warns you, because from the framework's
        # side nothing went wrong.
        #
        # sorted() because a set is not JSON-serialisable: return one and the
        # checkpoint write fails as a WARNING, so the run continues and the
        # durability silently is not there.
        return {"round": self._round, "window": self._window, "l1": self._l1,
                "l2": self._l2, "consulted": sorted(self._consulted),
                "unavailable": sorted(self._unavailable)}

    async def on_checkpoint_restore(self, state: dict[str, Any]) -> None:
        # Every field the save hook wrote, restored to the type the code expects.
        self._round = state.get("round", 0)
        self._window = state.get("window", [])
        self._l1 = state.get("l1", [])
        self._l2 = state.get("l2", "")
        self._consulted = set(state.get("consulted", []))
        self._unavailable = set(state.get("unavailable", []))


def select_checks(message: Any, target_ids: list[str]) -> list[str]:
    """Activate only the specialists triage ordered.

    A selection_func is ordinary code: it receives the message and every declared
    target id, and returns the subset to run. They run together, in one superstep.

    Note the fallback. Unlike a switch-case group, which the framework refuses to
    build without exactly one Default, nothing here forces exhaustiveness - return
    an empty list and no target fires at all. Exhaustiveness is ours to guarantee.
    """
    # Not paranoia: a selection function sees every message on its edge group, and
    # a graph that grows will eventually send something else down it. Returning all
    # targets fails OPEN, which is right for a screening desk and wrong for
    # something that spends money.
    if not isinstance(message, Plan):
        return list(target_ids)
    wanted = [t for t in target_ids if t in message.checks]
    # target_ids[0] is deterministic rather than arbitrary: the list is built from
    # SPECIALIST_SPECS in insertion order.
    return wanted or [target_ids[0]]


def make_client():
    # AzureCliCredential means auth comes from `az login` - no keys in this file.
    # The caller owns the credential and must close it.
    # (The lecture names these PROJECT_ENDPOINT / MODEL_DEPLOYMENT_NAME; this repo's
    # .env already uses the AZURE_* names below.)
    credential = AzureCliCredential()
    client = FoundryChatClient(
        project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        credential=credential,
    )
    return client, credential


def make_storage() -> FileCheckpointStorage:
    """Where the GRAPH's state lives between processes."""
    return FileCheckpointStorage(
        CHECKPOINT_DIR,
        # module:qualname. These are the types that travel our edges.
        # FileCheckpointStorage uses a RESTRICTED UNPICKLER: only a built-in safe
        # set plus what is named here can be deserialized. A dataclass defined in
        # the script you LAUNCH has the qualname "__main__:Finding", so it works in
        # that process and fails in every other one. Defining the types in an
        # imported module is not style - it is what makes cross-process resume work.
        allowed_checkpoint_types=[
            "desk:Plan",
            "desk:Finding",
            "desk:ApprovalRequest",
            "desk:ApprovalDecision",
        ],
    )


def make_session_store() -> FileSessionStore:
    """Where TRIAGE's conversation lives between processes.

    A different file from the checkpoint, holding a different thing: the checkpoint
    restores the graph, this restores what the agent remembers saying. Restore one
    without the other and you get a graph that resumes correctly with an agent that
    has amnesia.

    Three methods - get / set / delete - and it emits an ExperimentalWarning on
    first use. The file is named after the base64'd session id, so do not go
    looking for alert-AML-8807.json.
    """
    return FileSessionStore(SESSION_DIR)


def opening_prompt(alert_id: str) -> str:
    # The message that starts the graph. It lands on the start executor (triage),
    # whose from_prompt handler takes a str - the same shape review sends on a
    # "more" lap.
    return f"Alert {alert_id}. Record: {get_alert.func(alert_id)}"


# The prompts, all four in one place. Nothing here is graph code: it is the English
# that makes the graph behave, and it is the part worth reading closely.
TRIAGE_INSTRUCTIONS = (
    "You triage financial-crime alerts and decide WHICH checks to order. "
    "The three available checks are 'sanctions' (screens a counterparty NAME "
    "against watchlists), 'history' (prior transaction patterns for the "
    "customer) and 'kyc_check' (customer due diligence file). "
    # <<< this sentence is why triage orders two checks at once instead of one at a time
    "The checks you order RUN IN PARALLEL, so ordering three costs the same "
    "wall-clock time as ordering one. Order every check whose answer could "
    "change this alert's disposition in THIS round. "
    "Two rules override that. First: never order a check that cannot be "
    # <<< and this one is why AML-8815 declines the sanctions check entirely
    "answered - in particular, never order 'sanctions' when the alert's "
    "counterparty is null, missing or empty, because there is no name to "
    "screen. Second: when the alert rule names the problem and ONE check "
    "settles it outright, order that check alone. "
    "'focus' is the single question the ordered checks must answer. "
    "On a follow-up round, order only what is still open."
)

REVIEWER_INSTRUCTIONS = (
    "You are a financial-crime desk reviewer. This desk has exactly three "
    # <<< without these two sentences the reviewer demands registry data that does
    # <<< not exist in this corpus, chooses 'more' forever, and spends every round
    "specialists: sanctions, history, kyc_check. There is no other source of "
    "information and no way to obtain external registry data. "
    "Choose 'more' ONLY if a specialist you have NOT yet consulted could close a "
    # <<< paired with the "not yet consulted: NONE" line _context injects, this is
    # <<< what actually terminates the loop; MAX_ROUNDS is only the backstop
    "material gap. Once all three have reported, you must choose 'approve' or 'done'. "
    # <<< and this sentence is the entire human-in-the-loop policy: IRREVERSIBILITY,
    # <<< not confidence, is what decides whether a person is pulled in
    "Choose 'approve' when the disposition moves money, files a report, or is "
    "otherwise irreversible - a human must sign it, and 'action' names that step. "
    "Choose 'done' when the case resolves with no irreversible action. "
    "Never ask for data this desk cannot obtain."
)

SUMMARISER_INSTRUCTIONS = "You compress investigative findings. Keep concrete facts, drop hedging."

# All three specialists are the SAME executor with a different agent bound. A dict
# makes that symmetry visible, and a fourth check would be one more entry. The keys
# are the SPECIALISTS set from the top of the file.
SPECIALIST_SPECS = {
    "sanctions": dict(
        name="sanctions",
        # Both endings are load-bearing. "Never ask for data you were not given"
        # stops a specialist answering with a question, which in a fan-out means a
        # Finding containing no finding. "Three sentences maximum" is a token budget
        # - these answers accumulate in the review node's memory for the whole case.
        instructions=("You screen counterparties against sanctions lists. Call screen_watchlist "
                      "with the counterparty value you were given. A score of 0.95 or above is a "
                      "TRUE MATCH; below that is a NEAR MISS. Report what the tool returned and "
                      "stop. Never ask for data you were not given. Three sentences maximum."),
        tools=[screen_watchlist],  # one tool each, so a specialist cannot wander
    ),
    "history": dict(
        name="history",
        instructions=("You analyse transaction history. Call transaction_history with the "
                      "customer_id you were given. State whether the alerted payment fits the "
                      "prior pattern. Report what the tool returned and stop. Never ask for data "
                      "you were not given. Three sentences maximum."),
        tools=[transaction_history],
    ),
    "kyc_check": dict(
        name="kyc",
        instructions=("You review customer due diligence. Call kyc_record with the customer_id "
                      "you were given. Flag stale refresh dates, null or missing fields, and PEP "
                      "status. Report what the tool returned and stop. Never ask for data you "
                      "were not given. Three sentences maximum."),
        tools=[kyc_record],
    ),
}


#####
# Step 3, WIRE them into a graph
#####
def build_workflow(client, alert_id: str, checkpoint_storage=None, session=None):
    """Build a fresh workflow for one alert.

    A function, not a module-level object, for two reasons that happen to agree:
    fresh executor instances mean no state leaks between cases, and a resumed
    workflow must rebuild with identical executor ids or the checkpoint will not
    load onto it.

    Namespacing is necessary and not sufficient. State keys and the session id both
    carry the alert id, but Review._round is a plain integer on a plain object that
    no prefix protects. THE ISOLATION BOUNDARY IS THE WORKFLOW INSTANCE.
    """
    # Two framework-supplied memory strategies, applied to the AGENT's conversation
    # - not to the desk's findings. The window is a token budget (it also keeps the
    # last 4 tool-call groups, because dropping the tool output an agent is
    # mid-reasoning about is a specific kind of broken); the summariser replaces
    # evicted turns with linked summary text, and a summary can itself be
    # summarised, which is the same hierarchy Review._remember builds by hand.
    window = ContextWindowCompactionStrategy(max_context_window_tokens=24000, max_output_tokens=2000)
    summariser = SummarizationStrategy(client=client, target_count=4, threshold=2)
    # The agent's own thread for this case. hold.py and resume.py pass one in from
    # the session store; a fresh run makes its own. It has to_dict()/from_dict(),
    # which is what makes that store possible.
    session = session or AgentSession(session_id=f"alert:{alert_id}")

    triage = TriageNode(
        client.as_agent(
            name="triage",
            instructions=TRIAGE_INSTRUCTIONS,
            default_options={"response_format": TriagePlan},  # structured output - Pydantic typing
            compaction_strategy=window,
        ),
        alert_id,
        session,
    )
    # One executor per spec: the same function, a different agent bound.
    specialists = [
        make_specialist(node_id, client.as_agent(**spec))
        for node_id, spec in SPECIALIST_SPECS.items()
    ]
    review = Review(
        client.as_agent(
            name="reviewer",
            instructions=REVIEWER_INSTRUCTIONS,
            default_options={"response_format": ReviewDecision},
            compaction_strategy=summariser,
        ),
        # The fourth agent, and the only one nobody talks to: it exists to compress
        # the ladder in Review._remember. Every compression is a model call you pay
        # for, which is what WINDOW and L1_BEFORE_L2 are really tuning.
        summarize_agent=client.as_agent(
            name="summariser",
            instructions=SUMMARISER_INSTRUCTIONS,
        ),
    )

    builder = WorkflowBuilder(
        start_executor=triage,
        # Passing None simply leaves checkpointing off. Note this is the ONLY change
        # durability makes to the graph - no node changes, no edge changes. That is
        # what owning your edge types bought you.
        checkpoint_storage=checkpoint_storage,
        # Not cosmetic: the checkpoint partition key that list_checkpoints() queries
        # on. The alert id ends up doing four jobs in this file - workflow name,
        # state-key namespace, agent session id, and the boundary between cases.
        # That is where LangGraph's single thread_id went: it split into things that
        # are not the same thing.
        name=alert_id,
        # A superstep backstop for a runaway graph, NOT a termination policy.
        # MAX_ROUNDS is the policy.
        max_iterations=40,
        # Not tidying, and you will not guess this one: leave it out and every agent
        # node's streaming token updates arrive as "output" events - the terminal
        # fills with one word per line.
        output_from=[review],
    )
    # Fan out to the subset triage ordered. The width is decided at run time.
    builder.add_multi_selection_edge_group(triage, specialists, select_checks)
    # Plain edges, NOT add_fan_in_edges - see the note in Review.handle. Plain edges
    # deliver whichever message arrives; Review decides when the round is complete.
    for node in specialists:
        builder.add_edge(node, review)
    # The cycle, in one line. No special API, no loop construct: a graph is a graph
    # and an edge pointing backwards is allowed. Every named orchestration builder
    # is structurally incapable of expressing this line.
    builder.add_edge(review, triage)

    #####
    # Step 4, BUILD it, and RUN it
    #####
    return builder.build()
