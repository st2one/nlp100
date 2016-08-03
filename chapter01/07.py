#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 07. テンプレートによる文生成

def template(x, y, z):
    return str(x)+"時の"+str(y)+"は"+str(z)

x = 12
y = "気温"
z = 22.4

answer = template(x, y, z)
print(answer)
