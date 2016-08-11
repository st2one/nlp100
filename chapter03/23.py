#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 21.py

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

import json
import re
from uk import extract_uk

def find_category(text):
    lines = text.split('\n')
    sec1 = r"==(.*)=="
    sec2 = r"===(.*)==="
    sec3 = r"====(.*)===="
    for line in lines:
        search_obj = re.search(sec3, line)
        if search_obj:
            print(search_obj.group(1), "3")
            continue
        search_obj = re.search(sec2, line)
        if search_obj:
            print(search_obj.group(1), "2")
            continue
        search_obj = re.search(sec1, line)
        if search_obj:
            print(search_obj.group(1), "1")
            continue

find_category(extract_uk())
