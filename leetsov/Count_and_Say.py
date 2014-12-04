
__author__ = 'STEVE'
__tag__ = "LeetCode"



"""
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

def Say(i):
	m = range(0,10)
	print m


a = 1112223

a_to_s = str(a)




"Count and Say"


def count(s):
    if len(s)< 1: return ""
    number = s[0]
    length = len(s)
    return str(length) + str(number)
print count('11111')

print count('')

s = "1"

# s = n
start = s[0]
snippet = s[0]
ans = ""
for i in range(1, len(s)):
    if s[i] == start :
        snippet += s[i]
        start = s[i]
    else:
        ans += count(snippet)
        snippet = s[i]
        start = s[i]
    if i == len(s) -1 :
        ans += count(snippet)


print ans



"Reference "

class Solution:
    # @return a string
    # memoization
    ret = {1:"1"}
    def countAndSay(self, n):
        if n==1:
            return self.ret[1]
        elif n in self.ret:
            return self.ret[n]
        else: # ret[n] doesn't exist
            self.ret[n] = self.proceed(self.countAndSay(n-1),1)
            return self.ret[n]

    def proceed(self,s,index): # return the next string based on string s
        if len(s)==1:
            return str(index)+s[0]
        elif s[0]==s[1]:
            return self.proceed(s[1:],index+1)
        else: # s[0]!=s[1]
            return str(index)+s[0]+self.proceed(s[1:],1)