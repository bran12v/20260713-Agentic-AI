import os

from dotenv import load_dotenv
from azure.identity import AzureCliCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from pathlib import Path

load_dotenv(Path.cwd().parent / ".env")

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
    credential=AzureCliCredential(process_timeout=30)
)

AGENT_NAME = "delivery-support-agent"

V1_INSTRUCTIONS = (
    "You are an internal delivery-support agent for a software consulting "
    "firm. Answer questions about cloud architecture, CI/CD, and AI "
    "engagement delivery. Be concise and name the specific Azure service."
)

# The only change in v2: it must cite a Well-Architected pillar.
V2_INSTRUCTIONS = (
    "You are an internal delivery-support agent for a software consulting "
    "firm. Answer questions about cloud architecture, CI/CD, and AI "
    "engagement delivery. Be concise, name the specific Azure service, and "
    "cite the relevant Well-Architected pillar."
)


def main() -> None:
    # Idempotent
    version = project_client.agents.create_version(
        agent_name=AGENT_NAME,
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
            instructions=V1_INSTRUCTIONS
        )
    )

    print(f"Created new agent: {version.name}, version: {version.version}")

    openai_client = project_client.get_openai_client()
    response = openai_client.responses.create(
        input="What handles traffic switch in a blue-green deployment on AKS?",
        extra_body={"agent_reference": {
            "name": version.name,
            "type": "agent_reference"
        }} # use version 3 not 2 or 1
    )

    print(response.output_text)

    version2 = project_client.agents.create_version(
        agent_name=AGENT_NAME,
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
            instructions=V2_INSTRUCTIONS
        )
    )
    print(f"Created new agent version: {version2.name}, version: {version2.version}")

    versioned_response = openai_client.responses.create(
        input="Name one reliability practice for AKS in six words.",
        extra_body={"agent_reference": {
            "name": AGENT_NAME,
            "version": version2.version,
            "type": "agent_reference"
        }} # use version 3 not 2 or 1
    )
    print(versioned_response.output_text)
    

if __name__ == "__main__":
    main()