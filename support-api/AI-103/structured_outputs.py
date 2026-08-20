"""Structured outputs using Pydantic w/ the Microsoft Agent Framework."""

from dotenv import load_dotenv
import asyncio
import logging
import os
import sys
from typing import Annotated, Literal

from agent_framework import Agent, ChatOptions, tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
from pydantic import BaseModel, Field

load_dotenv()

class Entity(BaseModel):
    """One ID the agent recognizes in the user's question"""

    kind: Literal["ticket", "engagement"]
    id: str = Field(description="The ID exactly as it appears, e.g. TKT-##### where # represents a number from 0-9.")

class TicketTriage(BaseModel):
    """Structured triage of a delivery-support question. (output object)"""

    summary: str = Field(description="One sentence, plain English, no IDs.")

    priority: Literal["low", "medium", "high", "critical"] = Field(
        description="How urgent this is for the delivery team."
    )

    entities: list[Entity] = Field(
        description="Every ticket or engagement ID mentioned in the question."
    )

    budget_remaining_usd: float | None = Field(
        description="Remain engagement budget in USD, or null if not applicable."
    )

    needs_human: bool = Field(
        description="True if a person must review this before we reply."
    )

# getting ticket status
@tool
def get_ticket_status(
    ticket_id: Annotated[str, Field(description="Support ticket ID, e.g. TKT-#### where # represents a number from 0-9.")]
) -> str:
    """Look up the current status of an internal support ticket by its ID."""
    print(f"[TOOL] get_ticket_status({ticket_id!r})")
    tickets = {
        "TKT-4821": "In progress - platform team, ETA 2 days.",
        "TKT-5090": "Resolved - closed 2026-07-18, expired cert.",
    }
    return tickets.get(ticket_id, f"No ticket found with ID {ticket_id!r}")

# getting engagement budget
@tool
def get_engagement_budget(
    engagement_id: Annotated[str, Field(description="Client engagement ID, e.g. ENG-##### where # represents a number from 0-9.")]
) -> str:
    """Return remaining budget for a client engagement by its ID."""
    print(f"[TOOL] get_engagement_budget({engagement_id!r})")
    budgets = {"ENG-2200": "$48,500 of $250,000 remaining (19%)."}
    return budgets.get(engagement_id, f"No enagement found with ID {engagement_id!r}")

async def main() -> None:
        client = FoundryChatClient(
            project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
            model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
            credential=AzureCliCredential()
        )

        agent = Agent(
             client=client,
             instructions=(
                  "You are a delivery-support triage assistant. "
                  "Use tools to look up ticket and engagement data before triaging."
             ),
             tools=[get_ticket_status, get_engagement_budget]
        )

        prompt = input("User prompt: ")

        response = await agent.run(
            prompt,
            options=ChatOptions(response_format=TicketTriage) # this is payoff line, the structured output setting
        )

        triage = response.value

        print(triage.model_validate())

if __name__ == "__main__":
    asyncio.run(main())