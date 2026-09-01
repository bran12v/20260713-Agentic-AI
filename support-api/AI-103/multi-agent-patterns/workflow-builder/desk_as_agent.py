"""The finished desk, exposed as an agent.

A named builder is a graph somebody else wired for you. The reverse is also true:
Workflow.as_agent() returns a WorkflowAgent, and .run() returns an AgentResponse -
the same two types the specialists have been using all day. Five nodes, a
model-sized fan-out, a cycle, a memory ladder and a human gate, and from the
outside it is an agent you call.

That is what TriageNode.from_messages exists for: as_agent() sends list[Message]
to the start executor, so the start executor has to accept it or this raises
"Workflow's start executor cannot handle list[Message]" at build time.

THE HONEST CAVEAT: as_agent() is one call in, one disposition out, so a run that
pauses for a human does not fit this interface. Expose the desk as an agent for
the cases that close on their own; keep the streaming, request_info-aware path
(run_desk.py, hold.py/resume.py) for the ones that do not. AML-8823 is the default
here for exactly that reason - AML-8807 escalates.

RUN: python desk_as_agent.py [ALERT_ID]      # default AML-8823
"""

import asyncio
import sys

from desk import build_workflow, make_client, opening_prompt


async def main() -> None:
    alert_id = sys.argv[1] if len(sys.argv) > 1 else "AML-8823"
    client, credential = make_client()

    # The whole wrapping is this one call. A WorkflowAgent satisfies the same
    # interface SequentialBuilder(participants=[...]) wants, so this graph can be a
    # participant in somebody else's named orchestration - or a node in a bigger
    # graph. The two layers are not a hierarchy; they compose in both directions.
    # (Which is also the moment to ask whether you need it: every layer is a real
    # cost in latency, tokens and debuggability.)
    desk_agent = build_workflow(client, alert_id).as_agent(
        name="alert_desk",
        description="Investigates a financial-crime alert end to end and returns a disposition.",
    )

    print(f"=== calling the desk as an agent: {alert_id} ===")
    print(f"  type      : {type(desk_agent).__name__}")
    print(f"  agent name: {desk_agent.name}")

    # No stream, no event loop over WorkflowEvents: one await, one response object.
    # The desk's own print() lines still appear, because they are inside the nodes.
    response = await desk_agent.run(opening_prompt(alert_id))
    print(f"\n  response type: {type(response).__name__}")
    disposition = response.text.strip()
    if disposition:
        print(f"\nDISPOSITION: {disposition[:600]}")
    else:
        # The caveat above, live. An empty response means the reviewer chose
        # "approve": the graph parked at request_info and there is no output,
        # because this interface has nowhere to put the question. Nothing failed -
        # the case is simply unfinished, and finishing it needs the streaming path.
        print("\nNO DISPOSITION - the desk parked for a human approval, which this")
        print("interface cannot answer. Use the streaming, request_info-aware path:")
        print(f"    python run_desk.py {alert_id}      (same process)")
        print(f"    python hold.py {alert_id}          (park it, then resume.py)")

    await credential.close()


asyncio.run(main())
