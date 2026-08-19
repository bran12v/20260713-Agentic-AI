"""
Multi-agent sequential orchestration with three specialist/worker agents.

summarizer -> classifier -> action. The list order IS the dependency chain
"""
from dotenv import load_dotenv
import asyncio
import os
import sys
from typing import cast

from agent_framework import Message
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
from agent_framework.orchestrations import SequentialBuilder

load_dotenv()

# input item for our sequential multi-agent orchestration
BULLETIN = """
Source: FCA Handbook Notice 118, published 2026-07-31.
Effective 2027-01-01, firms carrying out MiFID investment services must retain
records of all client-facing electronic communications, including instant
messaging on approved channels, for a minimum of seven years (previously five).
Records must be retrievable within 72 hours of a written supervisory request.
Firms may apply for a transitional extension to 2027-07-01 for archived data
held on decommissioned platforms.
"""

async def main() -> None:
    # agent instructions (system prompts) -> three specialists, three narrow jobs with specific requirements.
    summarizer_instructions = """
    You are a regulatory analyst. Condense the bulletin into one neutral sentance
    stating who is affected, what changed, and when it takes effect.
    Do not add commentary, recommendations, or interpretation.
    """

    classifier_instructions = """
    You are a compliance triage analyst. Read the summary and classify the change
    as exactly one of: In scope, Out of scope, or Needs legal review.
    Answer with the classification only. No explanation.
    """

    action_instructions = """
    You are a compliance operations lead. The conversation above contains a summary of a regulatory bulletin 
    and a one-line classification of it. 
    Recommend the single next control action in one sentance, starting with a verb.
    Do NOT repeat the summary or classification.
    Example:
    Open a change record against the communcations archive control and assign to the Data Retention owner.
    """

    chat_client = FoundryChatClient(
        project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        credential=AzureCliCredential()
    )

    # Three agents -> one client

    # summarizer agent
    summarizer_agent = chat_client.as_agent(
        name="summarizer",
        instructions=summarizer_instructions
    )
    # classifier agent
    classifier_agent = chat_client.as_agent(
        name="classifier",
        instructions=classifier_instructions
    )
    # action agent
    action_agent = chat_client.as_agent(
        name="action",
        instructions=action_instructions
    )

    # Build sequential orchestration -> ORDER matters here, order IS the dependency chain
    workflow = SequentialBuilder(
        participants=[summarizer_agent, classifier_agent, action_agent],
        output_from="all"
    ).build() # must build before run

    result = await workflow.run(f"Regulartory bulletin: {BULLETIN}")
    outputs = result.get_outputs()

    i = 1
    for response in outputs:
        for message in cast(list[Message], response.messages):
            name = message.author_name or ("assistant" if message.role == "assistant" else "user")
            print(f"{'-' * 60}\n{i:02d} [{name}]\n {message.text}")
            i += 1

if __name__ == "__main__":
    asyncio.run(main())
