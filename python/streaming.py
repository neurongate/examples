"""
NeuronGate — Streaming Responses
"""
from openai import OpenAI

client = OpenAI(
    base_url="https://neurongate.net/v1",
    api_key="ng-your-api-key"
)

stream = client.chat.completions.create(
    model="anthropic/claude-sonnet-4-6",
    messages=[
        {"role": "user", "content": "Write a short story about an AI that learns to paint."}
    ],
    stream=True,
    max_tokens=1000
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)

print()  # Final newline
