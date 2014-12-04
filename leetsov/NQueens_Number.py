import itertools


class Solution:
    # @return an integer

    def totalNQueens(self, n):
        solutions = []
        for solution in itertools.permutations(range(n)):
            if len(set(x - y for x, y in enumerate(solution))) == \
               len(set(x + y for x, y in enumerate(solution))) == n:
                solutions.append(solution)
        return len(solutions)
s = Solution()
print(s.totalNQueens(5))



"Accepted Others"
class Solution:
    ans, limit = 0, 0
    # @return an integer
    def totalNQueens(self, n):
        self.ans = 0
        self.limit = (1<<n) - 1
        self.dfs(0, 0, 0)
        return self.ans

    def dfs(self, h, r, l):
        if h == self.limit:
            self.ans += 1
            return
        pos = self.limit & (~(h|r|l))
        while pos:
            p = pos & (-pos)    #return most right bit 1
            pos -= p
            self.dfs(h+p, (r+p)<<1, (l+p)>>1)   #no shift needed for h, left shift for anti diagonal

s = Solution()
print(s.totalNQueens(10))

