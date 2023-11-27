import requests
from requests.exceptions import SSLError, RequestException
import json

# 读取site2.json文件内容
with open('site2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 按照"name"字段排序父节点
sorted_json = sorted(data['json'], key=lambda x: x['api'])

# 检查链接是否可访问的函数
def check_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except (SSLError, RequestException):
        return False

# 一次处理5个节点
# batch_size = 5
# for i in range(0, len(sorted_json), batch_size):
#     batch = sorted_json[i:i+batch_size]
#     for node in batch:
#         print(f"check  {node['name']}:")
#         api_url = node['api']
#         if not check_url(api_url):
#             sorted_json.remove(node)

# 更新json数据
data['json'] = sorted_json

# 将更新后的数据写入site2.json文件
with open('site22.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)