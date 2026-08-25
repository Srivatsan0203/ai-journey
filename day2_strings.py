"""Day 2: string manipulation utilities."""


def clean_text(text: str) -> str:
    return text.strip().lower()


def word_count(text: str) -> int:
    return len(text.split())


def format_greeting(name: str, day: int) -> str:
    return f"Hi {name}, welcome to day {day} of your AI journey!"


def main() -> None:
    print(clean_text("   HELLO World   "))          # expect: "hello world"
    print(format_greeting("Vatsan", 2))             # expect: "Hi Vatsan, welcome to day 2 of your AI journey!"
    print(word_count("This is day 2 of your AI journey!"))  # expect: 8


if __name__ == "__main__":
    main()




