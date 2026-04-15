<div align="center">

# NeuronGate Code Examples

Real-world examples for integrating NeuronGate into your applications.

[![Docs](https://img.shields.io/badge/Full_Docs-neurongate/docs-6366f1?style=flat-square)](https://github.com/neurongate/docs)
[![Website](https://img.shields.io/badge/neurongate.net-8b5cf6?style=flat-square)](https://neurongate.net)

</div>

---

## Examples

| Example | Language | Description |
|---------|----------|-------------|
| [Basic Chat](#basic-chat) | Python, JS, cURL | Simple chat completion |
| [Streaming](#streaming) | Python, JS | Real-time token streaming |
| [Multi-Model](#multi-model-comparison) | Python | Compare responses across providers |
| [Vision](#vision--image-analysis) | Python | Analyze images with vision models |
| [Function Calling](#function-calling) | Python | Tool use with structured outputs |
| [Embeddings](#embeddings) | Python | Generate text embeddings |
| [RAG Pipeline](#rag-pipeline) | Python | Retrieval-augmented generation |
| [Error Handling](#production-error-handling) | Python | Robust production patterns |

---

## Basic Chat

### Python

```python
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
print(f"Tokens used: {response.usage.total_tokens}")
```

### JavaScript / TypeScript

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://neurongate.net/v1',
  apiKey: 'ng-your-api-key',
});

async function chat() {
  const response = await client.chat.completions.create({
    model: 'anthropic/claude-sonnet-4-6',
    messages: [
      { role: 'user', content: 'Explain microservices in 3 sentences.' }
    ],
  });

  console.log(response.choices[0].message.content);
}

chat();
```

### cURL

```bash
curl -X POST https://neurongate.net/v1/chat/completions \
  -H "Authorization: Bearer ng-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "google/gemini-2.5-flash",
    "messages": [
      {"role": "user", "content": "What is a neural network?"}
    ],
    "max_tokens": 200
  }'
```

---

## Streaming

### Python

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://neurongate.net/v1",
    api_key="ng-your-api-key"
)

stream = client.chat.completions.create(
    model="anthropic/claude-sonnet-4-6",
    messages=[
        {"role": "user", "content": "Write a short story about a robot learning to paint."}
    ],
    stream=True,
    max_tokens=1000
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)

print()  # Final newline
```

### JavaScript

```typescript
const stream = await client.chat.completions.create({
  model: 'openai/gpt-4o',
  messages: [{ role: 'user', content: 'Tell me a joke' }],
  stream: true,
});

for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) process.stdout.write(content);
}
```

---

## Multi-Model Comparison

Compare the same prompt across different providers:

```python
from openai import OpenAI
import time

client = OpenAI(
    base_url="https://neurongate.net/v1",
    api_key="ng-your-api-key"
)

models = [
    "openai/gpt-4o",
    "anthropic/claude-sonnet-4-6",
    "google/gemini-2.5-flash",
    "meta/llama-4-maverick",
    "deepseek/deepseek-v3",
]

prompt = "Explain the CAP theorem in distributed systems. Be concise."

for model in models:
    start = time.time()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    elapsed = time.time() - start
    tokens = response.usage.total_tokens

    print(f"\n{'='*60}")
    print(f"Model: {model}")
    print(f"Time: {elapsed:.2f}s | Tokens: {tokens}")
    print(f"{'='*60}")
    print(response.choices[0].message.content)
```

---

## Vision / Image Analysis

```python
response = client.chat.completions.create(
    model="openai/gpt-4o",  # or google/gemini-2.5-pro
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image? Describe it in detail."},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/photo.jpg"}
                }
            ]
        }
    ],
    max_tokens=500
)

print(response.choices[0].message.content)
```

---

## Function Calling

```python
import json

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="openai/gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools,
    tool_choice="auto"
)

tool_call = response.choices[0].message.tool_calls[0]
args = json.loads(tool_call.function.arguments)
print(f"Function: {tool_call.function.name}")
print(f"Arguments: {args}")
```

---

## Embeddings

```python
response = client.embeddings.create(
    model="openai/text-embedding-3-small",
    input=["NeuronGate is an AI API gateway", "Machine learning is fascinating"],
    encoding_format="float"
)

for i, embedding in enumerate(response.data):
    print(f"Text {i}: {len(embedding.embedding)} dimensions")
```

---

## RAG Pipeline

Retrieval-Augmented Generation with NeuronGate:

```python
import numpy as np
from openai import OpenAI

client = OpenAI(
    base_url="https://neurongate.net/v1",
    api_key="ng-your-api-key"
)

# Step 1: Embed your documents
documents = [
    "NeuronGate supports 50+ AI models from 8 providers.",
    "You can pay with USDT, USDC, ETH, or BTC.",
    "The API is fully OpenAI-compatible.",
    "Rate limits depend on your tier: Free, Standard, Pro, Enterprise.",
]

doc_embeddings = client.embeddings.create(
    model="openai/text-embedding-3-small",
    input=documents
).data

# Step 2: Embed the query
query = "How do I pay for NeuronGate?"
query_embedding = client.embeddings.create(
    model="openai/text-embedding-3-small",
    input=[query]
).data[0].embedding

# Step 3: Find most relevant documents (cosine similarity)
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

scores = [cosine_sim(query_embedding, d.embedding) for d in doc_embeddings]
top_docs = sorted(zip(scores, documents), reverse=True)[:2]

context = "\n".join([doc for _, doc in top_docs])

# Step 4: Generate answer with context
response = client.chat.completions.create(
    model="anthropic/claude-sonnet-4-6",
    messages=[
        {"role": "system", "content": f"Answer based on this context:\n{context}"},
        {"role": "user", "content": query}
    ]
)

print(response.choices[0].message.content)
```

---

## Production Error Handling

Robust patterns for production use:

```python
from openai import OpenAI
import openai
import time

client = OpenAI(
    base_url="https://neurongate.net/v1",
    api_key="ng-your-api-key",
    timeout=30.0,
    max_retries=3
)

def chat_with_fallback(prompt: str, primary="openai/gpt-4o", fallback="google/gemini-2.5-flash"):
    """Try primary model, fall back on failure."""
    for model in [primary, fallback]:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            return response.choices[0].message.content, model
        except openai.RateLimitError:
            print(f"Rate limited on {model}, trying fallback...")
            time.sleep(1)
        except openai.APIStatusError as e:
            if e.status_code == 402:
                raise Exception("Insufficient balance — top up at neurongate.net/topup")
            print(f"Error on {model}: {e.status_code}, trying fallback...")
        except openai.APIConnectionError:
            print(f"Connection error on {model}, trying fallback...")

    raise Exception("All models failed")

# Usage
text, used_model = chat_with_fallback("Explain quantum computing")
print(f"Response from {used_model}:\n{text}")
```

---

## More Resources

- 📖 [Full API Documentation](https://github.com/neurongate/docs)
- 🌐 [neurongate.net](https://neurongate.net)
- 🔑 [Get your API key](https://neurongate.net/keys)
- 💰 [Top up balance](https://neurongate.net/topup)

---

<div align="center">
<sub>© 2026 NeuronGate</sub>
</div>
