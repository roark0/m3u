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
5.要求一次处理5个节点,并打印处理进度
6.添加对应的段注释
请帮忙实现
"""
import requests
from requests.exceptions import SSLError, RequestException
import json

def check_api_availability(api):
    try:
        response = requests.get(api, timeout=5)
        # return response.status_code == 200
        return True
    except (SSLError, RequestException):
        return False

def process_nodes(nodes):
    sorted_nodes = sorted(nodes, key=lambda x: x['api'])  # 按照"api"字段排序父节点
    unique_apis = []
    processed_nodes = []

    for node in sorted_nodes:
        if node['api'] not in unique_apis:  # 如果api字段不重复
            unique_apis.append(node['api'])
            if check_api_availability(node['api']):  # 检查api是否可访问
                processed_nodes.append(node)
                print("已处理节点:", node)
            else:
                print("无法访问的API链接:", node['api'])
        else:
            print("重复的API链接，已删除节点:", node)

    return processed_nodes

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        json_data = data['json']
        total_nodes = len(json_data)
        processed_data = []
        for i in range(0, total_nodes, 5):
            batch_nodes = json_data[i:i+5]
            processed_nodes = process_nodes(batch_nodes)
            processed_data.extend(processed_nodes)
            print("进度: {}/{}".format(i + len(batch_nodes), total_nodes))
        
        data['json'] = processed_data

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 调用函数处理site2.json文件
process_file('site2.json')