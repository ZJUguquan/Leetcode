# -*- coding: utf-8 -*-


import math

def decompose_aux(nb, rac):
    if (nb == 0):
        return []
    i = rac
    l = None
    while (i >= int(math.sqrt(nb / 2.0)) + 1):
        diff = nb - i * i
        rac = int(math.sqrt(diff))
        l = decompose_aux(diff, rac);
        if l != None:
            l.append(i)
            return l
        i -= 1
    return l

def decompose(n):
    l = decompose_aux(n * n, int(math.sqrt(n * n - 1)))
    if l != None:
        return l
    else:
        return None



from math import sqrt

def doDecompose(n2, prev = None):
    for i in xrange(int(sqrt(n2)) - (0 if prev else 1), 0, -1):
        if not prev or i < prev:
            d = n2 - i ** 2
            if d:
                next = doDecompose(d, i)
                if next:
                    return next + [i, ]
            else:
                return [i, ]
    return None

def decompose(n):
    return doDecompose(n ** 2)


print(decompose(16))


















def oye():
    print('o'*79)









from math import sqrt, ceil

def doDecompose():
    if int(sqrt(n2)) == ceil


oye()

def sqInRect(lng, wdth):
    if lng == wdth:
        return None
