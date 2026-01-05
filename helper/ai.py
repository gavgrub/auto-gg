import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.groq.com/openai/v1/chat/completions"

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in .env")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def wordsToTokens(words: int) -> int:
    return int(words / 0.75) + 5

def generateText(prompt, maxWords=100) -> str:
    maxTokens = wordsToTokens(maxWords)

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8,
        "max_tokens": maxTokens
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)

    if response.status_code != 200:
        raise RuntimeError(
            f"HTTP {response.status_code}:\n{response.text}"
        )

    data = response.json()
    return data["choices"][0]["message"]["content"]

# Test Message
if __name__ == "__main__":
    print(generateText("how are you"))