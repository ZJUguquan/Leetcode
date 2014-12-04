#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'STEVE'

"""documents:
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false

"""

def isMatch(s, match):
	while '**' in match or '*?' in match or '*?' in match:
		match = match.replace('**', '*')
		match = match.replace('*?', '*')
		match = match.replace('?*', '*')

	if match == "" and s != "":
		return False
	if '?' not in match and '*' not in match:
		return s == match
	while match[0] != '?' and match[0] != '*':
		if s[0] != match[0]:
			return False
		else :
			return isMatch(s[1:], match[1:])
	if  match[0]  == '?' :
		return isMatch(s[1:], match[1:])
	if match[0] == '*' :
		if  len(match) == 1:
			return True
		else:
			to_find = s.lstrip('*?')[0]
			position = s.find(to_find)
			return isMatch(s[position:], match[1:])



str1 = "jinyong"
str2 = "*g"

# to_find = str2.lstrip('*?')[0]
# print to_find
# print str1[str1.find(to_find):]
# print str2.lstrip('*')
print isMatch(str1, str2)

# print str1.find('y')




'rewrite after discuss...'
'Status  Accept.'
'思路双指针 移动'

def comparison(str, pattern):
	s, p, match, starIdx = 0, 0, 0, -1
	while s < len(str):
		# both pointer move
		if p < len(pattern) and (pattern[p] == '?' or  str[s]== pattern[p]):
			s += 1
			p += 1   # get
		# found *, only  pattern pointer move
		elif p < len(pattern) and  pattern[p] == '*':
			starIdx  = p
			match = s
			p += 1

		# last pattern pointer was '*'
		elif starIdx != -1:
			p = starIdx + 1
			match += 1
			s = match
		else:
			return False

	while p < len(pattern) and pattern[p] == '*':
		p += 1

	return p == len(pattern)

print 'Com'
str1 = 'jy'
str2 = '*y'
print comparison(str1, str2)




'rewrite after discuss...'

