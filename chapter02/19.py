#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 18.py

"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

from collections import Counter

with open('data/hightemp.txt', 'r') as f:
    lines = [line.split('\t')[0] for line in f.read().rstrip().split('\n')]
counter = Counter(lines)
for word, cnt in counter.most_common():
    print(cnt, word)

import subprocess

print("")
print("command")
cmd_paste = "cut -f1 data/hightemp.txt | sort | uniq -c | sort -r"
result = subprocess.Popen(cmd_paste, shell=True)
stdout, stderr = result.communicate()
