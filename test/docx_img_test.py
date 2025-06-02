from io import BytesIO

import requests
from bs4 import BeautifulSoup
from docx import Document

url = 'https://www.baidu.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
document = Document()

for img in soup.find_all('img'):
    img_url = 'https:' + img['src']
    img_data = requests.get(img_url).content
    image_stream = BytesIO(img_data)
    document.add_picture(image_stream)
document.save('demo_img.docx')
