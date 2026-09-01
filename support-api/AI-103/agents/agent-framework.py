"""
Demo for the Microsoft Agent Framework (different from the Foundry SDK)

pattern -> client connect -> agent behaves -> tools act.
"""

import json

from dotenv import load_dotenv
import asyncio
import os
from pathlib import Path
from typing import Annotated
from pydantic import Field

from agent_framework import Agent, Message, tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

load_dotenv()

INSTRUCTIONS = """You are an AI assistant for expense claim submission.
At the user's request, create an expense claim and use the plug-in function to send an email to expenses@contoso.com with the subject 'Expense Claim' and a body that contains itemized expenses with a total.
Then confirm to the user that you've done so. Don't ask for any more information from the user, just use the data provided to create the email."""


# Tools do actions, this tool will simulate a email by printing it out. 
@tool(approval_mode="always_require")
def submit_claim(
    to: Annotated[str, Field(description="Who to send the email to")],
    subject: Annotated[str, Field(description="The subject of the email")],
    body: Annotated[str, Field(description="The text body of the email")],
):
    """Send the itemized expense claim to the expenses inbox."""
    print("\nTo:", to)
    print("Subject:", subject)
    print(body, "\n")

async def process_expense_data(prompt: str, expense_data: str) -> None:
    """The function will do the agent processing for completing the users provided prompt."""
    client = FoundryChatClient(
        project_endpoint=os.environ.get("AZURE_FOUNDRY_PROJECT_ENDPOINT"),
        model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        credential=AzureCliCredential(),
    )

    async with Agent( # TODO: going to come back to this `with` keyword
        client=client,
        name="ExpenseClaimAgent",
        instructions=INSTRUCTIONS,
        tools=[submit_claim]
    ) as agent:
        try:
            session = agent.create_session() # this will allow conversation continuation
            prompt_messages = [f"{prompt}: {expense_data}"]
            result = await agent.run(prompt_messages, session=session)

            while result.user_input_requests: # why the double loop
                approval_reponses = []

                for request in result.user_input_requests:
                    if request.function_call is None:
                        continue

                    args = request.function_call.parse_arguments() or {}
                    print(f"\nApproval needed: {request.function_call.name}")
                    print(json.dumps(args, indent=2, sort_keys=True, default=str))

                    approved = input("y/n: ").strip().lower() == "y" # this will return true if 'y', false for anything else

                    approval_reponses.append(
                        request.to_function_approval_response(approved=approved)
                    )

                if not approval_reponses:
                    break

                result = await agent.run(Message("user", approval_reponses), session=session)

            print(f"\n# Agent:\n{result}")
        except Exception as exc:
            print(exc)

async def main() -> None:
    file_path = Path(__file__).resolve().parent / "data.txt"
    with file_path.open("r") as file:
        data = file.read() + "\n"

    user_prompt = input(
        f"Here is the expense data in your file:\n{data}\n\n"
        "What would you like me to do with it?\n\n"
    )

    await process_expense_data(user_prompt, data) # print out the email the tool wants to send
    

if __name__ == "__main__":
    asyncio.run(main())