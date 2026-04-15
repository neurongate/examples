"""
NeuronGate — Basic Chat Completion
"""
from openai import OpenAI

client = OpenAI(
    base_url="https://neurongate.net/v1",
    api_key="ng-your-api-key"
)

response = client.chat.completions.create(
    model="openai/gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the benefits of using an API gateway for AI?"}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
print(f"\nTokens: {response.usage.total_tokens}")
