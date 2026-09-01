"""Pick the case back up in a different process and finish it.

Process 2 of two. Nothing is handed over in memory: two arguments arrive from the
command line - an alert id and a decision - and everything else comes off disk,
from the two stores hold.py wrote.

Three lines are the entire point:

    1. sessions.get(...)                  the agent's memory, off disk
    2. build_workflow(...)                the graph rebuilt FROM SCRATCH in a
                                          process that has never seen this case.
                                          Identical executor ids, or the checkpoint
                                          will not load onto it.
    3. run(checkpoint_id=..., stream=True) the restore, which re-emits the pending
                                          request with the SAME request_id the
                                          first process printed.

Everything between the two commands could have been a week.

RUN: python resume.py [ALERT_ID] [approve|deny]      # default AML-8807 approve
"""

import asyncio
import sys

from agent_framework import AgentSession

from desk import (
    ApprovalDecision,
    build_workflow,
    make_client,
    make_session_store,
    make_storage,
)


async def main() -> None:
    alert_id = sys.argv[1] if len(sys.argv) > 1 else "AML-8807"
    # Anything other than the literal "approve" denies - the same fail-safe
    # direction as Review.on_human, applied at the other end of the wire.
    approve = (sys.argv[2] if len(sys.argv) > 2 else "approve") == "approve"

    client, credential = make_client()
    storage = make_storage()
    sessions = make_session_store()
    # The checkpoint restores the GRAPH. This restores what triage remembers saying.
    # The `or AgentSession(...)` fallback is deliberate: a missing session must not
    # crash the resume - the graph is still recoverable, triage just starts a fresh
    # thread. Degrade, do not fail. The checkpoint is the load-bearing store; the
    # session is the enhancement.
    session = await sessions.get(f"alert:{alert_id}") or AgentSession(session_id=f"alert:{alert_id}")
    print(f"  agent session {session.session_id!r} loaded from the session store")
    # Same builder, same executor ids. A different topology cannot load this
    # checkpoint - which is the second reason build_workflow is a function.
    workflow = build_workflow(client, alert_id, checkpoint_storage=storage, session=session)

    # workflow_name is the partition key, and it is the alert id by way of
    # WorkflowBuilder(name=alert_id). One workflow name per case, one lineage.
    checkpoints = await storage.list_checkpoints(workflow_name=alert_id)
    if not checkpoints:
        print(f"No checkpoints for {alert_id}. Run hold.py first.")
        await credential.close()
        return
    latest = max(checkpoints, key=lambda c: c.iteration_count)
    print(f"=== {alert_id} (process 2) ===")
    print(f"  resuming from checkpoint {latest.checkpoint_id} (iteration {latest.iteration_count})")

    # Restoring re-emits any request the earlier process left pending.
    pending: dict[str, ApprovalDecision] = {}
    async for event in workflow.run(checkpoint_id=latest.checkpoint_id, stream=True):
        if event.type == "request_info":
            # Compare this id with the one hold.py printed: they are the same.
            # Different interpreter, different terminal, same conversation.
            print(f"  re-emitted pending request {event.request_id}")
            print(f"  action: {event.data.action[:90]}")
            pending[event.request_id] = ApprovalDecision(
                approve, "signed off in the morning batch" if approve else "insufficient evidence"
            )
        elif event.type == "output":
            print(f"\nRESULT: {event.data}")

    # Not ceremony: answering one request can drive the graph into another round
    # that asks again. Handle a sequence of pauses, not a single one.
    while pending:
        answers, pending = pending, {}
        async for event in workflow.run(stream=True, responses=answers):
            if event.type == "request_info":
                pending[event.request_id] = ApprovalDecision(approve, "batch decision")
            elif event.type == "output":
                print(f"\nRESULT: {event.data}")

    await credential.close()


asyncio.run(main())
