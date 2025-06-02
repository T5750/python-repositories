import requests

headers = {
    'Authorization': 'Bearer ACCESS_TOKEN'
}

response = requests.get('https://api.deepseek.com', headers=headers)

if response.status_code == 200:
    print(response.content)
else:
    print(f"Failed to retrieve image, status code: {response.status_code}")