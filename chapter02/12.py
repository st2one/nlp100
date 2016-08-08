#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 12.py

"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

with open("data/hightemp.txt") as f:
    lines = f.readlines()

col1 = []
col2 = []
for line in lines:
    cols = line.split("\t")
    col1.append(cols[0])
    col2.append(cols[1])
with open("data/col1.txt", "w") as f:
    for col in col1:
        f.write(col+"\n")
with open("data/col2.txt", "w") as f:
    for col in col2:
        f.write(col+"\n")

import subprocess

print("")
print("cut command")
cmd_expand = "cut -f1 data/hightemp.txt > data/cut_col1.txt"
result = subprocess.Popen(cmd_expand, shell=True)
stdout, stderr = result.communicate()

cmd_expand = "cut -f2 data/hightemp.txt > data/cut_col2.txt"
result = subprocess.Popen(cmd_expand, shell=True)
stdout, stderr = result.communicate()
