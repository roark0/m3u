#!/usr/bin/env python
# encoding: utf-8

import os
import re
import sys
import shutil

from m3u_parser import M3uParser

def parse_and_filter_m3u(url,  sort='name', filter='GOOD'):
    print(f"sort={sort}")
    useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

    # Instantiate the parser
    parser = M3uParser(timeout=10, useragent=useragent)

    # Parse the m3u file
    parser.parse_m3u(url)

    # Remove by mp4 extension
    # parser.remove_by_extension('mp4')

    parser.sort_by(sort, key_splitter="-", asc=True, nested_key=False)

    parser.remove_duplicates()

    parser.filter_by('status', filter)

    # Get the list of streams
    streams = parser.get_list()
    print(len(streams))

    # base_name = os.path.basename(url)
    # file_name_without_ext = os.path.splitext(base_name)[0]
    # new_name = f"{file_name_without_ext}_{filter}.m3u"
    # print(new_name)
   
    # Convert bad streams to m3u and save to a file
    if (len(streams)):
        parser.to_file(url, 'm3u')

# 检查命令行参数是否包含URL
if len(sys.argv) < 2:
    print("请提供URL参数")
    sys.exit(1)

# 获取URL参数
url = sys.argv[1]
if len(sys.argv) >= 3:
    sort = sys.argv[2]
else:
    sort =  "url"

if (url == "all"):
    m3u_pattern = re.compile(r'^.*\.m3u$')  # 匹配以.m3u结尾的文件名
    current_dir =  os.path.join(os.getcwd(), './')
    print("传递的URL为:", url)
    print("排序的模式为:", sort)

    for file_name in os.listdir(current_dir):
        if re.match(m3u_pattern, file_name):
            print(file_name)
            parse_and_filter_m3u(file_name, sort)
            shutil.move(file_name, "./new/")
else:
    print(sort)
    # 在这里使用获取到的URL参数进行后续操作
    print("传递的URL为:", url)
    print("排序的模式为:", sort)
    parse_and_filter_m3u(url, sort)

