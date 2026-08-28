"""Final artifact for our RAG lectures that puts all of our finds together
to create a robust RAG system that allows our agents to produce
accurate, cited, and safe results.
"""

import asyncio
import json
import os

from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import Annotated

from agent_framework import (
    Agent, Content, FunctionInvocationContext, MiddlewareTermination,
    function_middleware, tool,
)
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv
from pydantic import Field

from attacks import _ask
from guardrails import GATE_MARKER, TAU, verify
from kb_tool import retrieve

load_dotenv()

COMPRESS_PROMPT = (
    "Extract ONLY the sentences from the passage below that help answer the "
    "question. Copy them verbatim. If none of the passage is relevant, reply "
    "with exactly NONE.\n\n"
)
INSTRUCTIONS = (
    "You are an internal delivery-standards assistant. ALWAYS search before "
    "answering and NEVER answer from your own training data. Cite the doc_id "
    "of every claim in the form [doc_id: XXX-XXX]. If the passages do not "
    "contain the answer, say so plainly."
)

_TURN: dict[str, set[str]] = {"retrieved": set()}

REFUSAL = (
    "That isn't covered in our current standards library - "
    "please raise it with the delivery lead."
)

@dataclass
class Decision:
    """A refusal is first-class typed output with a reason code"""
    answered: bool
    text: str = ""
    reason: str | None = None
    top_score: float = 0.0
    sources: list[dict] = field(default_factory=list)
    uncited: list[str] = field(default_factory=list)

@tool(approval_mode="never_require")
def search_standards(
        question: Annotated[str, Field(description="The user's question, verbatim.")]
) -> str:
    """Search the delivery-standards corpus"""
    rows = retrieve(question, k=5)
    _TURN["retrieved"] = {r["doc_id"] for r in rows}
    return json.dumps({"chunks": rows})

@function_middleware
async def gate_and_compress(
    context: FunctionInvocationContext,
    call_next: Callable[[], Awaitable[None]]
) -> None:
    """Refuse below TAU, and compress the chunks if passed."""
    await call_next() # actual tool call
    if context.function.name != "search_standards":
        return
    
    text = "".join(getattr(c, "text", "") or "" for c in context.result) \
        if isinstance(context.result, list) else str(context.result or "")

    chunks = json.loads(text).get("chunks", [])
    top = max((c.get("reranker") or 0.0 for c in chunks), default=0.0)

    kept = []

    # JOB 1 - the Gate.
    # the best result does not clear the threshold, we need to return a error dict without synthesizing
    if top < TAU:
        print(f"    [gate] top {top:.2f} < {TAU} -> REFUSE (no synthesis call)")
        # set the context to have a appropriate error to indicate to the agent what happened.
        context.result = [Content.from_text(GATE_MARKER + json.dumps(
            {"reason": "below_retrieval_threshold", "top": round(top, 2), "tau": TAU}
        ))]
        raise MiddlewareTermination(f"below tau: {top:.2f}") # FAILURE
    
    # Compress, do not filter.
    kept = []
    for c in chunks:
        out = (_ask(COMPRESS_PROMPT + f"Question: {context.arguments['question']}\n\n"
                    f"Passage:\n{c['content']}") or "").strip()
        if out.upper().startswith("NONE") or not out:
            continue
        kept.append({**c, "content": out})
    before = sum(len(c["content"]) for c in chunks)
    after = sum(len(c["content"]) for c in kept)
    print(f"    [gate] top {top:.2f} >= {TAU} PASS | compressed {before}->{after} chars, "
          f"{len(chunks)}->{len(kept)} chunks, docs {sorted({c['doc_id'] for c in kept})}")
    context.result = [Content.from_text(json.dumps({"chunks": kept}))]


async def ask(agent, question: str) -> Decision:
    _TURN["retrieved"] = set()
    response = await agent.run(question)
    for msg in response.messages:
        for c in msg.contents:
            if getattr(c, "type", None) == "function_result":
                res = str(getattr(c, "result", "") or "")
                if res.startswith(GATE_MARKER):
                    d = json.loads(res[len(GATE_MARKER):])
                    return Decision(False, reason=d["reason"], top_score=d["top"])
    text = (response.text or "").strip()
    if not text:
        return Decision(False, reason="empty_response")
    sources, uncited = verify(text, _TURN["retrieved"])
    return Decision(True, text=text, sources=sources, uncited=uncited)



async def main() -> None:
    async with AzureCliCredential() as cred:
        client = FoundryChatClient(project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
                                   model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"], credential=cred)
        async with Agent(client, name="grounded", instructions=INSTRUCTIONS,
                         tools=[search_standards],
                         middleware=[gate_and_compress]) as agent:
            for q in ("Does rotating a TLS certificate on a load balancer need CAB approval?",
                      "What is our parental leave entitlement?"):
                print(f"\nQ: {q}")
                d = await ask(agent, q)
                if not d.answered:
                    print(f"   REFUSED  reason={d.reason}  top={d.top_score}")
                else:
                    print(f"   ANSWERED sources={[s['doc_id'] for s in d.sources]}"
                          f"  unsupported_citations={d.uncited}")
                    print(f"   {d.text[:300]}")


if __name__ == "__main__":
    asyncio.run(main())