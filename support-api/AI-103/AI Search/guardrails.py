"""The gate the search demo didn't have."""

import asyncio
import json
from collections.abc import Awaitable, Callable
import os
import re
from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import AzureCliCredential
from kb_tool import search_standards

from agent_framework import (
    Content,
    FunctionInvocationContext,
    MiddlewareTermination,
    function_middleware
)
from dotenv import load_dotenv
load_dotenv()

# Calibrated threshold value based on evaluations of a golden set against agent retrieval.
TAU = 2.47

GATE_MARKER = "GATE_REFUSED:"

REFUSAL = (
    "That isn't covered in our current standards library - "
    "please raise it with the delivery lead."
)

def _payload(result) -> dict:
    """context.result is normally a list[Content]. Never assume; don't index blindly."""
    if isinstance(result, list):
        text = "".join(getattr(c, "text", "") or "" for c in result) # generator function that will create a dict of chunks
    else:
        text = getattr(result, "text", None) or str(result or "")
    try:
        return json.loads(text)
    except(json.JSONDecodeError, TypeError):
        return {}

def verify(answer: str, retrieved: set[str]) -> tuple[list[dict], list[str]]:
    """
    All cited documents that were retrieved this agent turn. Getting info on anything that exists in the corpus.
    A citation to a real document but the agent never uses it is still a fabrication.
    """
    cited = set(re.findall(r"\[doc_id:\s*([A-Z]{3}-[A-Z]{3})\]", answer))
    sources = [{"doc_id": d} for d in sorted(cited & retrieved)]
    unsupported = sorted(cited - retrieved)
    return sources, unsupported


@function_middleware
async def gate_on_reranker(
    context: FunctionInvocationContext,
    call_next: Callable[[], Awaitable[None]]
) -> None:
    """Refuse below TAU, and drop the chunks that did not clear the threshold."""
    await call_next()
    if context.function.name != "search_standards":
        return

    chunks = _payload(context.result).get("chunks", [])
    top = max((c.get("reranker") or 0.0 for c in chunks), default=0.0)

    # JOB 1 - the Gate.
    # the best result does not clear the threshold, we need to return a error dict without synthesizing
    if top < TAU:
        print(f"    [gate] top {top:.2f} < {TAU} -> REFUSE (no synthesis call)")
        # set the context to have a appropriate error to indicate to the agent what happened.
        context.result = [Content.from_text(GATE_MARKER + json.dumps(
            {"reason": "below_retrieval_threshold", "top": round(top, 2), "tau": TAU}
        ))]
        raise MiddlewareTermination(f"below tau: {top:.2f}") # FAILURE
    else:
        # JOB 2 - the filter.
        # The Gate passed, but there may be individual chunks below the threshold that will be distractors.
        kept = [c for c in chunks if (c.get("reranker") or 0.0) >= TAU]
        dropped = len(chunks) - len(kept)
        print(f"    [gate] top {top:.2f} >= TAU -> PASS, kept {len(kept)} chunks, dropped {dropped} chunks")
        context.result = [Content.from_text(json.dumps({"chunks": kept}))]



async def main() -> None:
    instruction = (
        "You are an internal delivery-standards assistant. ALWAYS search the "
        "corpus before answering. Cite the doc_id and section of every claim."
    )
    async with AzureCliCredential() as credential:
        client = FoundryChatClient(
            project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
            model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
            credential=credential
        )
        async with Agent(
            client,
            instructions=instruction, 
            name="gated",
            tools=[search_standards],
            middleware=[gate_on_reranker]
        ) as agent:
            for q in (
                "Within how long must an emergency change be retrospectively reviewed?",
                "What is our parental leave entitlement?"
            ):
                print(f"\nQ: {q}")
                result = await agent.run(q)
                print(f"A: {result.text[:300]}")
                print(f"    [is verbatim REFUSAL: {result.text.strip() == REFUSAL}]")

if __name__ == "__main__":
    asyncio.run(main())