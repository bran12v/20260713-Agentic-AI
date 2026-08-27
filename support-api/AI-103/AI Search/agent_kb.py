"""Hand the knowledge to the agent we will write.

Agent will interact with Azure AI Search over the tool loop.
"""

import asyncio
import os
import sys

from collections.abc import Awaitable, Callable

from agent_framework import (
    Agent,
    FunctionInvocationContext,
    MCPStreamableHTTPTool,
    function_middleware
)
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv

load_dotenv()

from kb_lib import KB_NAME

MCP_URL = (
    f"{os.environ["SEARCH_ENDPOINT"]}/knowledgebases/{KB_NAME}"
    "/mcp?api-version=2026-05-01-preview"
)

INSTRUCTIONS = (
    "You are an internal delivery-standards assistant. You must ALWAYS search "
    "the connected knowledge base before answering, and you must NEVER answer "
    "from your own training data. Cite the doc_id and section of every claim. "
    "If the knowledge base does not contain the answer, respond exactly: "
    "\"That isn't covered in our current standards library - please raise it "
    "with the delivery lead.\""
)

@function_middleware
async def show_tool_result(
    context: FunctionInvocationContext,
    call_next: Callable[[], Awaitable[None]]
):
    """Print what the tool actually returned."""
    await call_next() # tool call that runs in the await
    items = context.result
    print(f"\n--- {context.function.name} returned {len(items)} content items")
    for i, item in enumerate(items[:2]):
        print(f"--- [{i}] {item.text[:300]}")
    print()

async def main() -> None:
    async with AzureCliCredential() as credential:
        token = (await credential.get_token(
            "https://search.azure.com/.default"
        )).token

        kb_tool = MCPStreamableHTTPTool(
            name="delivery_standards",
            url=MCP_URL,
            header_provider=lambda _kwargs: {"Authorization": f"Bearer {token}"}, # headers of all MCP requests
            allowed_tools=["knowledge_base_retrieve"],
            approval_mode="never_require",
            request_timeout=60,
        )

        client = FoundryChatClient(
            project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
            model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
            credential=credential
        )

        async with kb_tool, Agent(
            client,
            instructions=INSTRUCTIONS,
            name="delivery-standards-agent",
            tools=[kb_tool],
            middleware=[show_tool_result]
        ) as agent:
            for question in [
                "Does rotating a TLS certificate on a load balancer need CAB approval?",
                "What is our parental leave entitlement?",
            ]:
                response = await agent.run(question)
                print(f"Q: {question}\nA: {response.text}\n")



if __name__ == "__main__":
    asyncio.run(main())