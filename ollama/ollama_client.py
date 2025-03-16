from ollama import Client
import globals

client = Client(
    host=globals.ollamaHost,
    headers={'x-some-header': 'some-value'}
)

response = client.chat(model='deepseek-r1', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
])
print(response['message']['content'])
