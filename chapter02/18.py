#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 18.py

"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

with open('data/hightemp.txt', 'r') as f:
    lines = [line.split('\t') for line in f.read().rstrip().split('\n')]
sorted_lines = sorted(lines, key=lambda x: x[2])
print(sorted_lines)

import subprocess

print("")
print("sort command")
cmd_paste = "sort -k 3 data/hightemp.txt"
result = subprocess.Popen(cmd_paste, shell=True)
stdout, stderr = result.communicate()
