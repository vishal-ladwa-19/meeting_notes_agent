from openai import OpenAI
from config import OPENROUTER_API_KEY, OPENROUTER_MODEL, BASE_URL

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=BASE_URL,
)


def generate_response(system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        max_completion_tokens=1000,   # <-- IMPORTANT
    )

    return response.choices[0].message.content