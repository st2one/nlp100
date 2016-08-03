#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 05. n-gram

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

text = "I am an NLPer"
word_bi_gram = word_ngram(text, 2)
char_bi_gram = char_ngram(text, 2)
no_space_char_bi_gram = no_space_char_ngram(text, 2)
print(word_bi_gram)
print(char_bi_gram)
print(no_space_char_bi_gram)
