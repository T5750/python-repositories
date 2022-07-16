# https://www.imooc.com/code/22184
from urllib import request
import requests

CHAPTER_PREFIX = '=' * 50 + '> '

print(CHAPTER_PREFIX + '发送HTTP请求')
response = request.urlopen('https://www.imooc.com')  # 向慕课网官网发出请求
print(response)  # ==> <http.client.HTTPResponse object at 0x000001377D631948>
print(response.status)  # ==> 200
# HTTPResponse附带的一些信息
for k, v in response.getheaders():
    print('{}: {}'.format(k, v))

print(CHAPTER_PREFIX + 'requests库')
response = requests.get('https://www.imooc.com')
# 打印状态码
print(response.status_code)
# 打印回应头
print(response.headers)

print(CHAPTER_PREFIX + 'HTTP响应的内容')
response = requests.get('https://www.imooc.com')
content = str(response.content, encoding='utf-8')  # ==> 打印具体内容
content_list = content.split('\n')  # 分行
print(len(content_list))  # 打印页面内容的行数
# 通过字符串匹配的方式可以过滤出包含链接的行
for line in content_list:
    if 'href' in line and '">' in line:
        print(line.strip())
