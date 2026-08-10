"""Generate the OpenAPI spec that is needed to expose the support-api to a foundry agent."""

from support_api.models import Ticket
from typing import Any

from pathlib import Path
import yaml
import argparse

OPERATIONS: dict[str, dict[str, Any]] = { # OpenAPI Spec
    "/tickets": {
        "get": {
            "operationId": "listSupportTickets",
            # summary: one line, for a human reading the spec.
            "summary": "List support tickets, optionally filtered.",
            # description: 2-4 sentences, for the MODEL. Note how much of it is about
            # WHEN NOT to use this operation.
            "description": (
                "Retrieve support tickets for a customer account, optionally narrowed by "
                "priority, tenant, or status. Use this when the user asks what issues are "
                "open, which tickets are urgent, how many tickets a tenant has raised, or "
                "asks for a summary of current support load. Returns ticket metadata and "
                "body text, newest first. If the user names a specific ticket by its "
                "TKT-##### identifier, use getSupportTicket instead - this operation is for "
                "searching and listing, not for looking up one known ticket."
            ),
            "parameters": [
                {
                    "name": "tenant",
                    "in": "query",
                    "required": False,
                    # Parameter descriptions are prompts too. This one prevents a whole
                    # class of wrong answers.
                    "description": (
                        "Only return tickets belonging to this tenant (customer "
                        "organisation), e.g. 'acme-corp'. Always pass this when the user is "
                        "asking about a specific customer - omitting it returns tickets "
                        "across every tenant."
                    ),
                    "schema": {"type": "string", "maxLength": 50},
                },
            ],
            "responses": {
                "200": {
                    "description": "Matching tickets.",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "count": {"type": "integer"},
                                    "items": {
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/Ticket"},
                                    },
                                },
                            }
                        }
                    },
                }
            },
        }
    },
    "/tickets/{ticket_id}": {
        "get": {
            "operationId": "getSupportTicket",
            "summary": "Fetch one support ticket by its identifier.",
            "description": (
                "Retrieve the full record of a single support ticket when the user names it "
                "by identifier, for example 'what's the status of TKT-10042?'. Returns the "
                "title, body, priority, status, category, assignee, and timestamps. If the "
                "user has not given an identifier, use listSupportTickets to find candidates "
                "first."
            ),
            "parameters": [
                {
                    "name": "ticket_id",
                    "in": "path",
                    "required": True,
                    # The pattern is a HINT to the model about the shape of a ticket id,
                    # so it stops inventing TICKET-42. Flask validates the real thing.
                    "description": "Ticket identifier in the form TKT-##### , e.g. TKT-10042.",
                    "schema": {"type": "string", "pattern": r"^TKT-\d{5}$"},
                }
            ],
            "responses": {
                "200": {
                    "description": "The ticket.",
                    "content": {
                        "application/json": {"schema": {"$ref": "#/components/schemas/Ticket"}}
                    },
                },
                # No 404 here on purpose. Foundry fails the whole agent run on any non-2xx, so
                # the model never sees an error response - declaring one documents something
                # that cannot happen from the agent's point of view.
            },
        }
    },
}

MODELS = {"Ticket": Ticket}

def build_spec(server_url: str) -> dict[str, Any]:
    schemas: dict[str, Any] = {}
    for name, model in MODELS.items():
        # ref_template points nested refs at components/schemas, where OpenAPI expects them.
        # Without it they point into "#/$defs/" and resolve to nothing.
        schema = model.model_json_schema(ref_template="#/components/schemas/{model}")
        # Pydantic nests referenced models under $defs; OpenAPI wants them alongside.
        schemas.update(schema.pop("$defs", {}))
        schema.pop("title", None)  # the dict key already says what it is
        schemas[name] = schema

    return {
        "openapi": "3.1.0",
        "info": {
            "title": "Support API",
            "version": "0.2.3",
            "description": (
                "Customer support platform: read support tickets for customer accounts. "
                "Deployed to Azure Container Apps behind Microsoft Entra authentication; "
                "callers must present a token for this API's audience."
            ),
        },
        "servers": [{"url": server_url}],
        "paths": OPERATIONS,
        "components": {"schemas": schemas},
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--server-url", required=True)
    parser.add_argument("--out", type=Path, default=Path(__file__).parent / "openapi.yaml")
    args = parser.parse_args()

    spec = build_spec(args.server_url)
    args.out.write_text(
        yaml.safe_dump(spec, sort_keys=False, width=100, allow_unicode=True), encoding="utf-8"
    )
    operations = sum(len(methods) for methods in spec["paths"].values())
    print(f"Wrote {args.out}")
    print(f"  {operations} operations, {len(spec['components']['schemas'])} schemas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())