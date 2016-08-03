#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 03.py

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
answer = list(map(lambda x: len(x), text.replace(',', '').replace('.', '').split(" ")))
print(answer)
