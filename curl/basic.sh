#!/bin/bash
# NeuronGate — Basic cURL Example

API_KEY="ng-your-api-key"

curl -X POST https://neurongate.net/v1/chat/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-4o",
    "messages": [
      {"role": "user", "content": "What is NeuronGate?"}
    ],
    "max_tokens": 200
  }'
