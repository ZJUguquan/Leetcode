# coding: utf-8


import sys
reload(sys)
from pandas import DataFrame
sys.setdefaultencoding("utf-8")
from pprint import pprint

# http://www.codewars.com/kata/53cf7e37e9876c35a60002c9/train/python

# currying vs. Partial Application

from functools import reduce
m = lambda x, y: f(x, y)

def curryPartial(f,*initial_args):
    return reduce(m, initial_args)

def add(x,y,z):
  return x + y + z

  print curryPartial(add, (1,2,3))