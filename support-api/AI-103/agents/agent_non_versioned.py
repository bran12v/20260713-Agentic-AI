import os

from dotenv import load_dotenv
from azure.identity import AzureCliCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import MessageRole
from pathlib import Path

load_dotenv(Path.cwd().parent / ".env")

# classic (legacy) v1
agent_client = AgentsClient(
    endpoint=os.environ["AZURE_FOUNDRY_PROJECT_ENDPOINT"],
    credential=AzureCliCredential(process_timeout=30) # gets your credentials (permissions) from 'az login'
)

INSTRUCTIONS = ( # system prompt
    "You are an internal delivery-support assistant for a software "
    "consulting firm. Answer questions about cloud architecture, CI/CD, "
    "and AI engagement delivery. Be concise and name the specific "
    "Azure service or pattern. If a question is out of scope, say so."
)

def main() -> None:
    agent = agent_client.create_agent(
        model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        name="delivery-support-agent-bvanek",
        instructions=INSTRUCTIONS
    )

    print("Created agent id: ", agent.id)

    thread = agent_client.threads.create() # this will open a new conversation
    agent_client.messages.create(
        thread_id=thread.id, # this is the static id of your conversation
        role="user",
        content="What handles traffic switch in a blue-green deployment on AKS?"
    )

    # create_and_process runs the agent and any tool calls, blocking until done.
    agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id) #submit button

    # read in the latest message from the agent
    reply = agent_client.messages.get_last_message_text_by_role(
        thread_id=thread.id,
        role=MessageRole.AGENT
    )

    print(reply.text.value)

    # ask a follow up question
    agent_client.messages.create(
        thread_id=thread.id, # this is the static id of your conversation
        role="user",
        content="Does that work with our existing Helm charts?"
    )
    agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id) #submit button
    followup = agent_client.messages.get_last_message_text_by_role(
        thread_id=thread.id,
        role=MessageRole.AGENT
    )
    print(followup.text.value)

    # agent_client.messages.create(
    #     thread_id=thread.id, # this is the static id of your conversation
    #     role="user",
    #     content="What is postgres?"
    # )
    # agent_client.messages.create(
    #     thread_id=thread.id, # this is the static id of your conversation
    #     role="user",
    #     content="What is AKS?"
    # )
    # agent_client.messages.create(
    #     thread_id=thread.id, # this is the static id of your conversation
    #     role="user",
    #     content="What are VNETs?"
    # )
    # agent_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id) #submit button
    # followup = agent_client.messages.get_last_message_text_by_role(
    #     thread_id=thread.id,
    #     role=MessageRole.AGENT
    # )
    # print(followup.text.value)



if __name__ == "__main__":
    main()