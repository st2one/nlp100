#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 26.py

"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""

import json
import re
from uk import extract_uk

def remove_emphasis(text):
    lines = text.split('\n')
    file_pattern = r"^\|(.*) = (.*)"
    emphasis_pattern = r"\'{2,5}"

    info_dict = {}
    for line in lines:
        search_obj = re.search(file_pattern, line)
        if search_obj:
            info_dict[search_obj.group(1)] = re.sub(emphasis_pattern, "", search_obj.group(2))
    print(info_dict)

remove_emphasis(extract_uk())
