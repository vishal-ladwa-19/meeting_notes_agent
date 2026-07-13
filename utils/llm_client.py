from openai import OpenAI
from config import OPENROUTER_API_KEY, OPENROUTER_MODEL, BASE_URL


def generate_response(system_prompt: str, user_prompt: str) -> str:
    if not OPENROUTER_API_KEY:
        return "Error: OPENROUTER_API_KEY is missing. Add it in Streamlit Community Cloud Secrets."

    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=BASE_URL,
    )

    response = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        max_tokens=1200,
    )

    return response.choices[0].message.content