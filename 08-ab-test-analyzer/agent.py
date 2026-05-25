"""
08 — A/B Test Analyzer
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

SYSTEM = """You are a data analyst specializing in growth marketing experiments.
You analyze A/B test results and explain findings in plain language that marketers can act on immediately.
Always calculate statistical significance. Never declare a winner without sufficient sample size.
Flag when results are inconclusive and give clear guidance on what to do next."""


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


def run_ab_analyzer(test_name, hypothesis, days_run, primary_metric,
                     control_users, control_conversions,
                     variant_users, variant_conversions,
                     secondary_metrics="", segment_breakdown=""):

    control_rate = control_conversions / control_users * 100
    variant_rate = variant_conversions / variant_users * 100
    lift = (variant_rate - control_rate) / control_rate * 100

    prompt = f"""Analyze this A/B test result:

Test: {test_name}
Hypothesis: {hypothesis}
Days run: {days_run}
Primary metric: {primary_metric}

Control (A): {control_users:,} users, {control_conversions:,} conversions ({control_rate:.2f}%)
Variant (B): {variant_users:,} users, {variant_conversions:,} conversions ({variant_rate:.2f}%)
Observed lift: {lift:.1f}%

Secondary metrics: {secondary_metrics if secondary_metrics else "None provided"}
Segment breakdown: {segment_breakdown if segment_breakdown else "None provided"}

Tell me:
1. Winner — A, B, or no winner yet — and why
2. Statistical confidence level — is this result trustworthy
3. If not confident — how much more sample or how many more days needed
4. Any notable patterns in segment breakdown
5. Recommended action: rollout, keep testing, or stop

Use plain language. No statistical jargon. I need to make a decision today."""

    print(f"\nAnalyzing: {test_name}\n")
    print(f"Control: {control_rate:.2f}% | Variant: {variant_rate:.2f}% | Lift: {lift:+.1f}%\n")
    print("=" * 50)
    ai_stream(SYSTEM, prompt)
    print("\n")


if __name__ == "__main__":
    print("=== A/B Test Analyzer ===\n")

    test_name = input("Test name: ").strip()
    hypothesis = input("Hypothesis (what were you testing): ").strip()
    days_run = input("Days run: ").strip()
    primary_metric = input("Primary metric (e.g. click rate, conversion rate): ").strip()

    print("\n- Control (A) -")
    control_users = int(input("Number of users: ").strip().replace(",", ""))
    control_conversions = int(input("Number of conversions: ").strip().replace(",", ""))

    print("\n- Variant (B) -")
    variant_users = int(input("Number of users: ").strip().replace(",", ""))
    variant_conversions = int(input("Number of conversions: ").strip().replace(",", ""))

    secondary = input("\nSecondary metrics (press Enter to skip): ").strip()
    segments = input("Segment breakdown (press Enter to skip): ").strip()

    print()
    run_ab_analyzer(test_name, hypothesis, days_run, primary_metric,
                    control_users, control_conversions,
                    variant_users, variant_conversions,
                    secondary, segments)
