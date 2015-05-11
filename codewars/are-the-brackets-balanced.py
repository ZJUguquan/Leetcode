# -*- coding: utf-8 -*-
'''
Created on May , 2015
@author: stevey
'''

import numpy as np
np.random.seed(1428)
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import os, sys
from sklearn import datasets
style.use('ggplot')


def isBalanced(str):
    _stack = []
    for w in str:
        if w == ')':
            if len(_stack)>0 and _stack[-1] == '(':
                _stack.append(w)
        if (len(_stack) < 1 or _stack[-1] == ')' ) and w=='(':
            _stack.append(w)
    return len(_stack) > 0 and len(_stack) % 2 == 0

print isBalanced("hi)(")
print isBalanced("hi(hi)")
print isBalanced("(")
