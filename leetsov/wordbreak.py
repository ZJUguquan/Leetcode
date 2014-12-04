# -*- coding: utf-8 -*-

__author__ = 'STEVE'
__tag__ = "LeetCode"
__status__ == "Not Accepted in wordbreak II"



"Word Break II "
s = "catsanddog"
dict_s = ["cat", "cats", "and", "sand", "dog"]

def wordBreak(s, dict):
	cache = {"":True}
	def parser(s):
		for x in range(0, len(s) -  1):
			if s[:i+1] in dict and parse(s[i+1:]):
				cache[s] = True
				return True
		cache[s] = False
		return False

print wordBreak(s, dict_s)

1231
1231
12313
12312
