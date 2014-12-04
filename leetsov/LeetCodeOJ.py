# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# Question 5: 矩阵的上下翻转 或左右翻转
"http://ti.jisuanke.com/problem/5"

M, N = 4, 5
m = []
m.append([1, 2, 3, 4, 6])
m.append([5, 6, 7, 8, 8])
m.append([9, 0, 1, 2, 2])
m.append([3, 4, 5, 6, 10])


i = 2
#coding=utf-8
M, N, i = [int(x) for x in  raw_input().split()]
m = []
for x in range(M):
    m_row = raw_input().split()
    m.append(m_row)


if i == 1: # up and down
    for x in range(M-1, -1, -1):
        for y in range(0,N):
            print m[x][y],
        print "\n",
else:
    # left and righת
    for x in range(0,M):
        for y in range(0,N):
            print m[x][N-1-y],
        print "\n",
# Question 11: remove duplicates
"http://ti.jisuanke.com/problem/11"

# m = 5
# array_m = [0, 0, 1, 1, 2]
# set_m = set(array_m)
# print len(array_m)
# print len(set_m)

# m = raw_input()
# array_m = raw_input()
# b = array_m.split(" ")
# if len(b) <= 1:
#     print len(b)
# else:
#     i = 1
#     for x in range(1, len(b)):
#         if b[x] > b[x - 1]:
#             i += 1
#     print i

# "status:  未通过..."

## Single Number

import string
import re

def p(s):
    s = str(s)
    print(s)

p(123)

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for i in A:
            ans = ans ^ i
        return ans

""" Accept"""


def singleNumber(A):
    ans = 0
    for i in A:
        ans = ans ^ i
    return ans

A = [1,0,1,0,3]
print singleNumber(A)



## maxDepth of binary tree

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            l, r = 1, 1
            if root.left != None:
                l = l + self.maxDepth(root.left)
            if root.right != None:
                r = r + self.maxDepth(root.right)
       #


        if l > r:
            return l
        else:
            return r



# isSame Tree

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if (p == None or q ==None ) :
            return p == q
        else:
            return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


"""
Example1: x = 123, return 321
Example2: x = -123, return -321

"""

class Solution:
    # @return an integer
    def reverse(self, x):
        def print_reverse(input):
            trans_list = list(str(input))
            if "-" in trans_list:
                trans_list.remove("-")
            trans_list.reverse()
            for i in range(len(trans_list) ):
                if trans_list[i] == '0':
                    continue
                else:
                    break

            return "".join(trans_list[i:])

        if x > 0:
            return int(print_reverse(x))
        elif x == 0 :
            return 0
        else:
            return  int("-" + print_reverse(x * -1))




senword = "A man, a plan, a canal: Panama"
senword = "1a2"

class Solution:

    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        ans = ""
        for x in s:
            if  (ord(x) >= 65 and ord(x) <= 92 ) or (ord(x) >= 97 and ord(x) <=122)  or(ord(x)>=48 and ord(x) <= 57):
                ans += x
        new_word = ans.lower()

        if len(new_word) <= 1:
            return True
        else:

            for x in range(0, (len(new_word)+1 ) /2 ):
                if new_word[x] != new_word[len(new_word) -1 - x ]:
                    return False

                if x == len(new_word)/2 - 1:
                    return True



"Path sum"


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def hasPathSum(self, root, sum):
    if root:
        return not root.left and not root.right and sum==root.val or self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
    return False


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None: #or root.val < sum
            return False
        if root.left ==None and root.right ==None and root.val == sum :
            return True
        if root.left != None:
            if self.hasPathSum(root.left, sum - root.val) == True:
                return True
        if root.right != None:
            if self.hasPathSum(root.right, sum - root.val) == True:
                return True
        return False


"Valid Number"

def isNumber(s):
    try:
        float(s)
        print "True"
    except:
        print "False"

isNumber("2E10")
isNumber("210")
isNumber("0X10")

a = '11'
b = '1'
c = long(a, base = 2) + long(b, base =2)
print c
d = str(bin(c))
print d[2:]


"Add Binary"
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        c = long(a, base = 2) + long(b, base = 2)
        d = str(bin(c))
        return d[2:]


# "Pascal's Triangle"
# N = 5
# m = list(" " * N )
# m[0] = [1]
# m[1] = [1,1]
# m[2] = [1,2,1]
# n = 3
# while (n < N):
#     m[n] = [1,1]
#     for i in range(1, len(m[n-1])):
#         m[n].insert(i, m[n-1][i-1] + m[n-1][i] )

#     print m[n]
#     n += 1

def generate(numRows):

        if numRows == 0 :
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        elif numRows == 3:
            return [[1], [1,1], [1,2,1]]
        else:
            m = list(" " * numRows )
            m[0] = [1]
            m[1] = [1,1]
            m[2] = [1,2,1]
            n = 3
            while (n < numRows):
                m[n] = [1,1]
                for i in range(1, len(m[n-1])):
                    m[n].insert(i, m[n-1][i-1] + m[n-1][i] )
                n += 1
            return m
print generate(4)


"Accept"
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):

        if numRows == 0 :
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        elif numRows == 3:
            return [[1],[1,1], [1,2,1]]
        else:
            m = list(" " * numRows )
            m[0] = [1]
            m[1] = [1,1]
            m[2] = [1,2,1]
            n = 3
            while (n < numRows):
                m[n] = [1,1]
                for i in range(1, len(m[n-1])):
                    m[n].insert(i, m[n-1][i-1] + m[n-1][i] )

                #print m[n]
                n += 1
            return m


def factorial(n):
    if n==1:
        return 1
    else:
        return reduce(lambda x, y: x*y, range(1, n+1))
print factorial(10)
numbers = 30
#result = map(lambda i: map(labmda x: factorial), sequence)
# use formula.



def generate_2(rowIndex):
        if rowIndex == 0 :
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex == 2:
            return [1,2,1]
        elif rowIndex == 3:
            return [1,3,3,1]
        else:
            m = list(" " * rowIndex )
            m[0] = [1,1]
            m[1] = [1,2,1]
            m[2] = [1,3,3,1]
            n = 3
            while (n < rowIndex):
                m[n] = [1,1]
                for i in range(1, len(m[n-1])):
                    m[n].insert(i, m[n-1][i-1] + m[n-1][i] )

                #print m[n]
                n += 1
            return m.pop()

print generate_2(5)




"Minimum Depth of Binary Tree"

print min(3,2)


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right ==None :
            return 1
        if root.left != None and root.right ==None:
            return 1 + self.minDepth(root.left)
        if (root.left == None and root.right != None ) :
            return 1 + self.minDepth(root.right)
        l, r = 0, 0
        if root.left != None:
            l = 1 + self.minDepth(root.left)
        if root.right != None:
            r = 1 + self.minDepth(root.right)
        return min(l, r)

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        ans = ""
        for x in digits:
            ans += str(x)
        raw_number = int(ans)
        plus_one = raw_number + 1
        return map(int, list(str(plus_one)) )
#print plusOne([1,9,9])

print "333"
print range(5,-1, -1)


"Merge Sorted Array"

# class Solution:
#     # @param A  a list of integers
#     # @param m  an integer, length of A
#     # @param B  a list of integers
#     # @param n  an integer, length of B
#     # @return nothing
#     def merge(self, A, m, B, n):

#         i = m-1
#         j = n-1
#         for k in range(m+n+1,-1, -1) {
#             if (i < 0) :
#                 A[k] = B[j]
#                 j = j - 1
#             elif (j < 0):
#                 A[k] = A[i]
#                 i = i - 1
#             elif (A[i] < B[j]) :
#                 A[k] = B[j]
#                 j = j - 1
#             else:
#                 A[k] = A[i]
#                 i = i - 1

#     }
# "Not passed"


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(12)
head2 = ListNode(13)

head3 = ListNode(9)
head4 = ListNode(4)
head.next = head2
head2.next = head4
head4.next = head3

def sortList(head):
    res=[ ];
    while(head):
        res.append(head.val);
        head=head.next;
    res=sorted(res);
    ## res sorted value - list

    head=ListNode(0);
    resHead=head;
    for v in res:
        resHead.next=ListNode(v);
        resHead=resHead.next;
    return head.next

print sortList(head).val


s = "leetcode"
dict1 = ["leet", "code"]

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        cache = {"" :True}
        def parser(remain):
            if remain in cache:
                return cache[remain]
            for i in range(len(remain)):
                if (remain[:i+1] in dict and parser(remain[i+1:])):
                    cache[remain] = True
                    return True
            cache[remain] = False
            return False
        return parser(s)


"leetcode _ balanced binary tree "

class Solution:
    # @param root, a tree node
    # @return a boolean

    def isBalanced(self, root):
        return self.getHeight(root) is not None

    def getHeight(self, root):
        if not root:
            return 0
        lh = self.getHeight(root.left)
        if lh is None:
            return None
        rh = self.getHeight(root.right)
        if rh is None:
            return None
        if abs(lh-rh) > 1:
            return None
        else:
            return max(lh,rh)+1

"检测是否为对称树"

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None :
            return True
        r1 = root
        r2 = root
        return self.check(r1, r2)

    def check(self,root1, root2):
        if root1 == None and root2 != None:
            return False
        if root2 == None and root1 != None:
            return False
        if root1 == None and root2 == None:
            return True
        if root1.val != root2.val:
            return False
        else:
            return self.check(root1.left, root2.right) and self.check(root1.right, root2.left)




# "最长字符列表 前缀"

# # -*- coding: utf-8 -*-

# __author__ = 'STEVE'


# def longestCommonPrefix(strs):
#     from collections import OrderedDict
#         if len(strs) == 0 :
#             return ""
#         if len(strs) == 1:
#             return strs[0]
#         dd = sorted(strs, key= len, reverse = False)
#         beging = dd[0]
#         i = len(beging)
#         while i >= 1:
#             prefix = beging[:i]
#             if any( prefix not in x[:i] for x in strs):
#                 i -= 1
#                 continue
#             return beging[:i]
#         return ""


# strs = ["abcd", "abc", "abzzzzz"]
# strs = ["c", "ccc", "acc", "b"]
# print "c"[0:0]

# #print "ba"[0:2]
# print longestCommonPrefix(strs)
# # print "abc" in "abczz"



# # 学习如何用sorted 给字符列表  按照长度排序
# # 新建变量存储
# # d= sorted(old_list ,key = len)


# "Pow(x, n)"
# "Implement pow(x, n)."
# class Solution:
#     # @param x, a float
#     # @param n, a integer
#     # @return a float
#     def pow(self, x, n):
#         return float(x**n)


"10-29 code 300lines"

"Generate Paranthesses"

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

# def generateParenthesis(n):
#     if n == 1:
#         return ["()"]
#     left, right = 0, 0
#     while n >= 2:


# origin = (0, 0)
# left, right = origin
# left += 1
# right +=1
# print left,right, origin
class Solution:
    ans = []
    def dp(self, outstack, instack, res):
        if outstack == 0 and instack ==0:
            self.ans.append(res)
        if outstack > 0:
            self.dp(outstack -1, instack +1, res + "(" )
        if instack > 0:
            self.dp(outstack , instack -1, res + ")")
        return

s = Solution()
s.dp(2, 0, "")
#print s.ans


"Accepted "

class Solution:
    # @param an integer
    # @return a list of string
    ans = []
    def generateParenthesis(self, n):
        self.dp(n, 0, "")
        final = []
        for x in self.ans:
            if len(x) == n * 2:
                final.append(x)
        return final

    def dp(self, outstack, instack, res):
        if outstack == 0 and instack == 0:
            self.ans.append(res)
        if outstack > 0:
            self.dp(outstack -1, instack +1, res + "(" )
        if instack > 0:
            self.dp(outstack , instack -1, res + ")")
        return

s = Solution()
print s.generateParenthesis(4)


"Length of Lastword"
"Accepted"
def lst(s):
    if len(s) == 0:
        return 0
    l = len(s)
    count = 0

    for i in range(l - 1, -1, -1):
        if s[i] != " ":
            count += 1
        if s[i] == " " and count != 0 :
            return count
    return count

print lst('hello world')


"***********************************************************"

"Valid Parentheses"
"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not."
"""

def isValid(s):
    if s == "":
        return True
    if len(s) % 2 == 1:
        return False
    else:
        if "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
            return isValid(s)

print isValid("(())[{}]()")

"Accepted , do my ownn"
class Solution:
    # @return a boolean
    def isValid(self, s):
            if s == "":
                return True
            if len(s) % 2 == 1:
                return False

            else:
                while(  "()" in s or "[]" in s or "{}" in s):
                    s = s.replace("()", "")
                    s = s.replace("[]", "")
                    s = s.replace("{}", "")
                    return self.isValid(s)
                return False


"参考方法"
"""
class Solution:
    # @return a boolean
    def isValid(self, s):
        mappings = {')': '(', ']': '[', '}': '{'}
        stack = []

        for par in s:
            if par in mappings.values():
                stack.append(par)
            elif stack and stack[-1] == mappings[par]:
                stack.pop()
            else:
                return False

        # note: remember to check if stack is empty
        return False if stack else True
"""

"LRU Cache"
"last problem in leetcode in yixin"

"""
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):


    # @return an integer
    def get(self, key):


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):

"""

"Climbing stairs"
"Accept fibonacci series"
def climbStairs(n):
        first   = 0
        second  = 1
        for i in range(n):
            first, second = second, second + first

        return second

print climbStairs(10)

"Maximum Subarray"
a = [-2, -3, 4, -1,2,1,-5, 7]
"Status: Accepted!! "
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
            max = A[0]
            i = 1
            while i < len(A):
                if A[i-1] >= 0 :
                    A[i] += A[i-1]
                if max < A[i]:
                    max = A[i]
                i += 1
            return max
"List index"
# print len(a)
# print a.index(7)
# print sum(A)
# print maxSubArray(a)


"ZigZag Convert"

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
"given int row = 3"

s = "PAYPALISHIRING"
s_list = list(s)[::-1]
print s_list
#print s_list.pop()
#print s_list.pop()

m = []
n = 3
pos = 0
for i in range(0,n):
    m.append([])
remain = len(s)

while remain >= 3 :
    #print remain
    for i in range(0,n) :
        if s_list != []:
            m[i].append( s_list.pop())
    pos += n
    if pos % (n+1) == n and ( len(s_list) > 0):
        m[1].append(s_list.pop())
        pos += 1
    remain -= n

# print m[0]
# print m[1]
# print m[2]
print ''.join(m[0]) +''.join(m[1]) + ''.join(m[2])
def zigzag(s, n):
    if len(s) <= n:
        return s
    m = []
    pos = 0
    for i in range(0, n):
        m.append([])
    remain = len(s)
    s_list = list(s)[::-1]
    while remain >= n :
        #print remain
        for i in range(0,n) :
            if s_list != []:
                m[i].append( s_list.pop())
        pos += n
        if pos % (n+1) == n and ( len(s_list) > 0):
            m[(n - 1)/2 ].append(s_list.pop())
            pos += 1
        remain -= n
    result = ''
    for i in range(0,n):
        result += ''.join(m[i])
    return result
s = "ABC"
print zigzag(s, 2)

# print m[0]
# print m[1]
# print m[2]
#print ''.join(m[0]) +''.join(m[1]) + ''.join(m[2])

"对zigzag 排列方式不清楚  做错."
"关于排列方式 可以参考引内容: https://oj.leetcode.com/discuss/1212/expected-output-of-abcde-4"

"参考别人"
lis = range(0,10)
print lis[-2:0:-1]

def convert(text, nRows):
    def back_and_forth(interval, repeat=1):
        new_interval = interval + interval[-2:0:-1]
        for _ in range(repeat):
            for i in new_interval:
                yield i

    if nRows == 1:
        return text
    period = 2*(nRows-1)
    n_periods = len(text) / period + 1
    zigzag = back_and_forth(range(nRows), repeat=n_periods)
    # "Rememthis code !!!!"
    results = [ [] for _ in range(nRows)]
    for c, row in zip(text, zigzag):
        results[row].append(c)
    return ''.join(''.join(row) for row in results)

print convert("PAYPALISHIRING",3)

print '*' * 79

"GrayCode"

def grayCode(n):
    if n == 0 :
        return [0]
    result = [0, 1]
    for i in xrange(1,n):
        result += [(x + 2 **i) for x in reversed(result)]
    return result

print grayCode(3)

"wiki pedia: http://en.wikipedia.org/wiki/Gray_code#ConvertingtoandfromGraycode"

# 复用wiki百科页 写一个自己的方法


res = [0,1]
n = 1
n = 2
# reversed[res]
entry1 = res
entry2 = [ x + 2 ** (n-1) for x in reversed(res)]
print entry2
res =  entry1 + entry2

n = 3
entry1 = res  + [ x + 2**(n-1) for x in reversed(res)]
print entry1


"Single Number II"
"Given an array of integers, every element appears three times except for one."
"Find that single one."
"Note:"
"Your algorithm should have a linear runtime complexity. "
#Could you implement it without using extra memory?"

p('*'*200)

print 3 ^ 4
print 3 & 4
p('*'*200)

def getSingle(A):
    if len(A) == 0 :
        return None
    if len(A) < 2:
        return A[0]

"""
def singleNumber(self,A):
    n = len(A)
    if n==0:
        return A[0]
    else:
        result = 0
        for j in range(32):
            mask = 1 << j
            sum = 0
            for i in range(n):
                if (A[i] >> j) & 1:
                    # bb = aa >> j
                    sum = sum + 1
            output = sum%3
            result = (output << j) | result
        return result
"""

"reference"
""" too hard
public int singleNumber(int[] A) {
    int ones = 0, twos = 0;
    for(int i = 0; i < A.length; i++){
        ones = (ones ^ A[i]) & ~twos;
        twos = (twos ^ A[i]) & ~ones;
    }
    return one
}
"""

"""

The code makes use of 2 variables.

ones - At any point of time, this variable holds XOR of all the elements which have appeared "only" once.
twos - At any point of time, this variable holds XOR of all the elements which have appeared "only" twice.
So if at any point time,
    A new number appears - It gets XOR'd to the variable "ones".
    A number gets repeated(appears twice) - It is removed from "ones" and XOR'd to the variable "twos".
    A number appears for the third time - It gets removed from both "ones" and "twos".
    The final answer we want is the value present in "ones" - coz, it holds the unique element.

So if we explain how steps 1 to 3 happens in the code, we are done.
Before explaining above 3 steps, lets look at last three lines of the code,

    commonbitmask = ~(ones & twos)
    ones & = commonbitmask
    twos & = commonbitmask

All it does is, common 1's between "ones" and "twos" are converted to zero.
For simplicity, in all the below explanations - consider we have got only 4 elements in the array (one unique element and 3 repeated elements - in any order).

Explanation for step 1

    Lets say a new element(x) appears.

CURRENT SITUATION - Both variables - "ones" and "twos" has not recorded "x".

    Observe the statement "twos| = ones & x". Since bit representation of "x" is not present in "ones", AND condition yields nothing. So "twos" does not get bit representation of "x". But, in next step "ones ^= x" - "ones" ends up adding bits of "x". Thus new element gets recorded in "ones" but not in "twos".

The last 3 lines of code as explained already, converts common 1's b/w "ones" and "twos" to zeros. Since as of now, only "ones" has "x" and not "twos" - last 3 lines does nothing.

Explanation for step 2.

Lets say an element(x) appears twice.

CURRENT SITUATION - "ones" has recorded "x" but not "twos".

Now due to the statement, "twos| = ones & x" - "twos" ends up getting bits of x. But due to the statement, "ones ^ = x" - "ones" removes "x" from its binary representation.

Again, last 3 lines of code does nothing. So ultimately, "twos" ends up getting bits of "x" and "ones" ends up losing bits of "x".

Explanation for step 3.

Lets say an element(x) appears for the third time.

CURRENT SITUATION - "ones" does not have bit representation of "x" but "twos" has.

Though "ones & x" does not yield nothing .. "twos" by itself has bit representation of "x". So after this statement, "two" has bit representation of "x". Due to "ones^=x", after this step, "one" also ends up getting bit representation of "x".

Now last 3 lines of code removes common 1's of "ones" and "twos" - which is the bit representation of "x". Thus both "ones" and "twos" ends up losing bit representation of "x".

 class Solution {
    public:
    // Let us take the example of {3, 3, 2, 3} to understand this
        int singleNumber(int A[], int n) {
            int ones=0, twos =0;
            int common_bit_mask;
            for(int i=0; i<n;i++)
            {
                 /* The expression "one & arr[i]" gives the bits that are
               there in both 'ones' and new element from arr[].  We
               add these bits to 'twos' using bitwise OR

               Value of 'twos' will be set as 0, 3, 3 and 1 after 1st,
               2nd, 3rd and 4th iterations respectively */

                twos= twos|(ones&A[i]);
                /* XOR the new bits with previous 'ones' to get all bits
               appearing odd number of times

               Value of 'ones' will be set as 3, 0, 2 and 3 after 1st,
               2nd, 3rd and 4th iterations respectively */
                ones=ones^A[i];
                 /* The common bits are those bits which appear third time
               So these bits should not be there in both 'ones' and 'twos'.
               common_bit_mask contains all these bits as 0, so that the bits can
               be removed from 'ones' and 'twos'

               Value of 'common_bit_mask' will be set as 00, 00, 01 and 10
               after 1st, 2nd, 3rd and 4th iterations respectively */
                common_bit_mask= ~(ones&twos);
                /* Remove common bits (the bits that appear third time) from 'ones'

               Value of 'ones' will be set as 3, 0, 0 and 2 after 1st,
               2nd, 3rd and 4th iterations respectively */
                ones &=common_bit_mask;
                /* Remove common bits (the bits that appear third time) from 'twos'

               Value of 'twos' will be set as 0, 3, 1 and 0 after 1st,
               2nd, 3rd and 4th itearations respectively */
                twos &=common_bit_mask;
            }
            return ones;
        }
    };

"""



#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"
__project__ = ""

s = "the     sky is blue"
import re
if s.strip() == "":
    print ""
# arr = s.split(" ")
arr = re.split(r'\s+', s)
print  " ".join(arr[::-1])


" 正则可以"

" 不用正则"

arr = [1,2,3,"", ""]
while "" in arr:
    arr.remove("")
print arr


"Accept"
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip()# == "":
        if " " not in s:
            return s
        arr = s.split()
        while "" in arr:
            arr.remove("")
        return  " ".join(arr[::-1])



"Implement strSTr()"

"remove element"

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        read,write=0,0
        while read<len(A):
        if A[read]!=elem:
            A[write]=A[read]
            write+=1
            read+=1
        return write


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        # if len(A) <= 0:
        #     return 0
        read, write=0,0
        while read < len(A):
            if A[read]!=elem:
                A[write]=A[read]
                write+=1
            read+=1
        return write

# [1,3,4,3,4,5]  , 4  A[0] = 1

# A[1]
# step 3  read = 2 write = 2
#  read = 3 write = 2
# A[2] = A[3]   write = 3  read = 4
