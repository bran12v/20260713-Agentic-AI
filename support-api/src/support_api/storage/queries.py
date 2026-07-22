import json 
import sqlite3
from typing import Any

def _row_to_ticket(row: sqlite3.Row) -> dict[str, Any]:
    """Maps a sqlite3.Row to a dict[str, Any]"""
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
        conn: sqlite3.Connection, 
        priority: str | None = None, 
        tenant: str | None = None, 
        status: str | None = None, 
        limit: int = 100
) -> list[dict[str, Any]]:
    """The service function that will facilitate getting and filtering a list of tickets."""
    where, params = [], []
    if priority:
        where.append("priority = ?") # placeholder string for the where which will be filled with
        params.append(priority) # the value of priority that we will be filter on
    if tenant:
        where.append("tenant = ?")
        params.append(tenant)
    if status:
        where.append("status = ?")
        params.append(status)

    sql = "SELECT * FROM tickets"
    if where:
        sql += " WHERE " + " AND ".join(where) # SELECT * FROM tickets WHERE priority = ?
    sql += " ORDER BY created_at DESC LIMIT ?" # sorts our results by when they were created in decending order
    params.append(limit)

    return [_row_to_ticket(row) for row in conn.execute(sql, params).fetchall()] # want to get a list of dicts not a list of sqlite3.Row's

def get_ticket(conn: sqlite3.Connection, ticket_id: str) -> dict[str, Any] | None:
    """Get an individual ticket by ID and return it as a dict."""
    row = conn.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    return _row_to_ticket(row) if row else None

def insert_ticket(conn: sqlite3.Connection, ticket: dict[str, Any]) -> None:
    """Insert a single ticket into the database based on the ticket dict provided."""
    conn.execute(
        """INSERT INTO tickets
            (id, title, body, priority, status, category, tenant, customer_id, assignee, channel, tags, created_at, updated_at)
            VALUES (:id, :title, :body, :priority, :status, :category, :tenant, :customer_id, :assignee, :channel, :tags, :created_at, :updated_at)
        """,
        {**ticket, "tags": json.dumps(ticket.get("tags", []))}
    )