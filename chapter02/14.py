#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 14.py

"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

import sys

params = sys.argv

n = 0
if len(params) > 2:
    n = int(params[1])
    filename = params[2]

cnt = n
with open(filename, 'r') as f:
    line = f.readline().rstrip()
    while line:
        print(line)
        line = f.readline().rstrip()
        cnt -= 1
        if cnt < 1:
            break
    
import subprocess

print("")
print("head command")
cmd_paste = "head -n " + str(n) + " " + filename
result = subprocess.Popen(cmd_paste, shell=True)
stdout, stderr = result.communicate()
