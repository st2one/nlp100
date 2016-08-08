#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 14.py

"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import sys

params = sys.argv

n = 0
if len(params) > 2:
    n = params[1]
    filename = params[2]

with open(filename, 'r') as f:
    lines = f.readlines()

cnt = len(lines)
for line in lines[cnt-int(n):]:
    print(line.rstrip())

import subprocess

print("")
print("tail command")
cmd_paste = "tail -n " + n + " " + filename
result = subprocess.Popen(cmd_paste, shell=True)
stdout, stderr = result.communicate()
