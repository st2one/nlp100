#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def extract_uk():
    with open('data/jawiki-country.json', 'r') as f:
        line = f.readline()
        uk = ""
        while line:
            article = json.loads(line)
            if article["title"] == "イギリス":
                uk = article["text"]
                break
            line = f.readline()
    return uk
