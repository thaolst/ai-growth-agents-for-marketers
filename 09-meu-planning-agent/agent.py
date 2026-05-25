"""
09 — MEU Planning Agent: Campaign Plan from MEU Target
Supports: Anthropic Claude, OpenAI GPT
Set AI_PROVIDER=openai in .env to use OpenAI
"""

import os
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

SYSTEM = """You are a growth strategist specializing in MEU (Monthly Engaging Users) growth for fintech apps in Southeast Asia.
You work backward from targets — given a goal, you figure out what campaigns and mechanics are needed to hit it.
Be realistic. If a target is not achievable with the given resources, say so clearly and explain what is achievable.
Always give specific numbers, not ranges when possible. Base recommendations on realistic conversion rates for the industry."""


def ai_stream(system_prompt, user_prompt, max_tokens=2000):
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


def run_meu_agent(target_meu, current_meu, budget, days_remaining, channels, segments, constraints=""):
    gap = target_meu - current_meu

    prompt = f"""I need to hit my MEU target this month.

MEU target: {target_meu:,}
Current MEU: {current_meu:,}
Gap: {gap:,} ({gap/current_meu*100:.1f}% increase needed)
Budget: {budget}
Days remaining: {days_remaining}
Available channels: {channels}
User segments available: {segments}
Constraints: {constraints if constraints else "None"}

Give me:
1. Gap analysis — is this achievable, where does the MEU come from
2. Top 2-3 campaigns with specific mechanics, target segment, budget, and expected MEU contribution
3. Total expected MEU from all campaigns + confidence level
4. Plan B if primary plan falls short
5. One thing I should NOT do (common mistake for this type of target)

Be direct. Show your math. If I can realistically only hit 80% of target, tell me now."""

    print(f"\nMEU Gap: {gap:,} ({gap/current_meu*100:.1f}% needed)\n")
    print("Running MEU planning agent...\n")
    print("=" * 50)
    ai_stream(SYSTEM, prompt)
    print("\n")


if __name__ == "__main__":
    print("=== MEU Planning Agent ===\n")

    target_meu = int(input("MEU target this month: ").strip().replace(",", ""))
    current_meu = int(input("Current MEU (start of month): ").strip().replace(",", ""))
    budget = input("Available budget: ").strip()
    days_remaining = input("Days remaining this month: ").strip()
    channels = input("Available channels (e.g. push, in-app, email): ").strip()
    segments = input("User segments (brief description): ").strip()
    constraints = input("Any constraints (press Enter to skip): ").strip()

    print()
    run_meu_agent(target_meu, current_meu, budget, days_remaining, channels, segments, constraints)
