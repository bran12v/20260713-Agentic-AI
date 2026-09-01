import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv(Path.cwd().parent / ".env")

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_KEY"]
)
deployment = os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"]

conversation_messages = [
    {
        "role": "system", # system prompt
        "content": (
            "You are an internal delivery-support assistant for a software "
            "consulting firm. Answer questions about cloud architecture, CI/CD, "
            "and AI engagement delivery. Be concise and name the specific "
            "Azure service or pattern. If a question is out of scope, say so."
        )
    }
]

def main() -> None:
    print("Assistant: Ask a delivery question (or type 'quit' to exit).")
    while True:
        user_text = input("\nYou: ")
        if user_text == 'quit':
            print("\nAssistant: Goodbye.")
            break

        conversation_messages.append(
            {
                "role": "user",
                "content": user_text
            }
        )
        completion = client.chat.completions.create( # this is the actual LLM call using the chat completions API
            model=deployment,
            messages=conversation_messages # resend the ENTIRE message history with every call
        )
        reply = completion.choices[0].message.content
        print(f"\nAssistant: {reply}")
        conversation_messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )


if __name__ == "__main__":
    main()