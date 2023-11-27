"""
有一个名字叫site2.json的utf-8格式文件,包含如下内容:
{
"uuid":"e24b4542-ce5d-4625-b2cb-e40429945328",
"json":[{
"type":0,
"name":"唐人街",
"api":"https://www.tangrenjie.tv/api.php/provide/vod/at/xml"
},{
"type":8,
"name":"独播库",
"api":"https://raw.githubusercontent.com/trial/dp/master/json2/dbk.json"
}]
} 


1.要求使用python,
2.按照"api"字段排序父节点, 如果api字段相同,则删除重复api对应字段的父节点
3.检查所有api包含的链接是否可访问,如果不能访问,则删除它包含的父节点,
4.并做相应的异常处理包括SSLError, RequestException
5.要求同时处理10个节点,并打印处理进度
6.添加对应的段注释
请帮忙实现
"""
import json
import requests
from requests.exceptions import SSLError, RequestException
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

def check_api_availability(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return True
    except (SSLError, RequestException):
        return False

def process_node(node):
    api_url = node['api']
    if not check_api_availability(api_url):
        return None
    return node

def process_parent_nodes(parent_nodes):
    processed_nodes = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for node in parent_nodes:
            futures.append(executor.submit(process_node, node))
        for future in futures:
            if future.result():
                processed_nodes.append(future.result())
            print("Processed", len(processed_nodes), "out of", len(parent_nodes), "nodes")
    return processed_nodes

def sort_and_remove_duplicates(json_data):
    sorted_nodes = sorted(json_data['json'], key=lambda x: x['api'])
    unique_nodes = []
    prev_api = None
    for node in sorted_nodes:
        if node['api'] != prev_api:
            unique_nodes.append(node)
        prev_api = node['api']
    return unique_nodes

def main():
    # 读取并解析site2.json文件
    with open('site2.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # 按照api字段排序并删除重复的父节点
    unique_nodes = sort_and_remove_duplicates(json_data)

    # 处理父节点并检查api链接的可访问性
    processed_nodes = process_parent_nodes(unique_nodes)

    # 更新json_data并保存到新的json文件
    json_data['json'] = processed_nodes
    with open('processed_site2.json', 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()