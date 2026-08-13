import os, json, asyncio

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FunctionTool, PromptAgentDefinition
from dotenv import load_dotenv
from mcp import StdioServerParameters, ClientSession
from azure.identity import AzureCliCredential
from mcp.client.stdio import stdio_client
from typing import Callable
from openai.types.responses.response_input_param import FunctionCallOutput

load_dotenv()

AGENT_NAME = "delivery-support-agent-mcp"

server_params = StdioServerParameters(command="python", args=["server.py"])

# we are going to pass in the tools "input_schema"
def _mcp_schema_to_parameters(input_schema: dict) -> dict:
    """Translate an MCP tool's input_schema into the JSON schema that the model actually reads."""
    properties = (input_schema or {}).get("properties", {}) or {}
    required = list(properties.keys())
    return {
        "type": "object",
        "properties": properties,
        "required": required,
        "additionalProperties": False
    }


async def main() -> None:
    project = AIProjectClient(
        endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
        credential=AzureCliCredential(process_timeout=30)
    )

    openai_client = project.get_openai_client()

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize() # hey, mcp -> you there?
            tools_result = await session.list_tools() # cool, what tools do you have?
            print("Discovered:", [tool for tool in tools_result.tools]) # oh nice. Here are the tools.

            def make_wrapper(tool_name: str) -> Callable:
                async def _call(**kwargs):
                    result = await session.call_tool(tool_name, arguments=kwargs)
                    return result.content[0].text
                
                return _call

            function_dict = {tool.name: make_wrapper(tool.name) for tool in tools_result.tools} # dict of callables

            mcp_function_tools = [
                FunctionTool(
                    name=tool.name,
                    description=tool.description,
                    parameters= _mcp_schema_to_parameters(tool.inputSchema),
                    strict=True
                )
                for tool in tools_result.tools
            ]

            agent = project.agents.create_version(
                agent_name=AGENT_NAME,
                definition=PromptAgentDefinition(
                    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
                    instructions=(
                        "You are an interal delivery-support agent. Use the " \
                        "available tools to look up ticket and engagement data."
                    ),
                    tools=mcp_function_tools,
                )
            )
            print("Agent version:", agent.version)

            reference = {
                "agent_reference": {
                    "name": agent.name,
                    # "version": agent.version,
                    "type": "agent_reference"
                }
            }

            response = openai_client.responses.create(
                input=(
                    "What's the status of ticket TKT-4821, and how much budget " \
                    "is left on ENG-2200?"
                ),
                extra_body=reference
            )

            # the agent requests function_call items; we execute them.
            input_list = []
            for item in response.output:
                if item.type == "function_call":
                    print(f"[CLIENT] model requested {item.name}({item.arguments})")
                    fn = function_dict[item.name]
                    result = await fn(**json.loads(item.arguments)) # the actual tool call, which is asking the mcp server to call the tool.
                    input_list.append(
                        FunctionCallOutput(
                            type="function_call_output",
                            call_id=item.call_id,
                            output=result
                        )
                    )

            if input_list:
                response = openai_client.responses.create(
                    input=input_list,
                    previous_response_id=response.id, # server side state
                    extra_body=reference
                )

            print(response.output_text)



if __name__ == "__main__":
    asyncio.run(main())