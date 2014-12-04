#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"
__project__ = ""

'edit Distance'

def minDistance(word1, word2):
    if word1 = word2:
        return 0
    if word1 in word2 or word2 in word1:
        return max(len(word1)-len(word2), len(word2)-len(word1))
    if word1 == "" :
        return len(word2)
    if word2 == "":
        return len(word1)
    # "abc" & "bcd"


'other function'

'怎么在python中指定生成一个 5* 6 数组呢'


def minDistance(word1, word2):
