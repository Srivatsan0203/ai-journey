# AI Journey 🚀

My hands-on path from **QA Automation Engineer** to **AI Engineer** — building
LLM-powered applications with a strong focus on **testing, evaluation, and
reliability** (leveraging my QA background as an edge).

## Why this repo exists

Most AI demos work once and break silently. Coming from QA automation, I care
about the opposite: **AI systems that are reproducible, testable, and observable.**
This repo tracks that learning journey, one small, working project at a time.

## Tech stack

- **Python 3.12**
- **OpenAI SDK** (provider-agnostic; currently pointed at [Groq](https://groq.com))
- **python-dotenv** for secrets management

## Projects

| Day | Project | Concepts |
|-----|---------|----------|
| 1 | `day1_hello.py` | venv, environment setup, first function |
| 2 | `day2_strings.py` | strings, f-strings, text normalization |
| 3 | `day3_data.py` | dicts, lists, navigating nested JSON |
| 4 | `day4_llm.py` | **first live LLM call**, system prompts, temperature, token usage |
| 5 | `day5_summary.py` | **structured JSON output**, F1 race summaries, first factual-accuracy check (eval) |
| 6 | `day6_fewshot.py` | **few-shot prompting**, zero-shot vs few-shot, constraining output to reduce hallucination |

## Running it locally

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows PowerShell

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key
#    Create a .env file (see .env.example) and add your key:
#    GROQ_API_KEY=your_key_here

# 4. Run a project
python day4_llm.py
```

## Notes on reliability (the QA angle)

- Secrets live in a **git-ignored `.env`** — never committed.
- LLM calls use `temperature=0` where **deterministic, testable output** is needed.
- Token usage is logged per call for **cost/latency awareness**.

---

*Work in progress — updated as I learn.*
