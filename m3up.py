#!/usr/bin/env python
# encoding: utf-8

import os
import re
import sys

from m3u_parser import M3uParser

def parse_and_filter_m3u(url):
    useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

    # Instantiate the parser
    parser = M3uParser(timeout=5, useragent=useragent)

    # Parse the m3u file
    parser.parse_m3u(url)

    # Remove by mp4 extension
    # parser.remove_by_extension('mp4')

    # Filter streams by status
    # parser.filter_by('status', 'GOOD')

    parser.sort_by("url", key_splitter="-", asc=True, nested_key=False)

    parser.remove_duplicates()

    # Get the list of streams
    streams = parser.get_list()
    print(len(streams))

    # Convert streams to JSON and save to a file
    parser.to_file(url, 'm3u')

# 检查命令行参数是否包含URL
if len(sys.argv) < 2:
    print("请提供URL参数")
    sys.exit(1)

# 获取URL参数
url = sys.argv[1]

# 在这里使用获取到的URL参数进行后续操作
print("传递的URL参数是:", url)
parse_and_filter_m3u(url)