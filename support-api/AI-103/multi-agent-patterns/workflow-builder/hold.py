"""Run the desk until it asks for a human, then exit WITHOUT answering.

Process 1 of two. The lesson is what this file does NOT do: the request_info
branch prints and nothing else - no answer, no pending dict. The stream drains,
the workflow is idle, main() returns, the interpreter exits.

Nothing is running afterwards. No worker, no poller, no held connection. The case
exists as files, in two stores that answer two different questions:

    checkpoints/   what has this WORKFLOW done   (every executor's state, the
                   queued messages, the shared state, and the pending request)
    sessions/      what does this AGENT remember saying   (triage's thread)

Restore one without the other and you get a graph that resumes correctly with an
agent that has amnesia.

RUN: python hold.py [ALERT_ID]     # default AML-8807, the alert that escalates
     then, in a NEW shell:  python resume.py AML-8807 approve
"""

import asyncio
import sys

from agent_framework import AgentSession

from desk import build_workflow, make_client, make_session_store, make_storage, opening_prompt


async def main() -> None:
    alert_id = sys.argv[1] if len(sys.argv) > 1 else "AML-8807"
    client, credential = make_client()
    storage = make_storage()
    sessions = make_session_store()
    # The agent's own thread for this case, separate from the workflow checkpoint.
    # Created here rather than inside build_workflow because THIS process has to
    # save it afterwards.
    session = AgentSession(session_id=f"alert:{alert_id}")
    # Passing the storage is the only change durability makes to the graph. Every
    # superstep barrier now writes a checkpoint - the barrier being the only moment
    # a consistent view of the world exists.
    workflow = build_workflow(client, alert_id, checkpoint_storage=storage, session=session)

    print(f"=== {alert_id} (process 1) ===")
    parked = False
    async for event in workflow.run(opening_prompt(alert_id), stream=True):
        if event.type == "request_info":
            # Print and nothing else. That is the whole point of this file.
            print(f"\n  [HUMAN] approval requested: {event.data.action[:90]}")
            # Note this id. resume.py prints the same one, in another process.
            print(f"  [HUMAN] request_id: {event.request_id}")
            parked = True
        elif event.type == "output":
            print(f"\nRESULT: {event.data}")

    # Print the count every run and check it against the round count: a three-round
    # case writes roughly seven. A count of 1-2 means checkpoint writes are failing
    # as WARNINGS - the failure mode to watch for, because the run itself looks
    # perfectly healthy. (Two usual causes: a non-JSON value out of
    # on_checkpoint_save, or a cp1252 console - set PYTHONUTF8=1, which
    # sys.stdout.reconfigure cannot reach.)
    checkpoints = await storage.list_checkpoints(workflow_name=alert_id)
    print(f"\n  {len(checkpoints)} checkpoints written for workflow {alert_id!r}")
    for c in sorted(checkpoints, key=lambda c: c.iteration_count)[-3:]:
        print(f"    {c.checkpoint_id}  iteration={c.iteration_count}")

    # Two different things, saved to two different places.
    await sessions.set(session.session_id, session)
    print(f"  agent session {session.session_id!r} saved to the session store")

    if parked:
        print("\n  Parked awaiting a human. Exiting. Nothing is running now.")
        print("  In a NEW shell: python resume.py " + alert_id)

    await credential.close()


asyncio.run(main())
