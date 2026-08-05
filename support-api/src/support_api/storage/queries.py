import json 
import psycopg
from typing import Any

def _row_to_ticket(row: dict[str, Any]) -> dict[str, Any]:
    """Maps a psycopg dict row to a dict[str, Any]"""
    return {
        "id": row["id"],
        "title": row["title"],
        "body": row["body"],
        "priority": row["priority"],
        "status": row["status"],
        "category": row["category"],
        "tenant": row["tenant"],
        "customer_id": row["customer_id"],
        "assignee": row["assignee"],
        "channel": row["channel"],
        "tags": json.loads(row["tags"]),
        "created_at": row["created_at"],
        "updated_at": row["updated_at"],
    }

def list_tickets(
        conn: psycopg.Connection, 
        priority: str | None = None, 
        tenant: str | None = None, 
        status: str | None = None, 
        limit: int = 100
) -> list[dict[str, Any]]:
    """The service function that will facilitate getting and filtering a list of tickets."""
    where, params = [], []
    if priority:
        where.append("priority = %s") # placeholder string for the where which will be filled with
        params.append(priority) # the value of priority that we will be filter on
    if tenant:
        where.append("tenant = %s")
        params.append(tenant)
    if status:
        where.append("status = %s")
        params.append(status)

    sql = "SELECT * FROM tickets"
    if where:
        sql += " WHERE " + " AND ".join(where) # SELECT * FROM tickets WHERE priority = %s
    sql += " ORDER BY created_at DESC LIMIT %s" # sorts our results by when they were created in decending order
    params.append(limit)

    return [_row_to_ticket(row) for row in conn.execute(sql, params).fetchall()] # want to get a list of dicts not a list of sqlite3.Row's

def get_ticket(conn: psycopg.Connection, ticket_id: str) -> dict[str, Any] | None:
    """Get an individual ticket by ID and return it as a dict."""
    row = conn.execute("SELECT * FROM tickets WHERE id = %s", (ticket_id,)).fetchone()
    return _row_to_ticket(row) if row else None

def insert_ticket(conn: psycopg.Connection, ticket: dict[str, Any]) -> None:
    """Insert a single ticket into the database based on the ticket dict provided."""
    conn.execute(
        """INSERT INTO tickets
            (id, title, body, priority, status, category, tenant, customer_id, assignee, channel, tags, created_at, updated_at)
            VALUES (%(id)s, %(title)s, %(body)s, %(priority)s, %(status)s, %(category)s, %(tenant)s, %(customer_id)s, %(assignee)s, %(channel)s, %(tags)s, %(created_at)s, %(updated_at)s)
        """,
        {**ticket, "tags": json.dumps(ticket.get("tags", []))}
    )