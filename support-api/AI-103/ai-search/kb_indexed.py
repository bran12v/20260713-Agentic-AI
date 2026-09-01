"""
Part 2 - attach the search index that we built as a knowledge source and connect to our knowledge base.

Two sources in the KB, and the retrieval instructions will decide which one answers. Also,
This is the first time that we can filter, because we control the index (the fields).
"""

import os
import time

from azure.search.documents.indexes.models import (
    AzureOpenAIVectorizerParameters,
    KnowledgeBase,
    KnowledgeBaseAzureOpenAIModel,
    KnowledgeSourceReference,
    SearchIndexFieldReference,
    SearchIndexKnowledgeSource, 
    SearchIndexKnowledgeSourceParameters
)

from azure.search.documents.knowledgebases.models import( 
    KnowledgeRetrievalLowReasoningEffort
)

from kb_lib import (
    INDEX_NAME, KB_NAME, KS_FILES, KS_INDEX, 
    SEMANTIC_CONFIG, index_client, query, show
)

"""A search index knowledge source is a knowledge source that will wrap the existing 
search index that already exists."""
index_client.create_or_update_knowledge_source(
    SearchIndexKnowledgeSource(
        name=KS_INDEX,
        description=(
            "Delivery standards chunked by section, with doc_id, doc_type and section_path." \
            "Use when the question needs a clause or filter."
        ),
        search_index_parameters=SearchIndexKnowledgeSourceParameters(
            search_index_name=INDEX_NAME,
            semantic_configuration_name=SEMANTIC_CONFIG,
            source_data_fields=[
                SearchIndexFieldReference(name="doc_id"),
                SearchIndexFieldReference(name="title"),
                SearchIndexFieldReference(name="section_path"),
                SearchIndexFieldReference(name="content"),
            ]
        )
    )
)
print(f"Knowledge source: {KS_INDEX}")

# Same Knowledge Base, now with sources. Update the retrieval instructions to allow for/make useful
# having a second Knowledge Source.
index_client.create_or_update_knowledge_base(
    KnowledgeBase(
        name=KB_NAME,
        knowledge_sources=[
            KnowledgeSourceReference(name=KS_FILES),
            KnowledgeSourceReference(name=KS_INDEX),
        ],
        models=[
            KnowledgeBaseAzureOpenAIModel(
                azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
                    # Bare resource URL, same rule as the embedding vectorizer:
                    # Search appends /openai/deployments/{deployment}/chat/completions.
                    resource_url=os.environ["AZURE_OPENAI_RESOURCE_URL"],
                    deployment_name=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
                    model_name=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"]
                )
            )
        ],
        retrieval_instructions=(
            f"Prefer '{KS_INDEX}' for questions needing a specific clause, a "
            f"section reference, or a filter on document type. Use "
            f"'{KS_FILES}' for broad questions spanning multiple documents."
        ),
        answer_instructions=(
            "Answer only from the retrieved content. Cite the doc_id and "
            "section_path of every claim. If the retrieved content does not "
            "answer the question, say so plainly and do not fill the gap."
        ),
        output_mode="answerSynthesis",
        retrieval_reasoning_effort=KnowledgeRetrievalLowReasoningEffort()
    )
)
print(f"Knowledge Base: {KB_NAME} (2 sources)")

q1 = "Does rotating a TLS certificate on a load balancer need CAB approval?"
show(q1, query(q1, source_data=True, activity=True))

q2 = "What review components does a Tier 2 vendor need?"
show(q2, query(q2, doc_type="sop"))