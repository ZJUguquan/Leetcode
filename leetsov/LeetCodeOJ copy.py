# -*- coding: utf-8 -*-

## Single Number

import string
import re
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