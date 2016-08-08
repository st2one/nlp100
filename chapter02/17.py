#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 14.py

"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""

with open('data/hightemp.txt', 'r') as f:
    lines = f.read().rstrip().split('\n')
    first_lines_set = set([line.split('\t')[0] for line in lines])

print(first_lines_set)
import subprocess

print("")
print("sort command")
cmd_paste = "cut -f1 data/hightemp.txt | sort | uniq"
result = subprocess.Popen(cmd_paste, shell=True)
stdout, stderr = result.communicate()
