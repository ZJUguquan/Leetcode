# -*- coding: utf-8 -*-

__author__ = 'STEVE'
__tag__ = "LeetCode"
__status__ == "Accepted"


def longestCommonPrefix(strs):
	from collections import OrderedDict
        if len(strs) == 0 :
            return ""
        if len(strs) == 1:
            return strs[0]
        dd = sorted(strs, key= len, reverse = False)
        beging = dd[0]
        i = len(beging)
        while i >= 1:
            prefix = beging[:i]
            if any( prefix not in x[:i] for x in strs):
                i -= 1
                continue
            return beging[:i]
        return ""


strs = ["abcd", "abc", "abzzzzz"]
strs = ["c", "ccc", "acc", "b"]
print "c"[0:0]

#print "ba"[0:2]
print longestCommonPrefix(strs)
# print "abc" in "abczz"
