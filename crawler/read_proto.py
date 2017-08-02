#!/usr/bin/env python3
import os
import re

path = os.path.dirname(os.path.realpath(__file__)) + '/'
try:
    f = open('shooter.txt', 'r')
    proto = f.read()
    # print(proto)
    pattern = re.compile('.*?message (.*?)\s?{\n(.*?)\n}.*?', re.S)
    items = re.findall(pattern, proto)
    for item in items:
        print("------------item:-------------")
        print("messageName:", item[0], "\nmessageBody:\n", item[1])
finally:
    if f:
        f.close()
