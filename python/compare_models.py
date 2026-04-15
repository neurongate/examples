"""
NeuronGate — Multi-Model Comparison

Compare the same prompt across different AI providers.
The key advantage: one API key, one SDK, multiple providers.
"""
from openai import OpenAI
import time

client = OpenAI(
    base_url="https://neurongate.net/v1",
    api_key="ng-your-api-key"
)

MODELS = [
    "openai/gpt-4o",
    "anthropic/claude-sonnet-4-6",
    "google/gemini-2.5-flash",
    "deepseek/deepseek-v3",
]

PROMPT = "Explain the CAP theorem in distributed systems. Be concise (3 sentences max)."

print(f"Prompt: {PROMPT}")
print("=" * 70)

for model in MODELS:
    start = time.time()
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": PROMPT}],
            max_tokens=200
        )
        elapsed = time.time() - start
        tokens = response.usage.total_tokens
        text = response.choices[0].message.content

        print(f"\n🧠 {model}")
        print(f"   Time: {elapsed:.2f}s | Tokens: {tokens}")
        print(f"   {text}")
    except Exception as e:
        print(f"\n❌ {model}: {e}")

print("\n" + "=" * 70)
print("All responses generated with a single API key and SDK.")
