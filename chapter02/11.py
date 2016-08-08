#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 01.py

"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ
"""
import subprocess

cnt = 0
with open('data/hightemp.txt') as f:
    text = f.read().replace("\t", " ")
print("python")
print(text)

print("sed command")
cmd_sed = "sed -e s/\t/ /g data/hightemp.txt"
subprocess.call(['sed', '-e', 's/\t/ /g', 'data/hightemp.txt'])
cmd_tr = "cat data/hightemp.txt | tr '\t' ' '"
print("")
print("tr command")
result = subprocess.Popen(cmd_tr, shell=True)
stdout, stderr = result.communicate()

print("")
print("expand command")
cmd_expand = "expand -t 1 data/hightemp.txt"
result = subprocess.Popen(cmd_expand, shell=True)
stdout, stderr = result.communicate()
