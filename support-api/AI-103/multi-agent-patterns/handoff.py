from dotenv import load_dotenv
import asyncio
import logging
import os
import sys
from typing import cast

from agent_framework import Message
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
from agent_framework.orchestrations import HandoffBuilder

load_dotenv()

# record_retention is terminal by design - it always signs off, so it has no
# outgoing handoffs and the builder warns about it once per case.
logging.getLogger("agent_framework_orchestrations._handoff").setLevel(logging.ERROR)

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
SENTINEL = "CASE ASSIGNED"


def case_is_closed(conversation: list[Message]) -> bool:
    """Stop on a sign-off, or once two specialists have replied.

    financial_crime and client_assets can each hand to the other, and nothing in
    HandoffBuilder bounds that: it resets an agent's turn counter on every handoff,
    so turn_limits never bite and the two loop until the runner gives up. Two
    specialist replies means the case is covered - or that the desk is circling.
    """
    if not conversation:
        return False
    if SENTINEL in (conversation[-1].text or "").upper():
        return True
    # Require text: a handoff is a tool call, and that message has an author but
    # no text, so counting it would end the case a hop early.
    replies = [m for m in conversation if m.text and m.author_name not in (None, "triage")]
    return len(replies) >= 2


async def main() -> None:
    client = FoundryChatClient(
        project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
        model="gpt-5-mini", #os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        credential=AzureCliCredential()
    )

    # Front Door, intake agent.
    triage = client.as_agent(
        name="triage",
        description="Supervisory intake desk. Routes each case to its owning specialist.",
        instructions="You are a supervisory intake desk. Read the case and hand it to "
        "the ONE specialist who owns that regulation. ALWAYS hand off; never answer the case"
        "yourself, and never hand off to more than one specialist. Before handing off, "
        "say one short sentance naming who you are handing to and why.",
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

    TRANSFER_RULE = (
        "NEVER hand off silently: write your control action as text first, in the " \
        "same reply, and only then call the handoff tool. A reply with no text is a " \
        "failure. The triage desk is NOT a specialist - being handed the case by " \
        "triage does not make you the final owner. If the case also raises an " \
        "obligation another specialist owns, do your own part first and then hand " \
        "the case to them instead of signing off. Hand off at most once: if " \
        "another specialist has already replied on this case, you are the final " \
        f"owner and must end your reply with the line: {SENTINEL}"
    )

    # financial crime
    financial_crime = client.as_agent(
        name="financial_crime",
        description="Owns anti-money-laundering and sanctions screening obligations.",
        instructions="You own anti-money-laundering and sanctions screening. Take " \
        "ownership of the case and state the next control action in one sentence " \
        f"starting with a verb. {TRANSFER_RULE}",
        require_per_service_call_history_persistence=True
    )

    # client assets
    client_assets = client.as_agent(
        name="client_assets",
        description="Owns CASS client money segregation and reconciliation.",
        instructions="You own CASS client money segregation and reconciliation. Take " \
        "ownership of the case and state the next control action in one sentence " \
        f"starting with a verb. {TRANSFER_RULE}",
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
                # Stop as soon as an owner signs off, or the desk starts circling.
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
        result = await workflow.run(f"Inbound Case: {case}")

        print(f"{'=' * 60}\nCASE {case_number}\n{'=' * 60}")
        i = 1
        for response in result.get_outputs():
            for message in cast(list[Message], response.messages):
                if not (message.text or "").strip():
                    continue  # handoff tool call - no text to show
                name = message.author_name or "assistant"
                print(f"{'-' * 60}\n{i:02d} [{name}]\n {message.text}")
                i += 1


if __name__ == "__main__":
    asyncio.run(main())
