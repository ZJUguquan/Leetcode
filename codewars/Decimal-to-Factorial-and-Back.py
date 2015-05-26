# coding: utf-8
from math import factorial
# 2  http://www.codewars.com/kata/decimal-to-factorial-and-back

def maxiFact(nb):
    if nb == 1: return 1
    i = 1
    while nb > factorial(i):
        i += 1
    return i - 1 if factorial(i) > nb else i

from string import ascii_uppercase, digits
posix = digits + ascii_uppercase

def dec2FactString(nb):

    out = ['0'] + ['0'] * 35
    maxi = maxiFact(nb)
    # print maxiFact(nb)
    while nb > 0:
        qutient, nb = divmod(nb, factorial(maxi))
        out[maxi] = str(posix[qutient])
        maxi = maxiFact(nb)
    # print out
    return ''.join(out).rstrip('0')[::-1]

# print dec2FactString(463)


def factString2Dec(string):
    return sum([posix.index(s) * factorial(idx) for idx, s in enumerate(string[::-1])])

