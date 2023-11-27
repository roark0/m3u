#!/usr/bin/env python
# encoding: utf-8

import requests
import json
from requests.exceptions import SSLError, RequestException

def check_api_links(data):
    for item in data['json']:
        api_url = item['api']
        print(f"check  {item['name']}:")
        try:
            response = requests.get(api_url)
            print(f"status_code: {response.status_code}")
            # if response.status_code != 200:
            #     data['json'].remove(item)
            #     print(f"Removed parent node with API: {api_url}")
        except RequestException as e:
            data['json'].remove(item)
            print(f"Removed parent node with API: {item['name']} + {api_url}")
        except SSLError as e:
            data['json'].remove(item)
            print(f"Removed parent node with API: {item['name']} + {api_url}")

        # except http.client.RemoteDisconnected as e:
        #     # 处理 http.client.RemoteDisconnected 异常
        #     print(f"A RemoteDisconnected error occurred while accessing API: {api_url}")
        #     print(f"Error details: {str(e)}")
        #     # 其他异常处理逻辑
        #     # ...
        # except MaxRetryError as e:
        #     # 处理 MaxRetryError 异常
        #     print(f"A MaxRetryError occurred while accessing API: {api_url}")
        #     print(f"Error details: {str(e)}")

# 读取site2.json文件
with open('site2.json', 'r') as file:
    content = file.read()

# 解析JSON数据
data = json.loads(content)

# 检查API链接并删除不可访问的父节点
check_api_links(data)

# 将更新后的数据写回到site2.json文件
with open('site21.json', 'w') as file:
    file.write(json.dumps(data, indent=4))