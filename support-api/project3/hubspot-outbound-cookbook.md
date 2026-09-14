# HubSpot Outbound Cookbook

How the system talks back to HubSpot: emailing the person who opened the ticket, recording what it did
for the audit trail, and closing the ticket. Owned by **Edge & Approvals**.

Every call below was executed against live portal 51681374 and the request and response bodies are
what actually came back — not what the documentation implies.

> **Three operations, and the first two are the pair most likely to be confused.** A `MESSAGE` is
> delivered to the requester as email. A `COMMENT` is an internal note that is never emailed. Putting
> § 4.5's investigation summary in a `MESSAGE` mails your audit trail to the customer.

---

## Identifiers

**Four of these come off the ingest payload. Do not configure them by hand.**

| Value | Where it comes from | Sandbox value |
|---|---|---|
| `channelId` | `channel_id` on the ingest payload | `1002` |
| `channelAccountId` | `channel_account_id` on the ingest payload | `4021198932` |
| Thread id | `thread_id` on the ingest payload | `11178480985` |
| Recipient | The `HS_EMAIL_ADDRESS` delivery identifier off the **inbound** message — never from model output | `bvanek@skillstorm.com` |
| `senderActorId` | `A-<hubspotUserId>` for the account the token belongs to. Config | `A-47306113` |
| `inboxId` | The Help Desk inbox. Config, and needed only when creating a thread | `948000001` |

### Why the first two are payload values and not config

**`channelId` is a HubSpot-wide constant.** `GET /conversations/v3/conversations/channels` returns the
same fixed set in every portal, and `1002` is email:

```
1000 LIVE_CHAT      1003 FORMS                         1010 INSTAGRAM
1001 FB_MESSENGER   1004 CUSTOMER_PORTAL_THREAD_VIEW   1011 MIGRATION
1002 EMAIL          1007 WHATSAPP                      1009 SMS
```

**`channelAccountId` identifies one connected mailbox and is portal-specific.** This is the one that
bites. `GET /conversations/v3/conversations/channel-accounts` on portal 51681374 returns four email
accounts, and **three of them share the same inbox**:

| `id` | `channelId` | `inboxId` | Delivery identifier |
|---|---|---|---|
| **`4021198932`** | 1002 | **948000001** | **`helpdesk@skillstormlab.onmicrosoft.com`** ← ours |
| `3551452839` | 1002 | 948000001 | `support-3@skillstorm.com.hs-inbox.com` |
| `3558743646` | 1002 | 948000001 | `sample@51681374.hs-inbox.com` |
| `3551452842` | 1002 | 948000000 | `support-4@skillstorm.com.hs-inbox.com` |

Resolve the account by inbox id and take the first result and you send from `support-3@…` or
`sample@…`. **The API call succeeds.** Nothing fails, no error is logged, and the first sign of trouble
is a requester replying to an address nobody reads. Only `deliveryIdentifier.value` separates them.

So do not resolve it at all. **Every message on a thread carries both fields**, and the ingest action
copies them onto the payload:

```
direction=INCOMING   channelId=1002   channelAccountId=4021198932   bvanek@skillstorm.com
direction=OUTGOING   channelId=1002   channelAccountId=4021198932   helpdesk@skillstormlab...
```

Replying with the values the message arrived on is correct by construction, and it stays correct if
the mailbox is ever reconnected — which changes the id.

**The fallback.** A chat-sourced or manually created ticket has no thread, so both fields arrive null.
Only then fall back to configuration, and pin the configured value by delivery identifier rather than
by inbox.

---

## 1. Reply to the requester — sends email

This is what asks for missing information under § 4.1, delivers troubleshooting steps under § 4.4, and
says the work is finished.

```http
POST https://api.hubapi.com/conversations/v3/conversations/threads/{threadId}/messages
Authorization: Bearer {token}
Content-Type: application/json

{
  "type": "MESSAGE",
  "text": "Thanks - we need one more detail before we can continue. Which laptop model are you using?",
  "richText": "<p>Thanks - we need one more detail before we can continue. Which laptop model are you using?</p>",
  "senderActorId": "A-47306113",
  "channelId": "1002",
  "channelAccountId": "4021198932",
  "subject": "Re: TEST",
  "recipients": [
    {
      "actorId": "V-247729059090",
      "recipientField": "TO",
      "deliveryIdentifier": {
        "type": "HS_EMAIL_ADDRESS",
        "value": "bvanek@skillstorm.com"
      }
    }
  ]
}
```

**Verified response — `201`:**

```json
{
  "id": "900af967-abf7-4a4f-a5ce-50480d2f337f",
  "type": "MESSAGE",
  "direction": "OUTGOING",
  "status": { "statusType": "SENT" },
  "createdAt": "2026-09-13T21:36:56.548Z",
  "channelId": "1002",
  "channelAccountId": "4021198932",
  "truncationStatus": "TRUNCATED_TO_MOST_RECENT_REPLY"
}
```

The email arrived. `statusType: SENT` is the confirmation to assert on — a `201` alone only means
HubSpot accepted the message.

Both `text` and `richText` are worth sending. `text` is the plain-text part; `richText` is what a mail
client renders. Send only `text` and the email arrives unformatted.

---

## 2. Internal note — never emailed

Where § 4.5's investigation summary, proposed actions and approval outcome belong. Same endpoint,
different `type`, and **no recipients and no channel fields**.

```http
POST https://api.hubapi.com/conversations/v3/conversations/threads/{threadId}/messages
Authorization: Bearer {token}
Content-Type: application/json

{
  "type": "COMMENT",
  "text": "AI run 7f3a: investigated, 1 lane, proposed unlock.",
  "richText": "<p>AI run 7f3a: investigated, 1 lane, proposed unlock.</p>",
  "senderActorId": "A-47306113"
}
```

**Verified response — `201`:**

```json
{
  "id": "040fe7ea-50ba-459a-8573-1d00fb78b483",
  "type": "COMMENT",
  "conversationsThreadId": "11178480985",
  "createdAt": "2026-09-13T21:37:06.610Z",
  "createdBy": "I-52674089",
  "client": { "clientType": "INTEGRATION", "integrationAppId": 52674089 },
  "senders": [{ "actorId": "I-52674089" }],
  "recipients": [],
  "text": "AI run 7f3a: investigated, 1 lane, proposed unlock.",
  "type": "COMMENT"
}
```

Two things the response shows that the request does not:

**The sender is rewritten.** `senderActorId: "A-47306113"` was sent; HubSpot recorded
`I-52674089` — the integration's own actor id. Comments posted through a private app are attributed to
the app, not to a person. Do not assert on the actor you sent.

**There is no `direction` and no `recipients`.** That absence is what makes it internal, and it is also
why the ingest action ignores it.

> There is no separate comments endpoint. `POST .../threads/{id}/comments` returns **404** — the
> `type` field on the messages endpoint is the whole mechanism.

---

## 3. Close the ticket

Only two states matter: the ticket arrives in **New** and ends **closed**. Everything in between lives
on the run record in your own database — **no field is created on the ticket for this project.**

```http
PATCH https://api.hubapi.com/crm/v3/objects/tickets/{ticketId}
Authorization: Bearer {token}
Content-Type: application/json

{
  "properties": {
    "hs_pipeline_stage": "954564780"
  }
}
```

| Outcome | Stage | Id |
|---|---|---|
| Work finished | Resolved | `954564780` |
| Out-of-scope decline (§ 4.1) | Unresolvable | `954498199` |

Both are `ticketState: CLOSED` on pipeline `648529809`. **The stage is the only property this system
writes.** The correlation id that makes the write idempotent stays in your own store — HubSpot has no
field for it and none is being added.

---

## The loop this design avoids

The workflow re-enrolls on `hs_last_message_received_at` so that requester replies reach the system.
Our own outbound writes must not trip that, or the system ingests its own messages forever.

They do not, and it was checked rather than assumed. After posting both a `MESSAGE` and a `COMMENT`,
the ingest action was re-run against the same ticket:

```
event_id         48453757000:653c0c37-e4af-4e9b-af78-e80d19dc9363
kind             reply
message_id       653c0c37-e4af-4e9b-af78-e80d19dc9363     ← the requester's reply
```

Our outbound `900af967…` and our comment `040fe7ea…` were both ignored. Two independent guards make
that true, and **both must survive any refactor**:

1. The ingest action filters on `type === 'MESSAGE' && direction === 'INCOMING'`. A comment has no
   direction; an outbound reply has the wrong one.
2. `hs_last_message_received_at` only moves on inbound messages. The outbound reply moved
   `hs_last_message_sent_at` instead — a different property, which is why the workflow trigger must
   never be `hs_lastmodifieddate`.

---

## Wiring it into your service

Getting the config/payload split right is most of the work.

| Config (`pydantic-settings`) | Per-ticket (from the ingest payload) |
|---|---|
| `hubspot_sender_actor_id` · `hubspot_inbox_id` · the two stage ids · **fallback** channel values | `thread_id` · `requester_email` · `channel_id` · `channel_account_id` |

The channel values are in both columns on purpose: the payload carries them for every threaded ticket,
and the configured pair is used **only** when a chat-sourced or manual ticket arrives with both null.

**The token comes from Key Vault, never from an environment variable in code.** § 2.4 is keyless
throughout: fetch it with the managed identity at startup, and treat it as a secret with a rotation
date rather than a constant.

```python
import httpx
from pydantic import BaseModel

HUBSPOT_API = "https://api.hubapi.com"


class HubSpotConfig(BaseModel):
    sender_actor_id: str       # A-<hubspotUserId>
    resolved_stage_id: str     # 954564780
    declined_stage_id: str     # 954498199
    # Fallback only, for a ticket that arrived with no thread. Pin the account
    # by its delivery identifier, never by inbox — three accounts share ours.
    fallback_channel_id: str           # 1002
    fallback_channel_account_id: str   # 4021198932


class HubSpotClient:
    """Every method is idempotent on correlation_id. The store is yours."""

    def __init__(self, token: str, cfg: HubSpotConfig, store, client: httpx.AsyncClient):
        self._auth = {"Authorization": f"Bearer {token}"}
        self._cfg = cfg
        self._store = store          # (correlation_id, operation) -> hubspot id
        self._http = client

    def _channel(self, ticket) -> tuple[str, str]:
        """Reply on the account the message arrived on.

        Both are null only when the ticket had no thread. Resolving the account
        any other way is how you send from the wrong mailbox: the portal has four
        email channel accounts, three share one inbox, and the API accepts all of
        them without complaint.
        """
        return (
            ticket.channel_id or self._cfg.fallback_channel_id,
            ticket.channel_account_id or self._cfg.fallback_channel_account_id,
        )

    async def reply_to_requester(
        self, correlation_id: str, ticket, to_email: str, subject: str, body: str
    ) -> str:
        """Emails the requester. Use for clarifying questions and completion notices."""
        if existing := await self._store.get(correlation_id, "reply"):
            return existing

        channel_id, channel_account_id = self._channel(ticket)
        thread_id = ticket.thread_id
        payload = {
            "type": "MESSAGE",
            "text": body,
            # Without richText the email arrives unformatted.
            "richText": f"<p>{body}</p>",
            "senderActorId": self._cfg.sender_actor_id,
            "channelId": channel_id,
            "channelAccountId": channel_account_id,
            "subject": subject,
            "recipients": [{
                "recipientField": "TO",
                "deliveryIdentifier": {"type": "HS_EMAIL_ADDRESS", "value": to_email},
            }],
        }
        r = await self._http.post(
            f"{HUBSPOT_API}/conversations/v3/conversations/threads/{thread_id}/messages",
            headers=self._auth, json=payload, timeout=10.0,
        )
        r.raise_for_status()
        sent = r.json()

        # A 201 only means HubSpot accepted it. SENT is the delivery confirmation.
        if sent.get("status", {}).get("statusType") != "SENT":
            raise HubSpotDeliveryError(sent)   # your own exception type — see § 5

        await self._store.put(correlation_id, "reply", sent["id"])
        return sent["id"]

    async def add_internal_note(self, correlation_id: str, thread_id: str, body: str) -> str:
        """Never emailed. This is where the run summary goes."""
        if existing := await self._store.get(correlation_id, "note"):
            return existing

        # No recipients, no channel fields — that absence is what makes it internal.
        r = await self._http.post(
            f"{HUBSPOT_API}/conversations/v3/conversations/threads/{thread_id}/messages",
            headers=self._auth,
            json={
                "type": "COMMENT",
                "text": body,
                "richText": f"<p>{body}</p>",
                "senderActorId": self._cfg.sender_actor_id,
            },
            timeout=10.0,
        )
        r.raise_for_status()
        note_id = r.json()["id"]
        await self._store.put(correlation_id, "note", note_id)
        return note_id

    async def close_ticket(self, correlation_id: str, ticket_id: str, declined: bool) -> None:
        stage = self._cfg.declined_stage_id if declined else self._cfg.resolved_stage_id
        r = await self._http.patch(
            f"{HUBSPOT_API}/crm/v3/objects/tickets/{ticket_id}",
            headers=self._auth,
            json={"properties": {"hs_pipeline_stage": stage}},
            timeout=10.0,
        )
        r.raise_for_status()
```

**Four things that are easy to get wrong and hard to notice.**

`raise_for_status()` is not enough on the reply. A `201` means HubSpot accepted the message; only
`statusType: SENT` means it went out. Assert on it, or a silently undelivered email looks like success.

**Do not pass `actorId` in `recipients`.** Send the `deliveryIdentifier` only. The actor id is
per-contact, it is not on the ingest payload, and fetching it needs a contacts scope the token does
not hold.

**Retries respect `Retry-After`** and are bounded — § 5. Because every method checks the store first,
a retry after a partial failure returns the stored id rather than sending a second email.

**One store row per operation, not per correlation id.** A lane that asks a question, gets an answer
and later says it is finished writes two replies against the same run. Key on
`(correlation_id, operation)`, and make `operation` specific enough to distinguish them —
`reply:question` and `reply:complete` rather than `reply`.

---

## Resuming a conversation

The loop that carries a clarifying question through to an answer, end to end:

```
  lane needs information
        │
        ├─▶ reply_to_requester(...)          email leaves HubSpot
        │   ticket stays open in New; the lane's state is on the run record
        │
        │   ... hours pass ...
        │
        │   requester replies by email
        │        │
        │        ▼
        │   hs_last_message_received_at moves        ← the only property that does
        │        │
        │        ▼
        │   workflow re-enrolls, custom code fires
        │        │
        │        ▼
        └── POST /tickets/ingest  { kind: "reply", ticket_id, thread_id, body }
                 │
                 ▼
            look up the paused lane by ticket_id and resume it
```

Three things have to hold, and each is somewhere different:

1. **Re-enrollment fires** — on `hs_last_message_received_at`, never a thread id. Already configured
   in portal 51681374; see **Re-enrollment** below for why the alternatives fail silently.
2. **`kind` says `reply`** — the ingest action distinguishes a new request from an answer. Treating a
   reply as a new request restarts the investigation instead of resuming it, and the ticket never
   converges.
3. **The app correlates on `ticket_id`** and resumes that lane rather than opening one. This part is
   nobody else's job — the payload carries the id, and matching it to a paused run is the receiver's
   own work.

Our own outbound reply does not re-trigger any of this: it moves `hs_last_message_sent_at`, a
different property, and the ingest action filters it out by direction.

---

## Idempotency

**HubSpot has no idempotency key on messages, comments or property writes.** § 4.5 requires that a
retried update does not append a duplicate summary, so that guarantee is yours to build.

Keep a local table keyed on `(correlation_id, operation)` — checked before the call, written after a
`201`, storing the returned HubSpot id. A retry finds the row and returns the stored id instead of
posting again.

**Do not detect duplicates by searching note bodies.** It is slow, it breaks the moment anyone edits a
note, and it fails exactly when it matters — under a retry storm, when two workers race the same
correlation id.

---

## Environment

Portal **51681374** (sandbox) · workflow **HelpDesk Ticket Ingestion** `1882012709` · IT Service
pipeline **`648529809`** · connected inbox **`helpdesk@skillstormlab.onmicrosoft.com`**.

That inbox address matters beyond addressing: § 2.3 of the brief rests the requester's identity on
SPF, DKIM and DMARC being enforced there, and with approval gated to three lifecycle operations the
entitlement check is the only other control on that path.

| State | Stage | Id |
|---|---|---|
| Arrived | New | `954564777` |
| Work finished | Resolved | `954564780` |
| Out-of-scope decline | Unresolvable | `954498199` |

The other three stages — Assigned `954564778`, WIP `954564779`, Pending Stormer `954498198` — exist
and are left alone. **A ticket waiting on an approver or on a requester's reply stays in New**; that
state is on the run record, not in HubSpot. Do not repurpose the unused stages to carry it — the
HelpDesk team reads the same board, and a stage that means something only to this system is a
consistency problem rather than a feature.

### Re-enrollment

The ingestion workflow enrolls on pipeline `IT Service`, and **re-enrolls on
`hs_last_message_received_at`** with a second filter of `hs_last_message_from_visitor is true`. Both
halves are load-bearing and both failure modes are silent:

- **Never re-enroll on a conversation or thread id.** `hs_conversations_originating_thread_id` is
  stamped once at ticket creation and never changes, so a trigger on it can never fire. New tickets
  flow through perfectly while every reply is dropped, and nothing errors.
- **Never trigger on `hs_lastmodifieddate`.** It moves on the system's own writes, so the system
  ingests its own replies forever.
- The `from_visitor` filter is what keeps outbound `MESSAGE` writes from re-enrolling the ticket.

### What this system writes to HubSpot

**Three things.** A `MESSAGE` on the thread, a `COMMENT` on the thread, and `hs_pipeline_stage` on the
ticket. Everything else the system knows — which lane is waiting on whom, the correlation id, the
decline reason, the requester's laptop model, the target of the request — lives on the run record in
your own database.

So HubSpot needs no administration and there is nothing to hold consistent between two systems. The
cost is that **HubSpot shows an open ticket and nothing else while a run is in flight**: the internal
note is the only place a human can see what happened. Write it for them.

Two properties on the ticket look useful and are not. `hs_ticket_category` carries HubSpot's stock
options — Product issue, Billing issue, Feature request, General inquiry — none of which distinguish a
lockout from a laptop fault, and it is unpopulated on every ticket examined. `hs_ticket_priority` is
unpopulated too. The system reads neither.

---

## Scopes

The private app needs `conversations.read`, `conversations.write`, `crm.objects.tickets.read` and
`crm.objects.tickets.write`. The current token holds all four.

It does **not** hold `automation`, which is why the workflow cannot be read or configured through the
API. That part is UI work and is already done in the sandbox portal.
