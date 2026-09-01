"""Drafting a SAR narrative with chained agent nodes.

THE OTHER WAY TO PUT AN AGENT IN A GRAPH. desk.py calls its agents INSIDE
executors, because every message on its edges has to be a type it owns - routable
by a condition, and serialisable into a checkpoint. Here the agent IS the node: an
AgentExecutor consumes an AgentExecutorRequest and emits an AgentExecutorResponse,
and the next AgentExecutor takes that response directly. No adapters in between.

    start --> drafter --> reviewer --> editor --> publish
              |________ no adapters: the framework hands
                        each agent the conversation ______|

THE RULE FOR CHOOSING: AgentExecutor when agents feed each other directly. Your
own executor when a message has to be shaped, routed, or persisted. The desk
routes on a field and checkpoints its queue, so it owns its types. This pipeline
does neither, so it does not - and it is deliberately NOT checkpointed: an SDK
response object queued on an edge carries parametrized generics that do not
pickle, and the checkpoint write would fail as a warning while the run reports
success.

This is also a SequentialBuilder shape - three agents in a line. What you get by
wiring it yourself is per-hop context control, which is the one idea below.

Self-contained: the desk never imports this file.

RUN: python sar_pipeline.py
"""

import asyncio
import os
import sys

from agent_framework import (
    AgentExecutor,
    AgentExecutorRequest,
    AgentExecutorResponse,
    Message,
    WorkflowBuilder,
    WorkflowContext,
    executor,
)
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv
from typing_extensions import Never

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

# The disposition the desk reached, plus the evidence behind it. Hard-coded here so
# the pipeline is runnable on its own - in a real desk this is what a "file a
# report" approval would hand over.
CASE = """Alert AML-8807. Customer CUS-4000 (Marchetti Ventures LLP).
Payment: GBP 48,500 to Marchetti Ventures LLP, jurisdiction MT, 2026-06-14.
Sanctions: TRUE MATCH on EU CFSP and UK HMT (score 1.0); OFAC SDN near match
'Marchettii Ventures LLP' (0.978).
KYC: refresh date null; expected-geography and expected-counterparty fields absent.
History: three prior payments of 48,500 in three currencies to three counterparties.
Disposition: block the payment, freeze the account, file a report."""


@executor(id="start")
async def start(case: str, ctx: WorkflowContext[AgentExecutorRequest]) -> None:
    """The one adapter this pipeline needs: text in, agent request out."""
    # An agent node's inbox. `contents` is a LIST because one message can carry
    # text, images and function calls together. should_respond=False would push
    # context into a node without making it run.
    await ctx.send_message(
        AgentExecutorRequest(messages=[Message(role="user", contents=[case])], should_respond=True)
    )


@executor(id="publish")
async def publish(response: AgentExecutorResponse, ctx: WorkflowContext[Never, str]) -> None:
    """The last agent's response becomes the workflow output."""
    await ctx.yield_output(response.agent_response.text.strip())


async def main() -> None:
    credential = AzureCliCredential()
    client = FoundryChatClient(
        # The lecture names these PROJECT_ENDPOINT / MODEL_DEPLOYMENT_NAME; this
        # repo's .env already uses the AZURE_* names below, as desk.py does.
        project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        credential=credential,
    )

    # AgentExecutor(agent, id=...) is the whole wrapping: no handler to write and
    # no message type to declare, because the request and response types are the
    # framework's.
    drafter = AgentExecutor(
        client.as_agent(
            name="narrative_drafter",
            instructions=(
                "You draft the narrative section of a Suspicious Activity Report. "
                "Write 4-6 sentences covering who, what, when, where and why it is suspicious. "
                "Think on the page: state your reasoning as you go."
            ),
        ),
        id="drafter",
    )

    reviewer = AgentExecutor(
        client.as_agent(
            name="compliance_reviewer",
            instructions=(
                "You review SAR narratives for regulatory sufficiency. List any missing "
                "element a regulator would expect, then restate the narrative with those "
                "gaps closed. Be specific and brief."
            ),
        ),
        id="reviewer",
        # The reviewer needs the drafter's reasoning to judge it.
        context_mode="full",
    )

    editor = AgentExecutor(
        client.as_agent(
            name="final_editor",
            instructions=(
                "You produce the final filed narrative. Output ONLY the narrative prose: "
                "no preamble, no bullet list, no commentary on the review."
            ),
        ),
        id="editor",
        # The editor files what the reviewer approved. It has no business seeing the
        # drafter's working, and the drafter was told to think on the page.
        context_mode="last_agent",
    )

    # context_mode is what this pipeline exists to teach: "full" passes the entire
    # prior conversation, "last_agent" only the upstream agent's own messages,
    # "custom" whatever a context_filter callable returns. It applies on exactly one
    # path - an agent node receiving a prior AgentExecutorResponse - which is why it
    # is here and not on the desk's triage node, which is fed a plain prompt.
    workflow = (
        WorkflowBuilder(start_executor=start, output_from=[publish])
        .add_edge(start, drafter)
        .add_edge(drafter, reviewer)
        .add_edge(reviewer, editor)
        .add_edge(editor, publish)
        .build()
    )

    print("=== SAR narrative pipeline ===")
    async for event in workflow.run(CASE, stream=True):
        if event.type == "executor_completed":
            print(f"  [{event.executor_id}] done")
        elif event.type == "output":
            print(f"\nFILED NARRATIVE:\n{event.data}")

    await credential.close()


asyncio.run(main())
