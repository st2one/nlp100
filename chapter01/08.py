#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 08. 暗号文

def cipher(text):
    ciphertext = "".join([chr(219-ord(char)) if char.isalpha() and char.islower() else char for char in text])
    return ciphertext

text = "I am an NLPer"
ciphertext = cipher(text)
decodetext = cipher(ciphertext)
print(ciphertext)
print(decodetext)
