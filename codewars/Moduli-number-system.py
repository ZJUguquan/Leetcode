# coding: utf-8


#1 http://www.codewars.com/kata/moduli-number-system

from operator import mul
from itertools import combinations
from fractions import gcd

def fromNb2Str(n, modsys):
    prod = reduce(mul, modsys)
    if prod < n: return  "Not applicable"
    for x, y in combinations(modsys, 2):
        if gcd(x, y) > 1: return  "Not applicable"

    out = []
    for each in modsys:
        out.append( str(n % each))
    return '-' + '--'.join(out) + '-'


print fromNb2Str(25, [2,3,4])
print fromNb2Str(187, [8,7,5,3])
