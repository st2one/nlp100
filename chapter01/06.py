#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 06. 集合

def word_ngram(sequence, n):
    sequence_type = type(sequence)
    if sequence_type is str:
        words = sequence.split(" ")
    elif sequenct_type is list:
        words = sequence
    ngram_words = [words[i:i+n] for i in range(len(words)-n+1)]
    return ngram_words

def char_ngram(sequence, n):
    sequence_type = type(sequence)
    if type(sequence) is str:
        text = sequence
    elif sequence_type is list:
        text = " ".join(sequence)
    ngram_chars = [text[i:i+n] for i in range(len(text)-n+1)]
    return ngram_chars

def no_space_char_ngram(sequence, n):
    sequence_type = type(sequence)
    if type(sequence) is str:
        text = sequence.replace(" ", "")
    elif sequence_type is list:
        text = " ".join(sequence).replace(" ", "")
    ngram_chars = [text[i:i+n] for i in range(len(text)-n+1)]
    return ngram_chars

text1 = "paraparaparadise"
text2 = "paragraph"

x = set(no_space_char_ngram(text1, 2))
y = set(no_space_char_ngram(text2, 2))

union = x.union(y)
intersection = x.intersection(y)
difference = x.difference(y)
se = "se"
is_se_x = se in x
is_se_y = se in y

print(union)
print(intersection)
print(difference)
print(is_se_x)
print(is_se_y)
