/**
 * NeuronGate — Streaming (Node.js)
 * 
 * npm install openai
 */
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://neurongate.net/v1',
  apiKey: 'ng-your-api-key',
});

async function main() {
  const stream = await client.chat.completions.create({
    model: 'openai/gpt-4o',
    messages: [
      { role: 'user', content: 'Write a haiku about artificial intelligence.' },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content;
    if (content) process.stdout.write(content);
  }
  
  console.log(); // Final newline
}

main();
