import psycopg
from psycopg.rows import dict_row
import os
import json
from pathlib import Path
import time

# schema path
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"
# DB URL - local version
_DEFAULT_DATABASE_URL = "postgresql://support:support_dev@localhost:5432/support"
# Data path
_DATA_DIR = Path(__file__).resolve().parent.parent.parent.parent / "data"

_POSTGRS_TOKEN_SCOPE = "https://ossrdbms-aad.database.windows.net/.default"

_TOKEN_REFRESH_SECONDS = 300 # TTL of 5mins

_token_cache: tuple[str, float] | None = None

# def _resolve_db_url(database_url: str | None) -> str:
#     """Priority: Explicit arg > DATABASE_URL env > Module default"""
#     return database_url or os.environ.get("DATABASE_URL") or _DEFAULT_DATABASE_URL

def _resolve_data_dir() -> Path:
    """Priority: DATA_DIR env > module default"""
    return Path(os.environ.get("DATA_DIR") or _DATA_DIR)

def _entra_access_token() -> str:
    """Fetch (and cache) an Entra access token to use in place of a tradtional password."""
    global _token_cache
    if _token_cache is not None:
        token, expires_on = _token_cache
        if time.time() < expires_on - _TOKEN_REFRESH_SECONDS:
            return token

    from azure.identity import DefaultAzureCredential

    fetched = DefaultAzureCredential().get_token(_POSTGRS_TOKEN_SCOPE) # specifically gets permissions to access our DB.

    _token_cache = (fetched.token, float(fetched.expires_on))
    return fetched.token

# connection
def connect(database_url: str | None = None) -> psycopg.Connection:
    """Open a psycopg connection with rows as dicts, so callers can keep using row['id']"""

    explicit = database_url or os.environ.get("DATABASE_URL")
    if explicit:
        return psycopg.connect(
            explicit,
            row_factory=dict_row, # turns every row returned by this connection into dicts
        )

    #prod
    if os.environ.get("PGHOST"):
        return psycopg.connect(
            host=os.environ["PGHOST"],
            dbname=os.environ.get("PGDATABASE", "support"),
            user=os.environ["PGUSER"],
            password=_entra_access_token(),
            sslmode=os.environ.get("PGSSLMODE", "require"),
            connect_timeout=10,
            row_factory=dict_row
        )
    
    return psycopg.connect(_DEFAULT_DATABASE_URL, row_factory=dict_row) # hit for local testing

# initialize db
def init_db(database_url: str | None = None) -> None:
    """Run schema.sql. Idempotent - the schema is all CREATE .... IF NOT EXISTS"""
    conn = connect(database_url)
    try:
        with conn.cursor() as cur:
            cur.execute(SCHEMA_PATH.read_text(encoding="utf-8")) # read in all the schema DDL for our tables and execute it 
        conn.commit()
    finally:
        conn.close()

# seed db w/ data
def seed_from_json(database_url: str | None = None) -> tuple[int, int]:
    data_dir = _resolve_data_dir()
    customers = json.loads((data_dir / "customers.json").read_text(encoding="utf-8"))
    tickets = json.loads((data_dir / "tickets.json").read_text(encoding="utf-8"))

    conn = connect(database_url)
    try:
        with conn.cursor() as cur:
            # Customers
            cur.executemany(
                """
                    INSERT INTO customers
                        (id, name, tenant, plan, primary_contact_email, created_at)
                    VALUES (%(id)s, %(name)s, %(tenant)s, %(plan)s, %(primary_contact_email)s, %(created_at)s)
                    ON CONFLICT (id) DO UPDATE SET
                        name = EXCLUDED.name,
                        tenant = EXCLUDED.tenant,
                        plan = EXCLUDED.plan,
                        primary_contact_email = EXCLUDED.primary_contact_email,
                        created_at = EXCLUDED.created_at
                """, customers
            )
            # Tickets
            cur.executemany(
                """
                    INSERT INTO tickets
                        (id, title, body, priority, status, category, tenant, customer_id, assignee, channel, tags, created_at, updated_at) 
                    VALUES (%(id)s, %(title)s, %(body)s, %(priority)s, %(status)s, %(category)s, %(tenant)s, %(customer_id)s, %(assignee)s, %(channel)s, %(tags)s, %(created_at)s, %(updated_at)s)
                    ON CONFLICT (id) DO UPDATE SET
                        title = EXCLUDED.title,
                        body = EXCLUDED.body,
                        priority = EXCLUDED.priority,
                        status = EXCLUDED.status,
                        category = EXCLUDED.category,
                        tenant = EXCLUDED.tenant,
                        customer_id = EXCLUDED.customer_id,
                        assignee = EXCLUDED.assignee,
                        channel = EXCLUDED.channel,
                        tags = EXCLUDED.tags,
                        updated_at = EXCLUDED.updated_at
                """, [{**ticket, "tags": json.dumps(ticket.get("tags", []))} for ticket in tickets]
            )
        conn.commit()
    finally:
        conn.close()
    return len(customers), len(tickets)
