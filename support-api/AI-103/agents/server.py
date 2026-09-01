"""MCP server. Host a catalog of enterprise tools.

It can be ran directly or via the agent function."""

import sys

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("delivery-tools") # creates a MCP server object with the name "delivery-tools"

# used as a decorater on our functions to make them into discoverable tools on our MCP server.
@mcp.tool()
def get_ticket_status(ticket_id: str) -> str:
    """Look up the current status of an internal support ticket by its ID."""
    # stdout is the JSON-RPC transport under stdio; diagnostics must go to stderr.
    print(f"[SERVER] get_ticket_status({ticket_id!r})", file=sys.stderr, flush=True)
    tickets = {
        "TKT-4821": "In progress — platform team, ETA 2 days.",
        "TKT-5090": "Resolved — closed 2026-07-18, expired cert.",
    }
    return tickets.get(ticket_id, f"No ticket found with ID {ticket_id}.")


@mcp.tool()
def get_engagement_budget(engagement_id: str) -> str:
    """Return remaining budget for a client engagement by its ID."""
    print(f"[SERVER] get_engagement_budget({engagement_id!r})", file=sys.stderr, flush=True)
    budgets = {"ENG-2200": "$48,500 of $250,000 remaining (19%)."}
    return budgets.get(engagement_id, f"No engagement found: {engagement_id}.")

if __name__ == "__main__":
    mcp.run()