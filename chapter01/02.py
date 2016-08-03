#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 02.py

text1 = "パトカー"
text2 = "タクシー"
answer = "".join([(c1 + c2) for c1, c2 in zip(text1, text2)])
print(answer)
