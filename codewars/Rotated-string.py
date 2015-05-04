# -*- coding: utf-8 -*-

'''
Created on May , 2015
@author: stevey
'''
def is_rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    for idx, ele in enumerate(s1):
        if s1[idx:] + s1[:idx] == s2:
            return True
    return False


s1 = 'hello'
s2 = 'hello'
s1, s2 = '', ''
print(is_rotation(s1, s2))