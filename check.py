#!/usr/bin/env python
# encoding: utf-8

import requests
from requests.exceptions import SSLError

def process_m3u_url(url):
    # 发送HTTP请求获取链接内容
    try:
        response = requests.get(url)
        # 在这里处理正常的响应
        print(response.text)
        link_content = response.text

        link_status_code = response.status_code

        print(link_status_code)
        # 在这里处理链接内容
        # process_link_content(link_content)
    except SSLError as e:
        # 在这里处理SSLError异常
        print("发生了SSLError异常:", e)
        # 其他错误处理逻辑

def process_link_content(link_content):
    # 在这里编写处理链接内容的逻辑
    print("链接内容：")
    print(link_content)

# 获取用户输入的M3U链接
# m3u_url = input("请输入M3U链接：")
m3u_url = "https://files.honghufly.com/index/m3u8/id/10035/"

# 处理M3U链接
process_m3u_url(m3u_url)


import json

with open('./iplayr/site2.json', 'r') as file:
    data = json.load(file)

# 获取所有api字段的值
api_fields = [item['api'] for item in data['json']]


print(api_fields)


