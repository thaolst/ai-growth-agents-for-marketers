"""
04 — Tool Use: Campaign Data Analyzer
Supports: Anthropic Claude, OpenAI GPT
Set AI_PROVIDER=openai in .env to use OpenAI
"""

import os
import pandas as pd
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

SYSTEM = """You are a growth analyst. You analyze CSV data from marketing campaigns and give clear, actionable insights.
Focus on: what's working, what's not, and what to do next.
Keep analysis concise. Use numbers. No filler."""


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


def analyze_csv(file_path, question=""):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    df = pd.read_csv(file_path)

    summary = f"""Dataset: {file_path}
Shape: {df.shape[0]} rows, {df.shape[1]} columns
Columns: {', '.join(df.columns.tolist())}

First 5 rows:
{df.head().to_string()}

Basic stats:
{df.describe().to_string()}"""

    user_question = question if question else "Analyze this campaign data. What are the key insights and what should I do next?"
    prompt = f"{summary}\n\nQuestion: {user_question}"

    print(f"\nAnalyzing {file_path}...\n")
    print("=" * 50)
    ai_stream(SYSTEM, prompt)
    print("\n")


if __name__ == "__main__":
    print("=== Campaign Data Analyzer ===\n")
    file_path = input("Path to your CSV file: ").strip()
    question = input("What do you want to know? (press Enter for general analysis): ").strip()
    print()
    analyze_csv(file_path, question)
