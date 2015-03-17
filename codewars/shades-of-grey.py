# -*- coding: utf-8 -*-
'''
Created on Feb , 2015

@author: stevey
'''

def shades_of_grey(n):
    if n < 0:
        return []
    result = []
    for i in range(1, min(n, 254)+1):
        s = hex(i)[2:].zfill(2)
        result.append('#'+s*3)
    return result


print(shades_of_grey(1))