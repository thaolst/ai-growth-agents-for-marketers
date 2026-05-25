"""
05 — Multi-Agent Workflow: Research → Plan
Supports: Anthropic Claude, OpenAI GPT
Set AI_PROVIDER=openai in .env to use OpenAI
"""

import os
import json
from dotenv import load_dotenv

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

ANALYST_SYSTEM = """You are a campaign data analyst. Extract structured insights from campaign data.
Return ONLY valid JSON. No explanation, no markdown, no backticks."""

STRATEGIST_SYSTEM = """You are a growth strategist for a fintech app in Southeast Asia.
You receive analyst findings and turn them into concrete campaign plans.
Be specific. Use numbers. Justify every recommendation with data from the analysis."""


def ai_create(system_prompt, user_prompt, max_tokens=1000):
    """Non-streaming response from the configured AI provider."""
    if PROVIDER == "openai":
        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.choices[0].message.content
    else:
        response = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text


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


def run_analyst(data_input):
    prompt = f"""Analyze this campaign data and return structured insights:

{data_input}

Return JSON with these fields:
- top_performing_mechanics: list with mechanic name and why it worked
- underperforming_areas: list with area and suspected reason
- segment_insights: which user segments responded well or poorly
- recommended_focus: top 3 things strategist should prioritize
- data_gaps: what information is missing for better analysis"""

    return ai_create(ANALYST_SYSTEM, prompt)


def run_strategist(analyst_output, target, budget, timeline):
    prompt = f"""You received this analysis from your analyst:

{analyst_output}

Build a campaign plan:
- Target: {target}
- Budget: {budget}
- Timeline: {timeline}

Give a specific plan with campaign names, mechanics, budget split, and timeline.
Reference the analyst findings to justify your recommendations."""

    print("\nStrategist building plan...\n")
    print("=" * 50)
    ai_stream(STRATEGIST_SYSTEM, prompt)
    print("\n")


if __name__ == "__main__":
    print("=== Multi-Agent: Research → Plan ===\n")

    print("Step 1: Paste your campaign data (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    data = "\n".join(lines[:-1])

    print("\nAnalyst processing data...")
    analyst_output = run_analyst(data)

    print("\nAnalysis complete:")
    print(analyst_output)

    print("\nStep 2: Define your campaign parameters")
    target = input("Target (e.g. MEU 500k, 20% transaction growth): ").strip()
    budget = input("Budget: ").strip()
    timeline = input("Timeline (e.g. July 2025, Q3): ").strip()

    run_strategist(analyst_output, target, budget, timeline)
