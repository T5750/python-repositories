from ollama import Client
import globals

client = Client(
    host=globals.ollamaHost,
    headers={'x-some-header': 'some-value'}
)

response = client.chat(model='llama3.2-vision', messages=[
    {
        'role': 'user',
        'content': '用中文回答，提取图中的所有信息',
        # https://ollama.com/public/blog/wordart.jpg
        'images': ['D:\wordart.jpg']
    },
])
print(response['message']['content'])
