import asyncio
import json
import os

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import AzureCliCredential
from dotenv import load_dotenv

from kb_tool import retrieve, search_standards

load_dotenv()

Q = "What is our parental leave entitlement?"

def top(q: str) -> float:
    return max((r["reranker"] or 0 for r in retrieve(q, k=5)), default=0.0)

async def main() -> None:
    print(f"user question: {Q!r}")
    print(f"verbatim score: {top(Q):.2f}    (deterministic)\n")
    async with AzureCliCredential() as cred:
        client = FoundryChatClient(
            project_endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
            model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
            credential=cred
        )
        seen: dict[str, int] = {}
        for _ in range(6):
            async with Agent(
                client,
                instructions="Search the corpus first. Cite doc_id.", 
                name="placeholder",
                tools=[search_standards]
            ) as agent:
                r = await agent.run(Q)
                for c in (c for m in r.messages for c in m.contents
                          if getattr(c, "type", None) == "function_call"):
                    sent = json.loads(c.arguments).get("question", "")
                    seen[sent] = seen.get(sent, 0) + 1
        print(f"6 runs -> {len(seen)} distinct query strings sent to the tool:\n")

        for s, n in sorted(seen.items(), key=lambda kv: -kv[1]):
            tag = "VERBATIM " if s == Q else "REWRITTEN"
            print(f"  [{n}x] {tag} score={top(s):.2f}")
            print(f"        {s!r}")

if __name__ == "__main__":
    asyncio.run(main())