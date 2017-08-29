#! /usr/bin/env python
# coding: utf-8
import sys, os, random
import time
import tqdm

folder_path = "captcha-small"
pathDir = os.listdir(folder_path)
random.shuffle(pathDir)
print(pathDir[len(pathDir) - 2000:len(pathDir)])
