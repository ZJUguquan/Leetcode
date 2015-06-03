class Solution:
    def isIsomorphic(self, s, t):
        # part1:substituting s with t
        d = {}
        for i in range(len(s)):
            d[s[i]] = t[i]
        tempS1 = list(s[:])
        tempT1 = list(t[:])
        for i in range(len(s)):
            tempS1[i] = d[tempS1[i]]
        if tempS1 != tempT1:
            return False

        # part2:substituting t with s
        d = {}
        for i in range(len(s)):
            d[t[i]] = s[i]
        tempT2 = list(t[:])
        tempS2 = list(s[:])
        for i in range(len(s)):
            tempT2[i] = d[tempT2[i]]
        if tempS2 != tempT2:
            return False

        return True
# https://leetcode.com/problems/isomorphic-strings/
from string import maketrans


def occurence(s, char):
    if char not in s:
        return False
    return [idx for idx, ch in enumerate(s) if ch == char]


class Solution:

    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if occurence(s, s[i]) != occurence(t, t[i]):
                return False
        return True

    # def isIsomorphic(self, s, t):
    #     if len(s) != len(t):
    #         return False
    #     lens = len(s)
    #     s_dict = ''
    #     t_dict = ''

    #     for idx, ele in enumerate(s):
    #         if ele not in s_dict:
    #             s_dict += ele
    #             t_dict += t[idx]
    #     translated = s.translate(maketrans(s_dict, t_dict))
    #     print translated, t
    #     if translated == t:
    #         return True
    #     return False

sp = Solution()
s = 'egg'
t = 'add'
s = 'ba'
t = 'ef'
print sp.isIsomorphic(s, t)
        # for i in range(lens):
        #     x_vecotr = [idx for idx, chr in enumerate(s) if chr == s[i]]
        #     y_vecotr = [idx for idx, chr in enumerate(t) if chr == t[i]]
        #     if x_vecotr != y_vecotr:
        #         return False
        # return True

        # sc = Counter(s)
        # tc = Counter(t)

        # if sorted(sc.values()) != sorted(tc.values()):
        #     return False
        #
