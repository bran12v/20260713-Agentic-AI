from dotenv import load_dotenv
import logging
import asyncio
import os
import sys
from typing import cast

from agent_framework import Message
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
from agent_framework.orchestrations import HandoffBuilder
from agent_framework import WorkflowConvergenceException

load_dotenv()

# Agent replies contain typographic dashes; keep piped/redirected output from
# dying on a cp1252 console.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# intake, inbound cases to evaluate:
CASES = [
    """Supervisory query SUP-2291: our archive vendor confirms instant-message
    records from the decommissioned Symphony tenant are recoverable in 14 days,
    not 72 hours. Do we need to notify anyone before the 2027-01-01 date?""",

    """Alert AML-8807: a corporate client moved EUR 412,000 through three
    intermediaries in 48 hours, two of them in jurisdictions on our enhanced
    due diligence list. The relationship manager wants the fourth payment
    released today.""",

    """Incident INC-5540: overnight reconciliation shows GBP 180,000 of client
    money sitting in a firm account for six working days. The counterparty that
    sent it is on our sanctions screening watchlist and the payment reference
    was blank.""",
]

# Every specialist ends its reply with this line 
# if they do not need to route so the agent can stop its process.
class TerminalAgentFilter(logging.Filter):
    """Drop the builder's warning about agents with no outgoing handoff edges.

    record_retention is deliberately terminal: it owns its regulation end to end
    and always signs off, so it has nothing to route to. HandoffBuilder cannot tell
    that apart from a dead end and warns once per build. Filtered on the specific
    message rather than by silencing the logger, so its other warnings still show.
    """

    def filter(self, record: logging.LogRecord) -> bool:
        return "No handoff configuration found for agent" not in record.getMessage()


logging.getLogger("agent_framework_orchestrations._handoff").addFilter(TerminalAgentFilter())


SENTINEL = "CASE ASSIGNED"

RULE = "-" * 60

SPECIALISTS = {"record_retention", "financial_crime", "client_assets"}


def case_is_closed(conversation: list[Message]) -> bool:
    """Stop on a sign-off, or once the specialists have had their say.

    Financial Crime and Client Assets can each hand to the other, which is what
    lets triage route either one first. Nothing in HandoffBuilder bounds that
    cycle: HandoffAgentExecutor resets an agent's autonomous turn counter on every
    handoff, so per-agent turn limits never bite and the two will pass the case
    back and forth until the runner gives up 100 supersteps later. The bound lives
    here instead - the edge stays open, but the workflow stops once two specialist
    replies are on record, whether that is both halves of the case covered or one
    specialist repeating itself.
    """
    if not conversation:
        return False
    if SENTINEL in (conversation[-1].text or "").upper():
        return True
    spoken = [m for m in conversation if m.author_name in SPECIALISTS and m.text]
    return len(spoken) >= 2


async def main() -> None:
    client = FoundryChatClient(
        project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
        model="claude-haiku-4-5", #or os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        credential=AzureCliCredential()
    )

    # Front Door, intake agent.
    triage = client.as_agent(
        name="triage",
        description="Supervisory intake desk. Routes each case to its owning specialist.",
        instructions="You are a supervisory intake desk. Read the case and hand it to "
        "the ONE specialist who owns that regulation. ALWAYS hand off; never answer the "
        "case yourself, and never hand off to more than one specialist. Before handing "
        "off, say one short sentence naming who you are handing to and why.",
        require_per_service_call_history_persistence=True
    )

    # record retention
    record_retention = client.as_agent(
        name="record_retention",
        description="Owns MiFID communications recording and retention obligations.",
        instructions="You own MiFID communcations recording and retention. Take " \
        "ownership of the case, state the single next control action in one sentence " \
        f"starting with a verb, then end your reply with the line: {SENTINEL}",
        require_per_service_call_history_persistence=True
    )

    def transfer_rule(counterpart: str, counterpart_owns: str) -> str:
        """Let a specialist pass the case on instead of signing off."""
        return (
            "NEVER hand off silently: always write your own control action as text "
            "first, in the same reply, and only then call the handoff tool. A reply "
            "with no text is a failure. "
            "The triage desk is NOT a specialist - being handed the case by triage "
            "does not make you the final owner. If the case also raises "
            f"{counterpart_owns}, hand it to {counterpart} after stating your own "
            "action, and do NOT write the sign-off line yourself. Hand off at most "
            "once, and never back to a specialist who has already spoken on this "
            f"case - if {counterpart} has already spoken, you are the final owner. "
            f"Write the line {SENTINEL} only when no other specialist has an "
            "obligation here."
        )

    # financial crime
    financial_crime = client.as_agent(
        name="financial_crime",
        description="Owns anti-money-laundering and sanctions screening obligations.",
        instructions="You own anti-money-laundering and sanctions screening. Take "
        "ownership of the case and state the next control action in one sentence "
        "starting with a verb. " + transfer_rule(
            "Client Assets",
            "client money sitting in the wrong account, or a segregation or "
            "reconciliation obligation",
        ),
        require_per_service_call_history_persistence=True
    )

    # client assets
    client_assets = client.as_agent(
        name="client_assets",
        description="Owns CASS client money segregation and reconciliation.",
        instructions="You own CASS client money segregation and reconciliation. Take "
        "ownership of the case and state the next control action in one sentence "
        "starting with a verb. " + transfer_rule(
            "Financial Crime",
            "a sanctions watchlist hit, screening gap or suspected money "
            "laundering",
        ),
        require_per_service_call_history_persistence=True
    )

    desk = [triage, record_retention, financial_crime, client_assets]

    for case_number, case in enumerate(CASES, start=1):
        """Each case will get a fresh workflow because the handoff builder presists the 
            state/session across runs."""
        workflow = (
            HandoffBuilder(
                name="supervisory_intake",
                participants=desk,
                # Stop on sign-off, or once the cycle has been walked once.
                termination_condition=case_is_closed,
            )
            # which agent starts the workflow? (START sentinel)
            .with_start_agent(triage)
            # Which agents route to which other agents? (edges)
            .add_handoff(triage, [record_retention, financial_crime, client_assets])
            .add_handoff(financial_crime, [client_assets])
            .add_handoff(client_assets, [financial_crime])
            # How does it run?
            .with_autonomous_mode(turn_limits={agent.name: 2 for agent in desk})
            .build()
        )
        print(f"{'=' * 60}\nCASE {case_number}\n{'=' * 60}")
        try:
            result = await workflow.run(f"Inbound Case: {case}")
        except WorkflowConvergenceException as exc:
            # Two specialists kept handing the case back and forth without either
            # signing off. Surface the livelock instead of silently burning turns.
            print(f"LIVELOCK: no owner signed off - {exc}")
            continue
        messages = [
            message
            for response in result.get_outputs()
            for message in cast(list[Message], response.messages)
        ]
        i = 1
        for message in messages:
            # Text-less messages are the handoff tool traffic itself: the routing
            # decision rides in a function_result, not in the assistant text.
            text = (message.text or "").strip()
            if not text:
                continue
            name = message.author_name or "assistant"
            print(f"{RULE}\n{i:02d} [{name}]\n {text}")
            i += 1


if __name__ == "__main__":
    asyncio.run(main())