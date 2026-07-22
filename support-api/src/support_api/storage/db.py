import sqlite3
import json
from pathlib import Path

# schema path
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"
# DB path
DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent.parent.parent / "tickets.db"
# Data path
_DATA_DIR = Path(__file__).resolve().parent.parent.parent.parent / "data"

# connection
def connect(db_path: Path | str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row # w/o this rows come back as tuples rather than dict
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# initialize db
def init_db(db_path: Path | str = DEFAULT_DB_PATH) -> None:
    conn = connect(db_path)
    try:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8")) # read in all the schema DDL for our tables and execute it 
        conn.commit()
    finally:
        conn.close()

# seed db w/ data
def seed_from_json(db_path: Path | str = DEFAULT_DB_PATH) -> tuple[int, int]:
    customers = json.loads((_DATA_DIR / "customers.json").read_text(encoding="utf-8"))
    tickets = json.loads((_DATA_DIR / "tickets.json").read_text(encoding="utf-8"))
    conn = connect(db_path)
    try:
        # Customers
        conn.executemany(
            """
                INSERT OR REPLACE INTO customers
                    (id, name, tenant, plan, primary_contact_email, created_at)
                    VALUES (:id, :name, :tenant, :plan, :primary_contact_email, :created_at)
            """, customers
        )
        # Tickets
        conn.executemany(
            """
                INSERT OR REPLACE INTO tickets
                    (id, title, body, priority, status, category, tenant, customer_id, assignee, channel, tags, created_at, updated_at) VALUES (:id, :title, :body, :priority, :status, :category, :tenant, :customer_id, :assignee, :channel, :tags, :created_at, :updated_at)
            """, [{**ticket, "tags": json.dumps(ticket.get("tags", []))} for ticket in tickets]
        )
        conn.commit()
    finally:
        conn.close()
    return len(customers), len(tickets)
