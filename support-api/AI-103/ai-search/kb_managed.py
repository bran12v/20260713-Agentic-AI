"""The platform that owns the Index.

Create the knowledgebase upload the 10 md files to a knowledge source 
wrap it into the KB and then ask it a question. Chunking, embedding, indexing are 
the platform's problem not ours."""

from pathlib import Path
import time

from azure.core.exceptions import ResourceNotFoundError
from azure.search.documents.indexes.models import (
    AzureOpenAIVectorizerParameters,
    FileKnowledgeSource,
    FileKnowledgeSourceParameters,
    KnowledgeBase,
    KnowledgeBaseAzureOpenAIModel,
    KnowledgeSourceReference,
)
from azure.search.documents.knowledgebases.models import (
    KnowledgeSourceAzureOpenAIVectorizer,
    KnowledgeSourceIngestionParameters,
    KnowledgeRetrievalLowReasoningEffort
)

from kb_lib import (
    AOAI_RESOURCE_URL,
    CHAT_DEPLOYMENT,
    CHAT_MODEL,
    EMBEDDING_DEPLOYMENT,
    EMBEDDING_MODEL,
    KS_FILES,
    KB_NAME,
    index_client,
    query,
    show,
)

CORPUS = Path("corpus")

embedding = KnowledgeSourceAzureOpenAIVectorizer(
    azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
        resource_url=AOAI_RESOURCE_URL,
        deployment_name=EMBEDDING_DEPLOYMENT,
        model_name=EMBEDDING_MODEL
    )
)

# The embedding config on a file knowledge source is immutable once set, so a
# create_or_update that changes it is rejected. Drop the old one first to keep
# this script re-runnable. Any knowledge base referencing it must go first.
# try:
#     index_client.delete_knowledge_source(KS_FILES)
#     print(f"Deleted existing knowledge source: {KS_FILES}")
# except ResourceNotFoundError:
#     pass

# Knowledge source
index_client.create_or_update_knowledge_source(
    FileKnowledgeSource(
        name=KS_FILES,
        description="Internal delivery standards, change management and operations.",
        file_parameters=FileKnowledgeSourceParameters(
            ingestion_parameters=KnowledgeSourceIngestionParameters(
                embedding_model=embedding
            )
        )
    )
)
print(f"Knowledge source: {KS_FILES}")

# upload all the file documents to the knowledge source.
for path in sorted(CORPUS.glob("*.md")):
    index_client.upload_knowledge_source_file( # upload each file to the knowledge source
        KS_FILES, path.read_bytes(), filename=path.name
    )
    print(f"    uploaded {path.name}")

# Knowledge Base
index_client.create_or_update_knowledge_base(
    KnowledgeBase(
        name=KB_NAME,
        description="Delivery engineering standards.",
        knowledge_sources=[KnowledgeSourceReference(name=KS_FILES)],
        models=[
            KnowledgeBaseAzureOpenAIModel(
                azure_open_ai_parameters=AzureOpenAIVectorizerParameters(
                    # Bare resource URL, same rule as the embedding vectorizer:
                    # Search appends /openai/deployments/{deployment}/chat/completions.
                    resource_url=AOAI_RESOURCE_URL,
                    deployment_name=CHAT_DEPLOYMENT,
                    model_name=CHAT_MODEL
                )
            )
        ],
        answer_instructions=( # system prompt for the query and answer synthesizer 
            "Answer only from retrieved content. Cite the document each claim comes from." \
            "If the content does not answer the question, say so."
        ),
        output_mode="answerSynthesis",
        retrieval_reasoning_effort=KnowledgeRetrievalLowReasoningEffort() # rag returns fast and doesn't think extensively on the retrieval.
    )
)
print(f"Knowledge Base: {KB_NAME}")

"""
ingestion is asynchronous, we are going to have to poll for the result.
"""

question = "Within how long must an emergency change be retrospectively reviewed?"

# print("waiting for ingestion", end="", flush=True)
# for _ in range(60):

#     try:
#         if query(question).references:
#             break
#     except Exception:
#         pass # might take a sec to be able to access the KB
#     print(".", end="", flush=True)
#     time.sleep(5)
# print(" done.")

show(question, query(question, activity=True))