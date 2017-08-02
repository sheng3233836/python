#!/usr/bin/env python3
# coding=utf-8

import re
import requests
import tensorflow


def loadPage(page):
    str_items = []
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    response = requests.get(url)
    content = str(response.content, "utf-8")
    pattern = re.compile('<div.*?content">\n*<span>(.*?)</span>\n*</div>(.*?)<div class="stats">', re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImg = re.search("img", item[1])
        if not haveImg:
            str_items.append(item[0])
    return str_items


str_items = loadPage(1)
for item in str_items:
    input_str = input()
    if input_str == "Q":
        break
    print(item)
