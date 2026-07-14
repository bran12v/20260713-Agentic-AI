import json
from pathlib import Path
from typing import Iterator, Callable, Any, Iterable

from support_api.filters import DATA_DIR, TicketDict

def stream_tickets(path: Path | None = None) -> Iterator[TicketDict]:
    """Yield one ticket at a time from the JSON file.
    
    Currently, the file in its entirety is loaded into memory (not incremental). No ability
    to short circuit the process.
    """
    target = path or (DATA_DIR / "tickets.json") 
    with target.open(encoding="utf-8") as fh:
        for ticket in json.load(fh):
            yield ticket # the yield keyword returns the tickets, one at a time when called


# where - filter
def where(
    tickets: Iterable[TicketDict],
    predicate: Callable[[TicketDict], bool]
) -> Iterator[TicketDict]: # generator
    """Filter a ticket stream by an arbitrary predicate (condition function)."""
    for ticket in tickets:
        if predicate(ticket):
            yield ticket # halts the loop, and returns, when called again starts where it halted

# tag - add a field without mutating the input
def tag(
    tickets: Iterable[TicketDict],
    field: str,
    compute: Callable[[TicketDict], Any]
) -> Iterator[TicketDict]:
    """Add a computed field on each ticket without modifying the original input"""
    for ticket in tickets:
        yield {**ticket, field: compute(ticket)}

# take - return the first n tickets from the stream
def take(
    tickets: Iterable[TicketDict], 
    n: int
) -> list[TicketDict]:
    """Materialize the first n tickets from a stream."""
    result: list[TicketDict] = []
    for ticket in tickets:
        if len(result) >= n:
            break
        result.append(ticket)
    return result




if __name__ == "__main__":
    stream = stream_tickets() # <--- this is our generator (stream)

    high_billing = where(
        stream, lambda ticket: ticket["priority"] == "high" and ticket["category"] == "billing"
    )
    flagged = tag(
        high_billing,
        "needs_review",
        lambda ticket: ticket["status"] in {"open", "in_progress"} # value
    )

    five_most_recent = take(flagged, 5)

    for ticket in five_most_recent:
        print(f"{ticket["id"]}  [{ticket["status"]:<20}]    "
              f"review={ticket["needs_review"]} {ticket["title"][:60]}")

    # print(type(stream))
    # first = next(stream)
    # print(f"First ticket: {first["id"]}")
    # second = next(stream)
    # print(f"Second ticket: {second["id"]}")
    # remaining = sum(1 for _ in stream) # add up all the tickets that are left 48
    # print(f"Remaining: {remaining}")
    # print(f"Generator exhausted, trying to pull anyway: {next(stream)}")