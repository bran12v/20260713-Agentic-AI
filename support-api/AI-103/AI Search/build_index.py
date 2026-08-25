"""the index creation/definition file (P2 prep)

section-aware chunking, per-chunk metadata, filterable doc_types, section_paths
and semantic configuration. Every that Part 1 gave us for free we are going
to build natively.
"""
import os
import re
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    AzureOpenAIVectorizer,
    AzureOpenAIVectorizerParameters,
    HnswAlgorithmConfiguration,
    SearchableField,
    SearchField,
    SearchFieldDataType,
    SearchIndex,
    SemanticConfiguration,
    SemanticField,
    SemanticPrioritizedFields,
    SemanticSearch,
    SimpleField,
    VectorSearch,
    VectorSearchProfile,
)
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

SEARCH_ENDPOINT = os.environ["SEARCH_ENDPOINT"]
INDEX_NAME = "delivery-standards-idx"
SEMANTIC_CONFIG = "sem-config"
EMBED_DIM = 1536  # text-embedding-3-small

CORPUS = Path("corpus")
DOC_IDS = {
    "change-management-standard.md": ("CHG-STD", "standard"),
    "standard-change-catalog.md": ("CHG-CAT", "catalog"),
    "exception-request-procedure.md": ("EXC-PROC", "procedure"),
    "incident-severity-matrix.md": ("SEV-MTX", "matrix"),
    "production-access-policy.md": ("ACC-POL", "policy"),
    "records-retention-schedule.md": ("RET-SCH", "schedule"),
    "rollback-and-backout-standard.md": ("RBK-STD", "standard"),
    "release-freeze-calendar.md": ("FRZ-CAL", "calendar"),
    "on-call-escalation-runbook.md": ("ONC-RUN", "runbook"),
    "vendor-security-review-sop.md": ("VND-SOP", "sop"),
}

credential = DefaultAzureCredential()
index_client = SearchIndexClient(endpoint=SEARCH_ENDPOINT, credential=credential)

index = SearchIndex(
    name=INDEX_NAME,
    fields=[
        SimpleField(name="chunk_id", type=SearchFieldDataType.String, key=True),
        # filterable=True is set at index-creation time and cannot be added later
        # without a rebuild. Project 2 names these two fields specifically.
        SimpleField(name="doc_id", type=SearchFieldDataType.String, filterable=True, facetable=True),
        SimpleField(name="doc_type", type=SearchFieldDataType.String, filterable=True, facetable=True),
        SearchableField(name="section_path", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="title", type=SearchFieldDataType.String),
        SearchableField(name="content", type=SearchFieldDataType.String),
        SearchField(
            name="embedding",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=EMBED_DIM,
            vector_search_profile_name="hnsw-profile",
        ),
    ],
    vector_search=VectorSearch(
        algorithms=[HnswAlgorithmConfiguration(name="hnsw")],
        profiles=[VectorSearchProfile(name="hnsw-profile", algorithm_configuration_name="hnsw", vectorizer_name="aoai")],
        vectorizers=[
            AzureOpenAIVectorizer(
                vectorizer_name="aoai",
                parameters=AzureOpenAIVectorizerParameters(
                    resource_url=os.environ["AZURE_OPENAI_RESOURCE_URL"],
                    deployment_name=os.environ["EMBEDDING_DEPLOYMENT"],
                    model_name=os.environ["EMBEDDING_DEPLOYMENT"],
                ),
            )
        ],
    ),
    # Names the fields the ranker weights, and makes the index usable by the
    # classic single-query pipeline too. Agentic retrieval reranks either way.
    semantic_search=SemanticSearch(
        configurations=[
            SemanticConfiguration(
                name=SEMANTIC_CONFIG,
                prioritized_fields=SemanticPrioritizedFields(
                    title_field=SemanticField(field_name="title"),
                    content_fields=[SemanticField(field_name="content")],
                    keywords_fields=[SemanticField(field_name="section_path")],
                ),
            )
        ]
    ),
)
index_client.create_or_update_index(index)
print(f"index: {INDEX_NAME}")

# LLM
aoai = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_RESOURCE_URL"],
    azure_ad_token_provider=lambda: credential.get_token(
        "https://cognitiveservices.azure.com/.default"
    ).token,
    api_version="2024-10-21"
)

# returns each chunk as a tuple of body and heading.
def chunk(text: str) -> list[tuple[str, str]]:
    """
    Split on ## headings. Returns (section_path, body) pairs.

    ex: structure-aware chunking, not fixed size.
    """
    parts = re.split(r"\n(?=## )", text)
    chunks = []
    for part in parts:
        heading = part.splitlines()[0].lstrip("# ").strip() # the heading with no section header ##
        body = part.strip()
        if len(body) > 40: # Dropping any heading without a proper body underneath
            chunks.append((heading, body))
    return chunks

documents = [] # all of the .md files info and the schema metadata 

for path in sorted(CORPUS.glob("*.md")):
    if path.name not in DOC_IDS:
        continue
    doc_id, doc_type = DOC_IDS[path.name]
    text = path.read_text(encoding="utf-8") # a text string of the document
    title = text.splitlines()[0].lstrip("# ").strip()

    for i, (section_path, body) in enumerate(chunk(text)):
        documents.append({
            # schema fields
            "chunk_id": f"{doc_id}-{i:03d}",
            "doc_id": doc_id,
            "doc_type": doc_type,
            "section_path": section_path,
            "title": title,
            "content": body,
        })

vectors = aoai.embeddings.create(
    model=os.environ["EMBEDDING_DEPLOYMENT"],
    input=[doc["content"] for doc in documents]
)

for document, item in zip(documents, vectors.data):
    document["embedding"] = item.embedding

search_client = SearchClient(SEARCH_ENDPOINT, INDEX_NAME, credential)
search_client.upload_documents(documents)
print(f"uploaded {len(documents)} chunks from {len(DOC_IDS)} documents")