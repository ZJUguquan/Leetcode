# coding=utf-8
class Solution:

    def cmp(self, x, y):
        if x * (10 ** len(str(y))) + y < y * (10 ** len(str(x))) + x:
            return 1
        elif x * (10 ** len(str(y))) + y == y * (10 ** len(str(x))) + x:
            return 0
        else:
            return -1
    # @param num, a list of integers
    # @return a string

    def largestNumber(self, num):
        num.sort(self.cmp)
        return str(int(''.join(map(lambda x: str(x), num))))
