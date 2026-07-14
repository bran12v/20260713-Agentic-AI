"""Pure filter, and info return file for getting information on tickets."""

from pathlib import Path
import json
from typing import Iterable, Any, Callable

TicketDict = dict[str, Any]

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
# C:\Users\BrandonVanek\Desktop\AI Dev\20260713 Guidehouse\support-platform\support-api\data
# C:\Users\BrandonVanek\Desktop\20260713 Guidehouse\support-platform\support-api\src\support_api\filters.py

def load_tickets(path: Path | None = None) -> list[dict]:
    """Load the seed (tickets.json) into memory as a list of dicts."""
    target = path or (DATA_DIR / "tickets.json") 
    # C:\Users\BrandonVanek\Desktop\20260713 Guidehouse\support-platform\support-api\data\tickets.json - Default
    with target.open(encoding="utf-8") as fh:
        return json.load(fh) 
        # this returns the info in tickets.json as a list[dict]

# filter by priority
def filter_by_priority(tickets:  Iterable[TicketDict], priority: str) -> list[dict]:
    """Return tickets whose priority matches the given value. Case-Insensitive."""
    desired = priority.lower() # all lowercase
    return [ticket for ticket in tickets if ticket.get("priority", "").lower() == desired] # list comprehension, gather all the dict that meet the condition into a new dict

# filter by tenant
def filter_by_tenant(tickets:  Iterable[TicketDict], tenant: str) -> list[dict]:
    """Return tickets scoped to one tenant. Tenant Isolation."""
    return [ticket for ticket in tickets if ticket.get("tenant", "") == tenant] # ticket["tenant"]

def created_at(ticket: TicketDict):
    """Sort key: pull the timestamp that 'sorted()' should order the tickets by."""
    created: str = ticket["created_at"]
    return created

def most_recent(tickets: Iterable[TicketDict], n: int = 5):
    """Return the n most recently created tickets."""
    return sorted(tickets, key=created_at, reverse=True)[:n]

def format_ticket_row(ticket: TicketDict) -> str:
    """Return a one-line human-readable summary of a ticket."""
    short_title = ticket["title"]
    if len(short_title) > 50:
        short_title = short_title[:47] + "..."
    return (
        f"{ticket['id']:<10}"
        f"{ticket['priority']:<8}"
        f"{ticket['status']:<20}"
        f"{short_title}"
    )

# higher order functions and closures
def matches(
    predicate: Callable[[TicketDict], bool],
) -> Callable[[list[TicketDict]], list[TicketDict]]:
    """Return a filter function scoped to a single predicate.
    
    This is a closure: the returned function rememberes the predicate.
    """

    def apply(tickets: list[TicketDict]) -> list[TicketDict]:
        return [ticket for ticket in tickets if predicate(ticket)]
    
    return apply

if __name__ == "__main__":
    tickets = load_tickets()

    # lambda function, anonymous function that allows you to create and run/pass a function in-line
    is_urgent = matches(lambda ticket: ticket["priority"] == "urgent") 
    is_billing = matches(lambda ticket: ticket["category"] == "billing")
    is_high_billing = matches(lambda ticket: ticket["priority"] == "high" and ticket["category"] == "billing")
    # remember this also returns a function ^
    print(len(is_urgent(tickets)))
    print(len(is_billing(tickets)))
    print(len(is_high_billing(tickets)))

    # print("\n=== 5 most recent tickets ===")
    # for ticket in most_recent(tickets, n=5):
    #     print(format_ticket_row(ticket))

    # print("\n === 10 most recent urgent tickets ===")
    # for ticket in most_recent(filter_by_priority(tickets, "urgent"), n=10):
    #     print(format_ticket_row(ticket))

    # print(len(tickets))
    # print(type(tickets))
    # print(type(tickets[0]))
    # print(json.dumps(tickets[0], indent=2))

    # List comprehension
    # A list of Titles of   all urgent tickets
    # [(What is being returned) (What is being iterated over) (The condition for return)]
    urgent_titles: list[str] = [ticket["title"] for ticket in tickets if ticket.get("priority", "") == "urgent"] 
    # print(f"Urgent tickets: {urgent_titles}") # __len__ dunder functions

    # Set comprehension
    tenants = {ticket["tenant"] for ticket in tickets}
    # print(f"Tenants: {sorted(tenants)}")

    # dict comprehension
    # {"TKT-10001": "Broke my machine"}
    title_by_id = {ticket["id"]: ticket["title"] for ticket in tickets}
    # print(f"Lookup TKT-10005 {title_by_id.get("TKT-10005", "Not Found")}")

    # nested comprehension: all unique tags for all tickets
    all_tags = {tag for ticket in tickets for tag in ticket.get("tags", [])}
    # print(f"Tags: {sorted(all_tags)[2:5]}") # slicing
    
    urgent = filter_by_priority(tickets, "urgent")
    # print(f"Urgent: {len(urgent)}")

    acme = filter_by_tenant(tickets, "acme-corp")
    # print(f"acme-corp tickets: {len(acme)}")

