CREATE TABLE IF NOT EXISTS customers (
    id                      TEXT PRIMARY KEY,
    name                    TEXT NOT NULL,
    tenant                  TEXT NOT NULL,
    plan                    TEXT NOT NULL CHECK (plan IN ('starter', 'business', 'enterprise')),
    primary_contact_email   TEXT,
    created_at              TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS ix_customers_tenant ON customers(tenant);

CREATE TABLE IF NOT EXISTS tickets (
    id              TEXT PRIMARY KEY,
    title           TEXT NOT NULL,
    body            TEXT NOT NULL,
    priority        TEXT NOT NULL CHECK (priority IN ('urgent', 'high', 'normal', 'low')),
    status          TEXT NOT NULL CHECK (status IN ('open', 'in_progress', 'waiting_on_customer', 'resolved', 'closed')),
    category        TEXT NOT NULL CHECK (category IN ('billing', 'technical', 'account', 'general')),
    tenant          TEXT NOT NULL,
    customer_id     TEXT NOT NULL REFERENCES customers(id) ON DELETE CASCADE, -- foreign key
    assignee        TEXT,
    channel         TEXT NOT NULL CHECK (channel IN ('email', 'chat', 'phone', 'portal')),
    tags            TEXT NOT NULL DEFAULT '[]',
    created_at      TEXT NOT NULL,
    updated_at      TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS ix_tickets_tenant       ON tickets(tenant);
CREATE INDEX IF NOT EXISTS ix_tickets_status       ON tickets(status);
CREATE INDEX IF NOT EXISTS ix_tickets_priority     ON tickets(priority);
CREATE INDEX IF NOT EXISTS ix_tickets_customer_id  ON tickets(customer_id);

CREATE TABLE IF NOT EXISTS conversation_turns (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id       TEXT NOT NULL REFERENCES tickets(id) ON DELETE CASCADE,
    turn_type       TEXT NOT NULL CHECK (turn_type IN ('customer_message', 'agent_reply', 'internal_note', 'system_event', 'llm_draft')),
    author          TEXT NOT NULL,
    body            TEXT NOT NULL,
    created_at      TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS ix_turns_ticket_id ON conversation_turns(ticket_id);