#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 21.py

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

import json
import re
from uk import extract_uk

def find_category(text):
    lines = text.split('\n')
    pattern = r"\[\[Category:(.*)\]\]"
    for line in lines:
        search_obj = re.search(pattern, line)
        if search_obj:
            print(line)

find_category(extract_uk())
