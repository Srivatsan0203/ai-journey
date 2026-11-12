"""Day 7: enforce LLM output shape with a Pydantic schema (a data contract)."""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, ValidationError


# The CONTRACT: the exact shape + types we require from the model.
class RaceSummary(BaseModel):
    winner: str
    winning_team: str
    lead_changes: int        # must be a real integer, not "three"
    summary: str


RACE_DATA = {
    "race": "2023 Bahrain Grand Prix",
    "podium": [
        {"position": 1, "driver": "Max Verstappen", "team": "Red Bull"},
        {"position": 2, "driver": "Sergio Perez", "team": "Red Bull"},
        {"position": 3, "driver": "Fernando Alonso", "team": "Aston Martin"},
    ],
    "lead_changes": 2,
}


def build_client() -> OpenAI:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "gsk_replace_me_with_your_real_key":
        raise SystemExit("GROQ_API_KEY is missing. Add your real key to the .env file.")
    return OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")


def summarize_validated(client: OpenAI, race: dict) -> RaceSummary:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an F1 analyst. Return ONLY a JSON object with keys: "
                    "winner (string), winning_team (string), lead_changes (integer), "
                    "summary (string, one sentence). Use only facts in the data."
                ),
            },
            {"role": "user", "content": json.dumps(race)},
        ],
    )
    raw = response.choices[0].message.content

    # The boundary check: validate the model's JSON against our contract.
    # Raises ValidationError if a field is missing or the wrong type.
    return RaceSummary.model_validate_json(raw)


def main() -> None:
    client = build_client()
    result = summarize_validated(client, RACE_DATA)

    # result is now a TYPED object, not a loose dict.
    print("Validated OK!")
    print("Winner:", result.winner)
    print("Team:", result.winning_team)
    print("Lead changes:", result.lead_changes, "(type:", type(result.lead_changes).__name__, ")")
    print("Summary:", result.summary)


if __name__ == "__main__":
    main()
