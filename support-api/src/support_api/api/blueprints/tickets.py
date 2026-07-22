from flask import Blueprint, request, current_app, g
from datetime import datetime, timezone 
from support_api.filters import filter_by_priority, filter_by_tenant, load_tickets
from support_api.storage import queries
from support_api.models import TicketCreate
from support_api.api.errors import TicketNotFound
# A blueprint is a group of routes that we attach to the app
bp = Blueprint("tickets", __name__)

def _db():
    if "db" not in g:
        from support_api.storage import connect
        g.db = connect(current_app.config["DB_PATH"]) # ref our flask env variables
    return g.db

@bp.route("", methods=["GET"]) # url endpoint, and HTTP verbs usable by this route # localhost:5000/
def list_tickets():
    """GET /tickets
        returns all tickets in the DB/JSON file.
    """
    tickets = queries.list_tickets(
        _db(),
        priority=request.args.get("priority"),
        tenant=request.args.get("tenant"),
        status=request.args.get("status"),
        limit=int(request.args.get("limit", 100)),
    )
    return { "count": len(tickets), "items": tickets }

@bp.route("/<ticket_id>", methods=["GET"]) # /tickets/TKT-10001
def get_ticket(ticket_id: str):
    """GET /tickets/{id}
        returns an individual ticket based on the ID provided.
    """
    ticket = queries.get_ticket(_db(), ticket_id)
    if ticket is None:
        raise TicketNotFound(ticket_id) # 404 not found
    return ticket

# NEW (W2 D2) — same URL as list_tickets, different verb.
@bp.route("", methods=["POST"])
def create_ticket():
    # silent=True → None on bad body; `or {}` → Pydantic reports EVERY
    # missing field, not just "body can't be None".
    data = TicketCreate.model_validate(request.get_json(silent=True) or {})
    conn = _db()
    count = conn.execute("SELECT COUNT(*) AS n FROM tickets").fetchone()["n"] # how many tickets are in the database
    now = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

    new_ticket = {
        **data.model_dump(),     # spread validated fields
        "id": f"TKT-{10001 + count:05d}", # this probably needs to be changed longterm
        "created_at": now,
        "updated_at": now,
    }
    queries.insert_ticket(conn, new_ticket)
    conn.commit()
    return new_ticket, 201