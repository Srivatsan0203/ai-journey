"""Day 7: prove the RaceSummary contract rejects bad data (fixture-based tests, no API)."""

from pydantic import ValidationError

from day7_schema import RaceSummary


# Each case is (label, bad JSON string that should FAIL validation).
BAD_CASES = [
    ("missing field (no summary)",
     '{"winner": "Max", "winning_team": "Red Bull", "lead_changes": 2}'),
    ("wrong type (lead_changes is text)",
     '{"winner": "Max", "winning_team": "Red Bull", "lead_changes": "lots", "summary": "ok"}'),
]

# A valid case that should PASS.
GOOD_CASE = '{"winner": "Max", "winning_team": "Red Bull", "lead_changes": 2, "summary": "A clean win."}'


def main() -> None:
    print("--- Bad cases (should all be caught) ---")
    for label, bad_json in BAD_CASES:
        try:
            RaceSummary.model_validate_json(bad_json)
            print(f"[FAIL] {label}: UNEXPECTEDLY PASSED")
        except ValidationError as e:
            first = e.errors()[0]
            print(f"[OK]   {label}: caught '{first['type']}' on field {first['loc']}")

    print("\n--- Good case (should pass) ---")
    ok = RaceSummary.model_validate_json(GOOD_CASE)
    print(f"[OK]   valid data accepted -> winner={ok.winner}, lead_changes={ok.lead_changes}")


if __name__ == "__main__":
    main()
