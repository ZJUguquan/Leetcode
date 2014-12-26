# -*- coding: utf-8 -*-
"""
code log of stevey(raw: staticor)
from date(2014-10-28), begin to code_plan
makeprogramming_code at leat 1000 lines everyday.
"""
__author__ = "Stevey"
__project__ = "LeetCode"

__tags__ = "math"
url = "https://oj.leetcode.com/tag/math/"

"Roman to Integer"
"""qustion:
Given a roman numeral, convert it do an integer.
Input is guaranteed to be within the range from 1 to 3999
"""
'------'
"Accepted others"


def romanToInt(s):
    m = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    s = s.upper()
    stack = [0]
    # reversed
    for c in s[::-1]:
        if m[c] >= stack[-1]:
            stack.append(m[c])
        else:
            v = stack.pop()
            stack.append(v - m[c])
    return sum(stack)

s = "MMMCMXCIX"  # X I C
s = "MMCCCLI"
print romanToInt(s)

"Integer to Roman"
"Input is guaranteed to be within the range from 1 to 3999."
m = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
m = dict((v, k) for k, v in m.iteritems())
"## 小技巧 实现 字典中 k-v 对值的互换  反转  v k k v in iteritems()"

# for k in m:
#     print k , m[k]
#
m = {3900: "MMMCM",
     3000: "MMM",
     1000: "M",
     900: "CM",
     500: "D",
     400: "CD",
     100: "C",
     90: "XC",
     50: "L",
     40: "XL",
     10: "IX",
     9: "IX",
     5: "V",
     4: "IX",
     1: "I"}
# dict 按keys排序 输出
# for i in sorted(m.keys(), reverse=True):
#     print i
# 迭代方法 最终屡次出现 TLE  Time Limit Exceeding 不得不放弃


def intToRoman(num):
    m = {1000: "M",
         900: "CM",
         500: "D",
         400: "CD",
         100: "C",
         90: "XC",
         50: "L",
         40: "XL",
         10: "X",
         9: "IX",
         5: "V",
         4: "IX",
         1: "I"}
    for i in sorted(m.keys(), reverse=True):
        if num >= i:
            return m[i] + intToRoman(num - i)
    return ""


# print "Int to Roman Test"
# print intToRoman(3999)

"参考2"
"statis Accepted"


def intToRoman(num):
    roman = "IVXLCDM"
    result = ""
    divide = 1000
    for i in [6, 4, 2, 0]:
        temp = num / divide
        if (temp == 0):  # hundreds of , num < 1000
            divide /= 10
            continue
        if (temp <= 3):
            result += roman[i] * temp
        elif (temp == 4):
            result += roman[i]
            result += roman[i + 1]
        elif (temp == 5):
            result += roman[i + 1]
        elif (temp <= 8):
            result += roman[i + 1]
            result += roman[i] * (temp - 5)
        else:  # (temp == 9):
            result += roman[i]
            result += roman[i + 2]
        num %= divide
        divide /= 10
    return result
print intToRoman(3999)
"""
public String intToRoman(int num) {
        String roman = "IVXLCDM";
        StringBuilder result = new StringBuilder("");
        int divide = 1000;
        for (int i = 6; i >= 0; i-=2) {
            int temp = num / divide;
            if (temp == 0) {
                divide /= 10;
                continue;
            }
            if (temp <= 3) {
                result.append(createChars(roman.charAt(i),temp));
            }
            else if (temp == 4) {
                result.append(roman.charAt(i));
                result.append(roman.charAt(i+1));
            }
            else if (temp == 5) {
                result.append(roman.charAt(i+1));
            }
            else if (temp <= 8) {
                result.append(roman.charAt(i+1));
                result.append(createChars(roman.charAt(i),temp-5));
            }
            else {
                result.append(roman.charAt(i));
                result.append(roman.charAt(i+2));
            }
            num %= divide;
            divide /= 10;
        }
        return result.toString();
    }

    private String createChars(char c, int temp) {
        String result = "";
        for (int i = 0; i < temp; i++)
            result += c;
        return result;
    }
}
"""

"Palindrome Number"
"status: Accepted"
'需要注意一开始没有想到 如 11 22 33 这种长度为2的情况. 出现了 int('') 的错误'
'错误内容为 ValueError: invalid literal for int() with base 10:'


def isPalindrome(x):
    if x < 0:
        return False
    if x < 10:
        return True
    s = str(x)

    def head_and_tail(s):
        if len(s) == 2:
            if s[0] == s[-1]:
                return True
            else:
                return False
        if len(s) <= 1:
            return True
        for i in range(0, len(s) / 2):
            if s[0] != s[len(s) - 1 - i]:
                return False
            else:
                return head_and_tail(s[1:-1])

    return head_and_tail(s)

s = "100021"
print isPalindrome(int(s))
# print int('')

"Permutation Sequence"
"[1,2,3,4....,n] for any given k "
"output A_n_k(aka,  choose(n,k)*k! kinds of permutation sequence)"


def getPermutation(n, k):
    i, j, f = 1, 1, 1
    s = []
    for i in (1, n + 1):
        f *= i
        s.append(str(i))
    s = ''.join(s)
    # for i in range(n):

    # 12345 n = 5 first unit can bear 4! 24

# "test code"
# t = [1, 2 , 3, 4, 5]
# res = []
# n = 5 ; s = ""  ; f = 1 ; print s

# print "before", s
# for i in (1, 5):
#     s[i]  += str(i)
# print "after", s


"reference_code"
"""
string getPermutation(int n, int k) {
    int i,j,f=1;
    // left part of s is partially formed permutation, right part is the leftover chars.
    string s(n,'0');
    for(i=1;i<=n;i++){
        f*=i;
        s[i-1]+=i; // make s become 1234...n
    }
    for(i=0,k--;i<n;i++){
        f/=n-i;
        j=i+k/f; // calculate index of char to put at s[i]
        char c=s[j];
        // remove c by shifting to cover up (adjust the right part).
        for(;j>i;j--)
            s[j]=s[j-1];
        k%=f;
        s[i]=c;
    }
    return s;
}
"""
