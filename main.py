import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("API Key not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def main():
    response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ],
)
    if not response.usage:
        raise RuntimeError("Usage data not found in response")
    X = response.usage.prompt_tokens
    Y = response.usage.completion_tokens

    print(f"Prompt tokens: {X}")
    print(f"Response tokens: {Y}")
    print("Ressponse:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
