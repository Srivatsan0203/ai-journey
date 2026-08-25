"""Day 3: navigating nested data (dicts, lists) like an API response."""

# A simplified mock of what an LLM API returns.
response = {
    "id": "chatcmpl-123",
    "model": "llama-3.1",
    "choices": [
        {"index": 0, "message": {"role": "assistant", "content": "Hello, Vatsan!"}},
        {"index": 1, "message": {"role": "assistant", "content": "Hi again, Vatsan!"}}
    ],
    "usage": {"prompt_tokens": 12, "completion_tokens": 5},
}


def get_reply(response: dict) -> str:
    return response["choices"][0]["message"]["content"]


def get_total_tokens(response: dict) -> int:
    return response["usage"]["prompt_tokens"] + response["usage"]["completion_tokens"]


def list_model_and_reply(response: dict) -> str:
    return f"Model {response['model']} said: {get_reply(response)}"


def count_choices(response: dict) -> int:
    return len(response["choices"])

def main() -> None:
    print(get_reply(response))              # expect: Hello, Vatsan!
    print(get_total_tokens(response))       # expect: 17
    print(list_model_and_reply(response))   # expect: Model llama-3.1 said: Hello, Vatsan!
    print(count_choices(response)) 

if __name__ == "__main__":
    main()