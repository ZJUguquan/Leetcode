
# https://leetcode.com/problems/isomorphic-strings/
from string import maketrans
class Solution:

    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        lens = len(s)
        s_dict = ''
        t_dict = ''

        for idx, ele in enumerate(s):
            if ele not in s_dict:
                s_dict += ele
                t_dict += t[idx]
        translated = s.translate(maketrans(s_dict, t_dict))
        print translated, t
        if translated == t:
            return True
        return False

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