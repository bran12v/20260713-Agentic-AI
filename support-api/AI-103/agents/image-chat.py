"""A Azure vision enabled chat bot."""

import os
import base64
from pathlib import Path

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
model_deployment = os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"]

REMOTE_IMAGE_URL = (
    "https://microsoftlearning.github.io/mslearn-ai-vision/Labfiles/gen-ai-vision/orange.jpeg"
)

SYSTEM_PROMPT = (
    "You are an AI assistant that helps people with questions about the images " \
    "they show you. Answer only rom what is visible in the image."
)

image_path = Path("mango.jpeg")
image_file_type = "jpeg"

# multi-modal chat message
def ask(client: OpenAI, prompt: str, image_url: str) -> str:
    """One Response API call, one MULTI-PART user message: text + image"""
    response = client.responses.create(
        model=model_deployment,
        input=[
            {"role": "developer", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": prompt },
                    { "type": "input_image", "image_url": image_url }
                ]
            }
        ]
    )
    return response.output_text

def build_data_url(path: Path, image_format: str) -> str:
    """LOAD -> encode -> CREATE URL. Three steps that a public url skips."""
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")
        return f"data:image/{image_file_type};base64,{image_data}"

def main() -> None:
    credential = DefaultAzureCredential()
    token_provider = get_bearer_token_provider(credential, "https://ai.azure.com/.default") # this getting an API token
    client = OpenAI(
        base_url=openai_endpoint,
        api_key=token_provider()
    )

    image_url = REMOTE_IMAGE_URL

    source = input("choose 1 or 2 (remote or local): ").strip()

    if source == "2":
        if not image_path.exists():
            raise SystemExit(f"{image_path} does not exist")
        image_url = build_data_url(image_path, image_file_type)
        print(f"Using local file {image_path} as the data url")
    else:
        print(f"using {REMOTE_IMAGE_URL} as URL")

    while True:
        prompt = input("\nEnter a prompt (or 'quit' to exit): ").strip()
        if prompt == "quit":
            break
        if not prompt:
            continue
        print()
        print(ask(client, prompt, image_url))

if __name__ == "__main__":
    main()