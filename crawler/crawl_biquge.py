#!/usr/bin/env python3
# coding=utf-8

import re
import requests

base_biquge_url = 'http://www.biquge.info'


def dump_book(book_url, chapter_url, file):
    f = open(file, 'a', encoding='utf8')
    while chapter_url != book_url:
        title, text, chapter_url = load_page(book_url, chapter_url)
        print("下载：" + title)
        f.write(title)
        f.write(text + "\n\n")
    f.close()


def load_page(book_url, first_url):
    url = base_biquge_url + str(book_url) + str(first_url)
    response = requests.get(url)
    content = str(response.content, "utf-8")
    # 正则表达式
    text_pattern = re.compile('<div id="content">.*?<!--go-->(.*?)<!--over-->.*?</div>', re.S)
    title_pattern = re.compile('<div class="bookname">.*?<h1>(.*?)</h1>.*?</div>', re.S)
    pattern = re.compile(
        '<script language="javascript" type="text/javascript">.*?next_page = "(.*?)";var index_page.*?function jumpPage.*?</script>',
        re.S)
    text = re.findall(text_pattern, content)[0]
    title = re.findall(title_pattern, content)[0]
    next_url = re.findall(pattern, content)[0]
    text = format_html(text)
    return title, text, next_url


def format_html(html):
    html = html.replace("&nbsp;", " ")
    html = html.replace("<br/>", "\n")
    return html


if __name__ == "__main__":
    dump_book('/11_11668/', '5336378.html', 'gold_eys.txt')
