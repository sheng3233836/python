#!/usr/bin/env python3
# coding=utf-8

import re
import sys, getopt
import requests
from lxml import etree

base_biquge_url = 'http://www.biquge.info'


def format_html(html):
    html = html.replace("&nbsp;", " ")
    html = html.replace("<br/>", "\n")
    return html


def load_page(book_url, chapter_url):
    url = base_biquge_url + str(book_url) + str(chapter_url)
    response = requests.get(url)
    content = str(response.content, "utf-8")
    # 正则表达式
    text_pattern = re.compile('<div id="content">.*?<!--go-->(.*?)<!--over-->.*?</div>', re.S)
    title_pattern = re.compile('<div class="bookname">.*?<h1>(.*?)</h1>.*?</div>', re.S)
    pattern = re.compile('<script language="javascript".*?next_page = "(.*?)";var index_page.*?</script>', re.S)

    text = re.findall(text_pattern, content)[0]
    title = re.findall(title_pattern, content)[0]
    next_url = re.findall(pattern, content)[0]
    text = format_html(text)
    return title, text, next_url


def get_first_url(book_url):
    url = base_biquge_url + str(book_url)
    response = requests.get(url)
    html = str(response.content, "utf-8")
    selector = etree.HTML(html)
    first_url = selector.xpath('//*[@id="list"]/dl/dd[1]/a/@href')[0]
    if first_url == '':
        print("开始页面获取失败")
        sys.exit()
    print("开始页面：" + first_url)
    return first_url


def dump_book(book_url, file, first_url=''):
    f = open(file, 'a', encoding='utf8')
    chapter_url = first_url
    if chapter_url == '':
        chapter_url = get_first_url(book_url)
    while chapter_url != book_url:
        title, text, chapter_url = load_page(book_url, chapter_url)
        print("下载：" + title)
        f.write(title)
        f.write(text + "\n\n")
    f.close()


def main(argv):
    book_id = ''
    outfile = ''
    first_chapter_rl = ''
    try:
        opts, args = getopt.getopt(argv, 'hb:o:f:')  # 短格式 --- h 后面没有冒号：表示后面不带参数，b：和 o：后面有冒号表示后面需要参数
    except getopt.GetoptError:
        print("crawl_biquge.py -b <book_id> -o <outfile> [-f <first_chapter_rl>]")
        sys.exit()

    for opt, value in opts:
        if opt == '-h':
            print("crawl_biquge.py -b <book_id> -o <outfile> [-f <first_chapter_rl>]")
            sys.exit()
        elif opt == '-b':
            book_id = value
        elif opt == '-o':
            outfile = value
        elif opt == '-f':
            first_chapter_rl = value

    if book_id != '' and outfile != '':
        if first_chapter_rl != '':
            dump_book('/' + book_id + '/', outfile, first_chapter_rl)
        else:
            dump_book('/' + book_id + '/', outfile)
    else:
        print("must need book_id and outfile")
        print("this usage : crawl_biquge.py -b <book_id> -o <outfile> [-f <first_chapter_rl>]")


if __name__ == "__main__":
    main(sys.argv[1:])
    # dump_book('/11_11668/', 'gold_eys.txt')
