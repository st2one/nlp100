#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 04.py

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one = [1, 5, 6, 7, 9, 15, 16, 19]

words = text.replace('.', '').split(" ")
symbols = [words[i][0] if i+1 in one else words[i][0:2] for i in range(len(words))]
symbols_dic = {}
for i in range(len(symbols)):
    symbols_dic[i+1] = symbols[i]
print(symbols_dic)
