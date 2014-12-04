#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'STEVE'

"""documents:

Understanding the definiation of  Binary Search Tree
"""

class Solution:
    # @return an integer
    def numTrees(self, n):
        if n <= 1:
            return 1
        if n == 2:
            return 2
        s = 0
        for i in range(n):
            s += self.numTrees(i)*self.numTrees(n-1-i)
        return s