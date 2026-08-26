"""Day 5: turn structured F1 race data into an AI-generated summary (JSON output)."""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI


# Real result: 2023 Bahrain Grand Prix, top 3 finishers.
RACE_DATA = {
    "race": "2023 Bahrain Grand Prix",
    "circuit": "Bahrain International Circuit",
    "laps": 57,
    "podium": [
        {"position": 1, "driver": "Max Verstappen", "team": "Red Bull", "time": "1:33:56.736"},
        {"position": 2, "driver": "Sergio Perez", "team": "Red Bull", "time": "+11.987s"},
        {"position": 3, "driver": "Fernando Alonso", "team": "Aston Martin", "time": "+38.637s"},
    ],
}


def build_client() -> OpenAI:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "gsk_replace_me_with_your_real_key":
        raise SystemExit("GROQ_API_KEY is missing. Add your real key to the .env file.")
    return OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")


def summarize_race(client: OpenAI, race_data: dict) -> dict:
    # We pass the race data to the model as a JSON string inside the prompt.
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        temperature=0,  # deterministic -> testable
        response_format={"type": "json_object"},  # API guarantees valid JSON
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an F1 analyst. Given race data as JSON, return a JSON object "
                    "with keys: 'winner' (string), 'winning_team' (string), and "
                    "'summary' (a 2-sentence, factually accurate race summary). "
                    "Only use facts present in the data."
                ),
            },
            {"role": "user", "content": json.dumps(race_data)},
        ],
    )
    raw = response.choices[0].message.content
    # The API guarantees valid JSON text; json.loads turns that text into a Python dict.
    return json.loads(raw)


def check_winner(result: dict, race_data: dict) -> bool:
    # The AI's claimed winner should match the ACTUAL winner in the source data
    # (the driver at podium position 1).
    return result["winner"].strip().lower() == race_data["podium"][0]["driver"].strip().lower()


def main() -> None:
    client = build_client()
    result = summarize_race(client, RACE_DATA)

    print("Parsed result type:", type(result).__name__)
    print("Winner:", result["winner"])
    print("Team:  ", result["winning_team"])
    print("Summary:", result["summary"])
    print("Winner check passed: ", check_winner(result, RACE_DATA))

if __name__ == "__main__":
    main()
