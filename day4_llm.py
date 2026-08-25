"""Day 4: my first real LLM API call (via Groq's OpenAI-compatible endpoint)."""

import os                       # to read environment variables
from dotenv import load_dotenv  # loads key/values from the .env file
from openai import OpenAI       # the SDK; works with any OpenAI-compatible API


def main() -> None:
    # 1. Load the .env file into environment variables.
    load_dotenv()

    # 2. Read the secret by NAME (never hardcode the value).
    api_key = os.getenv("GROQ_API_KEY")

    # 3. Fail fast with a clear message if the key is missing/placeholder.
    #    (QA habit: validate inputs at the boundary before doing work.)
    if not api_key or api_key == "gsk_replace_me_with_your_real_key":
        raise SystemExit("GROQ_API_KEY is missing. Add your real key to the .env file.")

    # 4. Create the client, pointing the OpenAI SDK at Groq's endpoint.
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )

    # 5. Send the chat completion request.
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a pirate. Answer in pirate speak."},
            {"role": "user", "content": "Explain what an API is in one sentence."},
        ],
        temperature=0,
        max_tokens=200,
    )

    # 6. Parse the reply using the SAME drill-down path you learned on Day 3.
    #    (SDK objects use dot-access, e.g. .choices[0].message.content)
    reply = response.choices[0].message.content
    print("Model reply:\n", reply)

    # 7. Token usage — matters for cost/latency tracking later.
    usage = response.usage
    print(
        f"\nTokens -> prompt: {usage.prompt_tokens}, "
        f"completion: {usage.completion_tokens}, "
        f"total: {usage.total_tokens}  (you are billed on total)"
    )


if __name__ == "__main__":
    main()
