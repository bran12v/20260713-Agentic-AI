"""The KB tool that keeps the score for the citations.

The previous agent demo uses the MCPStreamableHTTPTool accessing the KB over the MCP URL endpoint which 
gives the agent access to the prebuilt retrieval function which doesn't the hybrid/reranker scores.
"""

import json
import os
from typing import Annotated

from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizableTextQuery
from dotenv import load_dotenv
from pydantic import Field

from agent_framework import tool

load_dotenv()

from kb_lib import INDEX_NAME, SEMANTIC_CONFIG

FIELDS = ["chunk_id", "doc_id", "section_path", "content"]

search = SearchClient(os.environ["SEARCH_ENDPOINT"], INDEX_NAME, DefaultAzureCredential())

def retrieve(question: str, k: int = 5) -> list[dict]:
    """Hybrid + cross-encoder. Returns rows carrying the reranker score."""
    results = search.search(
        search_text=question, # BM25 Keyword
        vector_queries=[VectorizableTextQuery(
            text=question, k_nearest_neighbors=k*2, fields="embedding"
        )], # HNSW Vector Search
        select=FIELDS,
        query_type="semantic", # semantic ranker / cross-encoder
        semantic_configuration_name=SEMANTIC_CONFIG,
        top=k
    )
    rows = []
    for result in results:
        rows.append({
            "chunk_id": result["chunk_id"],
            "doc_id": result["doc_id"],
            "section_path": result["section_path"],
            "content": result["content"],
            # 0-4, bounded, comparable. THIS is the number our Gate will need to apply a threshold.
            "reranker": result.get("@search.reranker_score") # None
        })
        if len(rows) >= k:
            break
    return rows

@tool(approval_mode="never_require")
def search_standards(
    question: Annotated[str, Field(description="The user's question, verbatim.")]
) -> str:
    """Search the delivery-standards corpus. Return chunks with their scores."""
    return json.dumps({"chunks": retrieve(question, k=5)})

if __name__ == "__main__":
    for q in (
        "Within how long must an emergency change be retrospectively reviewed?",
        "What is our parental leave entitlement?"
    ):
        print(f"\nQ: {q}")
        for result in retrieve(q, k=5):
            print(f"    {result["reranker"]:.2f}    {result["doc_id"]:9} {result["section_path"][:44]}")