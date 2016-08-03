#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 09. Typoglycemia

import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = text.split(" ")
random_words = []
for word in words:
    if len(word) < 4:
        random_words.append(word)
    else:
        word_list = list(word)
        middle = word_list[1:-1]
        random.shuffle(middle)
        random_words.append(word_list[0]+"".join(middle)+word_list[-1])
answer = " ".join(random_words)
print(answer)
