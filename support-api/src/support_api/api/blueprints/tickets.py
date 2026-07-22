from flask import Blueprint, request
from datetime import datetime, timezone 
from support_api.filters import filter_by_priority, filter_by_tenant, load_tickets
from support_api.models import TicketCreate
from support_api.api.errors import TicketNotFound
# A blueprint is a group of routes that we attach to the app
bp = Blueprint("tickets", __name__)

@bp.route("", methods=["GET"]) # url endpoint, and HTTP verbs usable by this route # localhost:5000/
def list_tickets():
    """GET /tickets
        returns all tickets in the DB/JSON file.
    """
    # Gets all tickets
    tickets = load_tickets()

    # filters the total tickets down by priority
    priority = request.args.get("priority")
    if priority:
        tickets = filter_by_priority(tickets, priority)

    # filters the total tickets down by tenant
    tenant = request.args.get("tenant")
    if tenant:
        tickets = filter_by_tenant(tickets, tenant)
    
    return { "count": len(tickets), "items": tickets }

@bp.route("/<ticket_id>", methods=["GET"]) # /tickets/TKT-10001
def get_ticket(ticket_id: str):
    """GET /tickets/{id}
        returns an individual ticket based on the ID provided.
    """
    tickets = load_tickets()
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket # 200 OK
    raise TicketNotFound(ticket_id) # 404 not found

# NEW (W2 D2) — same URL as list_tickets, different verb.
@bp.route("", methods=["POST"])
def create_ticket():
    # silent=True → None on bad body; `or {}` → Pydantic reports EVERY
    # missing field, not just "body can't be None".
    data = TicketCreate.model_validate(request.get_json(silent=True) or {})

    # ISO-8601 with trailing Z, the canonical API timestamp format.
    now = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    existing = load_tickets()
    return (
        {
            **data.model_dump(),     # spread validated fields
            "id": f"TKT-{10001 + len(existing):05d}",
            "created_at": now,
            "updated_at": now,
        },
        201,                         # 201 Created
    )