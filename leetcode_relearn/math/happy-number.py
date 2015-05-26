# coding: utf-8


class Solution:

    def scy(self, number):
        return sum([int(i) ** 2 for i in str(number)])

    def isHappy(self, n):
        pool = []
        pool.append(n)
        while True:
            print n
            if self.scy(n) in pool:
                return False
            if self.scy(n) > 1 and self.scy(n) not in pool:
                n = self.scy(n)
                pool.append(n)
            if self.scy(n) == 1:
                return True


s = Solution()


# https://leetcode.com/problems/happy-number/

class Solution:

    def scy(self, number):
        return sum([int(i) ** 2 for i in str(number)])

    def isHappy(self, n):
        sum = 0
        while n > 0:
            num = n % 10
            n /=  10
            sum += num ** 2

        if sum == 1:
            return True
        elif sum//10 >0:
            return self.isHappy(sum//10)
        else:
            return False

print s.isHappy(19)


