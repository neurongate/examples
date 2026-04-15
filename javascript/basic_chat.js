/**
 * NeuronGate — Basic Chat Completion (Node.js)
 * 
 * npm install openai
 */
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://neurongate.net/v1',
  apiKey: 'ng-your-api-key',
});

async function main() {
  const response = await client.chat.completions.create({
    model: 'anthropic/claude-sonnet-4-6',
    messages: [
      { role: 'system', content: 'You are a helpful assistant.' },
      { role: 'user', content: 'Explain microservices in 3 sentences.' },
    ],
    max_tokens: 200,
  });

  console.log(response.choices[0].message.content);
  console.log(`\nTokens: ${response.usage.total_tokens}`);
}

main();
