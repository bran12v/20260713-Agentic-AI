"""These the query transforms -> what reaches the gate instead of the question."""

import os
import time

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

_cred = DefaultAzureCredential()
aoai = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_RESOURCE_URL"],
    azure_ad_token_provider=get_bearer_token_provider(
        _cred, "https://cognitiveservices.azure.com/.default"
    ),
    api_version="2024-10-21"
)

# HyDE promt
HYDE_PROMPT = (
    "Write a short passage from an interal IT/delivery policy document that would " \
    "answer the question below. Write it as policy prose - clauses, conditions, " \
    "obligations. Do not hedge, do not say you are unsure, do not mention you are " \
    "generating an example.\n\n"
)

# Decomposition prompt
DECOMP_PROMPT = (
    "Split this question into 1-3 standalone search queries that together cover it. " \
    "One per line, no numbering, no commentary.\n\n"
)

def _ask(prompt: str) -> str:
    """A helper function to prompt a model with a retry element."""
    for a in range(4):
        try: 
            result = aoai.chat.completions.create(
                model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
                messages=[{"role": "user", "content": prompt}]
            )
            return result.choices[0].message.content or ""
        except Exception:
            if a == 3:
                raise
            time.sleep(3)

def hyde_draft(question: str) -> str:
    """Generate a hypothetical ANSWER. This is what gets embedded, not question."""
    return _ask(HYDE_PROMPT + f"Question: {question}")

def subqueries(question: str) -> list[str]:
    raw = _ask(DECOMP_PROMPT + f"Question: {question}")
    return [line.strip() for line in raw.splitlines() if line.strip()][:3]