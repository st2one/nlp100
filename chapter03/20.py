#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 20.py

"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json

with open('data/jawiki-country.json', 'r') as f:
    line = f.readline()
    while line:
        article = json.loads(line)
        if article["title"] == "イギリス":
            print(article["text"])
        line = f.readline()
