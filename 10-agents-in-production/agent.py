"""
10 — Agents in Production: Pre-deploy Review
Supports: Anthropic Claude, OpenAI GPT
Set AI_PROVIDER=openai in .env to use OpenAI
"""

import os
import json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# ── Provider setup ─────────────────────────────────────────────
PROVIDER = os.getenv("AI_PROVIDER", "anthropic").lower()

if PROVIDER == "openai":
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    MODEL = os.getenv("AI_MODEL", "gpt-4o")
else:
    from anthropic import Anthropic
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    MODEL = os.getenv("AI_MODEL", "claude-sonnet-4-20250514")

SYSTEM = """You are an expert at reviewing AI agent prompts for production readiness.
You identify failure modes, edge cases, and reliability issues before they happen in real usage.
Be specific and practical. Focus on what will actually break in real-world conditions."""


def ai_stream(system_prompt, user_prompt, max_tokens=1500):
    """Stream response from the configured AI provider."""
    if PROVIDER == "openai":
        stream = client.chat.completions.create(
            model=MODEL,
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            stream=True,
        )
        for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
    else:
        with client.messages.stream(
            model=MODEL,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)


def review_agent(agent_description, system_prompt, example_input, example_output):
    prompt = f"""Review this agent for production readiness:

Agent description: {agent_description}

System prompt being used:
{system_prompt}

Example input:
{example_input}

Output produced:
{example_output}

Review:
1. Prompt weaknesses — where could this produce inconsistent or wrong results
2. Edge cases not handled — unusual inputs that could cause failures
3. Specific prompt improvements to make output more reliable
4. What to monitor when running in production — warning signs of degraded performance
5. Production readiness verdict — deploy now, needs more testing, or needs redesign

Be direct. Point out real problems, not theoretical ones."""

    print("\nReviewing agent for production readiness...\n")
    print("=" * 50)
    ai_stream(SYSTEM, prompt)
    print("\n")

    # Log the review
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "agent": agent_description[:50],
        "reviewed": True,
    }

    with open("agent_review_log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    print("Review logged to agent_review_log.json")


if __name__ == "__main__":
    print("=== Agent Production Review ===\n")

    description = input("Describe your agent (what it does): ").strip()

    print("\nPaste your system prompt (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    system_prompt = "\n".join(lines[:-1])

    print("\nPaste an example input:")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    example_input = "\n".join(lines[:-1])

    print("\nPaste the output your agent produced:")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    example_output = "\n".join(lines[:-1])

    print()
    review_agent(description, system_prompt, example_input, example_output)
