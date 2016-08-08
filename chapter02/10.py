#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 10.py

import subprocess

cnt = 0
with open('data/hightemp.txt') as f:
    while f.readline():
        cnt += 1
print(cnt)

result = subprocess.call(['wc', '-l', 'data/hightemp.txt'])
print(result)
