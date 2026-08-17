"""Server-side MCP: hand Foundry a remote MCP endpoint and let the runtime drive it.

Contrast with agent.py, which does *client-side* MCP -- we spawn server.py over stdio,
translate every inputSchema into a FunctionTool by hand, and execute each tool call
ourselves. Here the Foundry runtime does discovery, invocation, and result-feeding
inside the service. We only approve or deny.

IMPORTANT: Foundry connects to the MCP server from its own compute, so a stdio
server.py is NOT reachable -- there is no URL to dial. To point this at delivery-tools
you must first host server.py over streamable HTTP (Azure Container Apps or Azure
Functions) and set MCP_SERVER_URL. Until then it defaults to the public Microsoft Learn
MCP server so the wiring is runnable end to end.
"""

import os, sys, json

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MCPTool, PromptAgentDefinition
from azure.identity import AzureCliCredential
from dotenv import load_dotenv
from openai.types.responses.response_input_param import McpApprovalResponse

load_dotenv()

# model output routinely contains non-breaking hyphens and smart quotes; the default
# Windows console codepage (cp1252) throws on them mid-print.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

AGENT_NAME = "delivery-support-agent-mcp-tool"

# swap these two for your hosted delivery-tools endpoint once server.py is deployed.
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "https://learn.microsoft.com/api/mcp")
MCP_SERVER_LABEL = os.getenv("MCP_SERVER_LABEL", "learn-docs")

# and swap this for the ticket/engagement question at the same time.
QUESTION = os.getenv(
    "MCP_QUESTION",
    "Search the Microsoft docs: what does the require_approval setting do on the "
    "Foundry Agent Service MCP tool? Cite the doc you used.",
)

def _approve(item) -> bool:
    """Review one mcp_approval_request before letting the runtime make the call."""
    print(f"[APPROVAL] server={item.server_label} tool={getattr(item, 'name', '<unknown>')}")
    print(f"[APPROVAL] args={json.dumps(getattr(item, 'arguments', None), default=str)}")

    # the doc sample blocks on a bare input(); that dies under CI or a piped stdin.
    # isatty() alone is not enough -- Git Bash on Windows claims a TTY then hands back EOF.
    try:
        if not sys.stdin.isatty():
            raise EOFError
        return input("Approve this MCP tool call? (y/N): ").strip().lower() == "y"
    except EOFError:
        print("[APPROVAL] no interactive stdin -- auto-approving. safe only for read-only tools.")
        return True


def _collect_approvals(response) -> list:
    """Pull every pending approval request off a response, and narrate what the runtime did."""
    for item in response.output:
        # mcp_list_tools is Foundry doing the discovery that agent.py does by hand.
        if item.type in ("mcp_list_tools", "mcp_call"):
            print(f"[RUNTIME] {item.type}: {getattr(item, 'name', item.server_label)}")

    return [
        McpApprovalResponse(
            type="mcp_approval_response",
            approve=_approve(item),
            approval_request_id=item.id,
        )
        for item in response.output
        if item.type == "mcp_approval_request" and item.id
    ]


def main() -> None:
    project = AIProjectClient(
        endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
        credential=AzureCliCredential(process_timeout=30)
    )

    openai_client = project.get_openai_client()

    # the entire client-side dance from agent.py collapses into this one declaration:
    # no ClientSession, no list_tools(), no _mcp_schema_to_parameters, no wrapper callables.
    mcp_tool = MCPTool(
        server_label=MCP_SERVER_LABEL,
        server_url=MCP_SERVER_URL,
        require_approval="never",   # "never" | {"never": [...]} | {"always": [...]}
        # allowed_tools=[...],       # optional allow-list; omitted means every tool on the server
        # project_connection_id=...  # required when the MCP server needs auth
    )

    agent = project.agents.create_version(
        agent_name=AGENT_NAME,
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
            instructions=(
                "You are an internal delivery-support agent. Use the "
                "available MCP tools to answer questions."
            ),
            tools=[mcp_tool],
        )
    )
    print("Agent version:", agent.version)

    reference = {
        "agent_reference": {
            "name": agent.name,
            "type": "agent_reference"
        }
    }

    response = openai_client.responses.create(input=QUESTION, extra_body=reference)

    # loop rather than the doc's single follow-up: the model can chain several MCP
    # calls, and each round trip can surface a fresh batch of approval requests.
    while (input_list := _collect_approvals(response)):
        response = openai_client.responses.create(
            input=input_list,
            previous_response_id=response.id, # server side state
            extra_body=reference
        )

    print(response.output_text)


if __name__ == "__main__":
    main()
