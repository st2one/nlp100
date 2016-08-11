#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 21.py

"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""

import json
import re
from uk import extract_uk

def find_category(text):
    lines = text.split('\n')
    file_pattern = r"\[\[ファイル:(.*)\]\]"
    for line in lines:
        search_obj = re.search(file_pattern, line)
        if search_obj:
            print(search_obj.group(1))

find_category(extract_uk())
