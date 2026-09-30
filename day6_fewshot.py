"""Day 6: few-shot prompting - steer F1 summaries by showing examples.

Compares ZERO-SHOT (rules only) vs FEW-SHOT (rules + examples) side by side.
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI


# A new race the model has NOT seen in our examples.
REAL_RACE = {
    "race": "2023 Las Vegas Grand Prix",
    "winner": "Max Verstappen",
    "team": "Red Bull",
    "notable": "overtook Leclerc late after a safety car restart",
}


def build_client() -> OpenAI:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "gsk_replace_me_with_your_real_key":
        raise SystemExit("GROQ_API_KEY is missing. Add your real key to the .env file.")
    return OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")


def summarize_zero_shot(client: OpenAI, race: dict) -> str:
    """Rules only - no examples. Style may drift."""
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        temperature=0,
        messages=[
            {"role": "system", "content": "You are an F1 analyst. Summarize the race."},
            {"role": "user", "content": json.dumps(race)},
        ],
    )
    return response.choices[0].message.content


def summarize_few_shot(client: OpenAI, race: dict) -> str:
    """Rules + examples. The model imitates the demonstrated style."""
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        temperature=0,
        messages=[
            {"role": "system", "content": "You are an F1 analyst. Summarize races in exactly ONE punchy sentence."},

            {"role": "user", "content": '{"race": "2021 British GP", "winner": "Hamilton", "notable": "controversial clash with Verstappen at Copse"}'},
            {"role": "assistant", "content": "Hamilton triumphed at Silverstone after a controversial opening-lap clash with Verstappen."},
            {"role": "user", "content": '{"race": "2022 Austrian GP", "winner": "Leclerc", "notable": "held off Verstappen despite a throttle issue"}'},
            {"role": "assistant", "content": "Leclerc battled a throttle problem to hold off Verstappen and win the Austrian Grand Prix."},
            {"role": "user", "content": json.dumps(race)},
        ],
    )
    return response.choices[0].message.content


def main() -> None:
    client = build_client()

    print("=== ZERO-SHOT (rules only) ===")
    print(summarize_zero_shot(client, REAL_RACE))

    print("\n=== FEW-SHOT (rules + examples) ===")
    print(summarize_few_shot(client, REAL_RACE))


if __name__ == "__main__":
    main()
