import asyncio
from ollama import AsyncClient
import globals

asyncClient = AsyncClient(
    host=globals.ollamaHost,
    headers={'x-some-header': 'some-value'}
)


async def chat():
    message = {'role': 'user', 'content': 'Why is the sky blue?'}
    async for part in await asyncClient.chat(model='deepseek-r1', messages=[message], stream=True):
        print(part['message']['content'], end='', flush=True)


asyncio.run(chat())
