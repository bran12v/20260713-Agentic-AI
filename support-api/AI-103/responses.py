import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv(Path.cwd().parent / ".env")

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_KEY"],
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"]
)

deployment = os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"]

INSTRUCTIONS = (
    "You are an internal delivery-support assistant for a software "
    "consulting firm. Answer questions about cloud architecture, CI/CD, "
    "and AI engagement delivery. Be concise and name the specific "
    "Azure service or pattern. If a question is out of scope, say so."
)

def main() -> None:
    last_response_id = None
    print("Assistant: Ask a delivery question (or type 'quit' to exit).")
    while True:
        user_text = input("\nYou: ")
        if user_text == 'quit':
            print("\nAssistant: Goodbye.")
            break

        response = client.responses.create(
            model=deployment,
            instructions=INSTRUCTIONS,
            input=user_text,
            previous_response_id=last_response_id
        )
        print(f"\nAssistant: {response.output_text}")
        last_response_id = response.id

if __name__ == "__main__":
    main()