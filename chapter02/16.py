#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 14.py

"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

import sys

params = sys.argv

n = 0
print(params)
if len(params) > 3:
    n = int(params[1])
    inputfile = params[2]
    outputfile = params[3]
else:
    sys.exit()

with open(inputfile, 'r') as f:
    lines = f.readlines()

step = int(len(lines) / n)

splited_lines = []
for i in range(0, n):
    if i == n-1:
        block = lines[i*step:len(lines)]
    else:
        block = lines[i*step:(i+1)*step]  
    splited_lines.append(block)

for i in range(0, n):
    with open("data/" + str(i) + "_" + outputfile, "w") as f:
        for line in splited_lines[i]:
            f.write(line)

import subprocess

print("")
print("split command")
cmd_paste = "split -l " + str(step) + " " + inputfile + " data/command_" + outputfile
result = subprocess.Popen(cmd_paste, shell=True)
stdout, stderr = result.communicate()
