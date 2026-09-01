"""Run one alert end to end, answering the desk's approval request in-process.

This is the SAME-PROCESS half of human-in-the-loop. The desk parks a request with
ctx.request_info(); this driver sees the request_info event and answers it by
calling run() again on the SAME workflow object. Nothing is persisted: the parked
request lives in the workflow's in-memory context, so the object and the process
must both outlive the pause.

That is fine here because this driver answers instantly - it signs off on the
desk's behalf. When the human is at lunch instead, a process holding an idle
workflow for six hours is not a design, it is a leak: see hold.py / resume.py,
which park the case on disk and finish it from a different process.

RUN: python run_desk.py [ALERT_ID]        # default AML-8807
     AML-8807 escalates to a human; AML-8815 and AML-8823 usually close alone.
"""

import asyncio
import sys

from desk import ApprovalDecision, build_workflow, make_client, opening_prompt


async def main() -> None:
    alert_id = sys.argv[1] if len(sys.argv) > 1 else "AML-8807"
    client, credential = make_client()
    # No checkpoint_storage: this run is entirely in memory.
    workflow = build_workflow(client, alert_id)

    print(f"=== {alert_id} ===")
    # Keyed by request_id - the id the framework matches back to the executor that
    # asked, so it can call that executor's @response_handler. In a real desk this
    # id is what the ticket, the queue message or the email would carry.
    pending: dict[str, ApprovalDecision] = {}
    async for event in workflow.run(opening_prompt(alert_id), stream=True):
        # event.type is a plain string - there is no event class to isinstance
        # against. The framework emits one WorkflowEvent discriminated by a literal:
        # started, status, failed, output, intermediate, request_info,
        # executor_invoked, executor_completed, executor_failed, superstep_completed.
        if event.type == "request_info":
            print(f"  [HUMAN] approval requested: {event.data.action}")
            # Flip True to False to watch the deny path: the disposition changes,
            # the audit line does not - you can still see exactly what was proposed
            # and refused, which is what a regulator asks for.
            pending[event.request_id] = ApprovalDecision(True, "signed off by desk head")
        elif event.type == "output":
            print(f"\nRESULT: {event.data}")
        elif event.type in ("error", "failed", "executor_failed"):
            print(f"  !! {event.type}: {event.data}")

    # A while loop, not an if: answering one request can drive the graph into
    # another round that asks again. This desk asks at most once, but a gate that
    # reopens is normal and a single `if` would silently drop the second request.
    while pending:
        answers, pending = pending, {}
        # run(responses=...) with NO message resumes the same run. Runs are not
        # isolated - state carries across calls on one instance. This is not a
        # second investigation, it is the answer to a question the first one asked.
        async for event in workflow.run(stream=True, responses=answers):
            if event.type == "request_info":
                pending[event.request_id] = ApprovalDecision(True, "signed off by desk head")
            elif event.type == "output":
                print(f"\nRESULT: {event.data}")

    await credential.close()


asyncio.run(main())
