#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 21.py

"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import json
import re
from uk import extract_uk

def find_category(text):
    lines = text.split('\n')
    pattern = r"\[\[Category:(.*)\]\]"
    pattern2 = r"(.*)\|(.*)"
    for line in lines:
        search_obj = re.search(pattern, line)
        if search_obj:
            category = search_obj.group(1)
            search_obj2 = re.search(pattern2, category)
            if search_obj2:
                print(search_obj2.group(1))
            else:
                print(category)

find_category(extract_uk())
