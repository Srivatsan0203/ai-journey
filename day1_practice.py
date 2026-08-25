"""Day 1 smoke test: prove the environment is wired up correctly."""

import sys          # standard library: info about the running Python
import openai        # the package we installed into the venv


def greet(name: str) -> str:
    return f"Hello, {name}, welcome to AI Engineering!"


def main() -> None:
    # sys.version is a string describing this exact Python interpreter.
    print("Hello, AI engineer!")
    print(f"Python version: {sys.version.split()[0]}")

    # sys.prefix should point INSIDE our .venv folder if the venv is active.
    print(f"Running from:   {sys.prefix}")

    # If this line runs without error, the openai package imported successfully.
    print(f"openai SDK:     {openai.__version__}")

    print(greet("Vatsan"))


if __name__ == "__main__":
    main()




