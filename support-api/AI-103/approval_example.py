import asyncio
from typing import Annotated
from dotenv import load_dotenv
from agent_framework import Agent, Message, tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
import os
load_dotenv()

@tool(approval_mode="always_require")
def add_to_calendar(
    event_name: Annotated[str, "Name of the event"],
    date: Annotated[str, "Date of the event"],
) -> str:
    """Add an event to the calendar (requires approval)."""
    return f"Added '{event_name}' to calendar on {date}"


async def main() -> None:
    agent = Agent(
        client=FoundryChatClient(
            project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
            credential=AzureCliCredential(),
            model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        ),
        name="CalendarAgent",
        instructions="You are a helpful calendar assistant.",
        tools=[add_to_calendar],
    )

    session = agent.create_session()

    result = await agent.run("Add a dentist appointment on March 15th", session=session)

    if result.user_input_requests:
        for request in result.user_input_requests:
            if request.function_call is None:
                continue
            print(f"Function: {request.function_call.name}")
            print(f"Arguments: {request.function_call.arguments}")

            approved = input("y/n: ").strip().lower() == "y"
            approval_response = request.to_function_approval_response(approved=approved)
            result = await agent.run(Message("user", [approval_response]), session=session)

    print(result)


asyncio.run(main())