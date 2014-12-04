#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"
__project__ = ""

"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""
# 最终找到了相同思路 但是算法非常简洁的代码.
#
# 学习了函数 divmod, 取两个整数除法运算的商 余数结果.
# 省得两行 / % 分别取.
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        array = range(1, n + 1)
        k = (k % math.factorial(n)) - 1
        permutation = []
        for i in xrange(n - 1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            permutation.append(array.pop(idx))

        return "".join(map(str, permutation))

n = 4
if n == 1:
    print 1
n = 4
k = 10
result = []

def factorial(n):
    return reduce(lambda x,y: x* y , range(1, n+1))

# print factorial(4)


f = k / factorial(n- 1 )
print f
result.append(f+1)

q = k % factorial(n-1)
print q


'divmod'

q, p = divmod(10, 3)
print q,p