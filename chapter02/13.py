#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 12.py

"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""

with open("data/col1.txt") as f:
    cols1 = f.read().rstrip().split('\n')
with open("data/col2.txt") as f:
    cols2 = f.read().rstrip().split('\n')
merge = []
for col1, col2 in zip(cols1, cols2):
    merge.append(col1 + "\t" + col2)

with open("data/merge.txt", "w") as f:
    for m in merge:
        f.write(m+"\n")

import subprocess

print("")
print("paste command")
cmd_paste = "paste data/cut_col1.txt data/cut_col2.txt > data/merge_paste.txt"
result = subprocess.Popen(cmd_paste, shell=True)
stdout, stderr = result.communicate()
