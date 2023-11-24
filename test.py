#!/usr/bin/env python
# encoding: utf-8

import os
import re
import shutil

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

    print(url)
    # Convert streams to JSON and save to a file
    if (len(streams)):
     parser.to_file(url, 'm3u')


m3u_pattern = re.compile(r'^.*\.m3u$')  # 匹配以.m3u结尾的文件名
current_dir =  os.path.join(os.getcwd(), 'playlist')

for file_name in os.listdir(current_dir):
    if re.match(m3u_pattern, file_name):
        print(file_name)
        parse_and_filter_m3u(file_name)
        shutil.move(file_name, "./new/")


