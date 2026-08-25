"""Shared library for the knowledge base creation scripts
The Foundry SDK to create and set the resources.
"""

import os
import sys

from azure.identity import DefaultAzureCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.knowledgebases import KnowledgeBaseRetrievalClient
from azure.search.documents.knowledgebases.models import (
    KnowledgeBaseMessage,
    KnowledgeBaseMessageTextContent,
    KnowledgeBaseRetrievalRequest,
    KnowledgeRetrievalLowReasoningEffort,
    SearchIndexKnowledgeSourceParams
)

from dotenv import load_dotenv

load_dotenv()

SEARCH_ENDPOINT = os.environ["SEARCH_ENDPOINT"]

# Bare Azure OpenAI resource URL. Search appends
# /openai/deployments/{deployment}/embeddings, so this must NOT carry the
# /openai/v1 suffix that AZURE_OPENAI_ENDPOINT uses for the OpenAI-compatible client.
AOAI_RESOURCE_URL = os.environ["AZURE_OPENAI_RESOURCE_URL"]

# Deployment name and model name are distinct; they just coincide here.
EMBEDDING_DEPLOYMENT = os.environ["EMBEDDING_DEPLOYMENT"]
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", EMBEDDING_DEPLOYMENT)

# Chat model used by the knowledge base for query planning and answer synthesis.
CHAT_DEPLOYMENT = os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"]
CHAT_MODEL = os.getenv("AZURE_OPENAI_CHAT_MODEL", CHAT_DEPLOYMENT)

KB_NAME = "delivery-standards"
KS_FILES = "delivery-standards-files"
KS_INDEX = "delivery-standards-index"
INDEX_NAME = "delivery-standards-idx"
SEMANTIC_CONFIG = "sem-config"

credential = DefaultAzureCredential()
index_client = SearchIndexClient(endpoint=SEARCH_ENDPOINT, credential=credential)
kb_client = KnowledgeBaseRetrievalClient(
    SEARCH_ENDPOINT, credential, knowledge_base_name=KB_NAME
)

# Query
def query(text: str, doc_type: str, activity: bool = False, source_data: bool = False):
    """Ask the knowledge base one question. Returns the raw retrieval result.
    
    source_data / doc_type which will target the index source rather than the integrated KB.
    """
    params = None
    if source_data or doc_type:
        params = [
            SearchIndexKnowledgeSourceParams(
                knowledge_source_name=KS_INDEX,
                include_references=True,
                include_reference_source_data=True,
                filter_add_on=f"doc_type eq '{doc_type}'" if doc_type else None,
                always_query_source=bool(doc_type)
            )
        ]
    return kb_client.retrieve(
        KnowledgeBaseRetrievalRequest(
            messages=[
                KnowledgeBaseMessage(
                    role="user",
                    content=[KnowledgeBaseMessageTextContent(text=text)]
                )
            ],
            knowledge_source_params=params, # makes it so we will hit our index if we query our specific params
            include_activity=activity,
            retrieval_reasoning_effort=KnowledgeRetrievalLowReasoningEffort(),
        )
    )

# Show
def show(question: str, result, *, limit: int = 5) -> None:
    """Print the answer, the top references and their reranker scores."""
    print(f"\nQ: {question}")
    for message in result.response or []:
        for block in message.content or []:
            print(f"A: {getattr(block, 'text', '')[:400]}")

    # Index references carry doc_id + section_path in source_data; file
    # references carry the uploaded filename on doc_name. Neither has both.
    for ref in (result.references or [])[:limit]:
        data = ref.source_data or {}
        label = data.get("doc_id") or getattr(ref, "doc_name", None) or "?"
        section = data.get("section_path", "")
        print(f"    [{ref.id}] {label} {section}  reranker={ref.reranker_score}")

    for act in result.activity or []:
        fields = " ".join(
            f"{f}={getattr(act, f)}"
            for f in ("model_name", "input_tokens", "output_tokens", "count")
            if getattr(act, f, None) is not None
        )
        print(f"    {act.type}  {fields}")