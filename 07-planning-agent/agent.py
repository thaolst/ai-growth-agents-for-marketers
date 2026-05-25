"""
07 — Planning Agent: Campaign Plan from Target
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

SYSTEM = """You are a growth strategist with deep experience in fintech and super apps in Southeast Asia.
You help growth marketers build campaign plans from targets — working backward from goals to tactics.
Always be direct. Flag unrealistic targets. Recommend based on what actually works, not what sounds good."""


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


def run_planning_agent(target_metric, target_number, baseline, budget, period, channels, context="", constraints=""):
    prompt = f"""I need a campaign plan for {period}.

Target metric: {target_metric}
Target: {target_number}
Current baseline: {baseline}
Budget: {budget}
Channels available: {channels}
Context: {context if context else "None"}
Constraints: {constraints if constraints else "None"}

Give me:
1. Gap analysis — how much do I need and where can it realistically come from
2. Overall strategy — main approach and why
3. Campaign breakdown — how many campaigns, what type, priority order
4. Budget allocation — how to split budget and why
5. Timeline — what runs first, what runs in parallel, what comes last
6. Top risks and how to handle them

Be direct. If the target is not achievable with this budget and timeline, say so."""

    print("Running planning agent...\n")
    ai_stream(SYSTEM, prompt)
    print("\n")


if __name__ == "__main__":
    print("=== Growth Planning Agent ===\n")

    target_metric = input("Target metric (e.g. MEU, transaction volume): ").strip()
    target_number = input("Target number: ").strip()
    baseline = input("Current baseline: ").strip()
    budget = input("Budget: ").strip()
    period = input("Period (e.g. July 2025, Q3 2025): ").strip()
    channels = input("Available channels (e.g. push, in-app, email): ").strip()
    context = input("Any special context (press Enter to skip): ").strip()
    constraints = input("Any constraints (press Enter to skip): ").strip()

    print("\n")
    run_planning_agent(target_metric, target_number, baseline, budget, period, channels, context, constraints)
