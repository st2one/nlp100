#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 25.py

"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import json
import re
from uk import extract_uk

def extract_template(text):
    lines = text.split('\n')
    file_pattern = r"^\|(.*) = (.*)"
    info_dict = {}
    for line in lines:
        search_obj = re.search(file_pattern, line)
        if search_obj:
            info_dict[search_obj.group(1)] = search_obj.group(2)
    print(info_dict)

extract_template(extract_uk())
