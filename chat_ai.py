import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import ChatCompletionsClient

# === Load environment variables ===
load_dotenv()

# === Azure OpenAI GitHub Model Setup ===
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
token = os.getenv("GITHUB_TOKEN_BACKUP")

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# Store chat history
chat_history = []

def ask_ai(prompt):
    global chat_history

    # Add user input
    chat_history.append({"role": "user", "content": prompt})

    # Send request to Azure OpenAI
    response = client.complete(
        model=model,
        messages=chat_history
    )

    # Extract reply
    reply = response.choices[0].message.content

    # Add assistant's reply to history
    chat_history.append({"role": "assistant", "content": reply})

    return reply
