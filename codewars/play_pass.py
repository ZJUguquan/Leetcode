#! /usr/bin/python
# coding: utf-8
# Thursday, January 14, 2016

from __future__ import print_function
import re
import sys
import os
import matplotlib as mpl
import seaborn as sns
from matplotlib import pyplot as plt
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

# playing with passphrases

#1 circular shift

def play_pass(s, n):
    """
    shift each letter by a given number but the transformed letter must be a letter (circular shift),
replace each digit by its complement to 9,
keep such as non alphabetic and non digit characters,
downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
reverse the whole result.

    """
    from string import ascii_lowercase, ascii_uppercase, punctuation, whitespace
    news = ''
    llower = ascii_lowercase * 2
    uuper = ascii_uppercase * 2
    for idx, ch in enumerate(s):
        if ch in punctuation + whitespace:
            news += ch
        if ch in ascii_lowercase:
            news += llower[ascii_lowercase.index(ch) + n] if idx % 2  else llower[ascii_lowercase.index(ch) + n].upper()
        if ch in ascii_uppercase:
            news += uuper[ascii_uppercase.index(ch) + n] if idx % 2 ==0 else uuper[ascii_uppercase.index(ch) + n].lower()
        if ch in '0123456789':
            news += str(9-int(ch))

    return news[::-1]

s = 'I LOVE YOU!!!'
n = 1
print(play_pass(s, n))
