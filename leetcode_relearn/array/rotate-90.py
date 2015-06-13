




'''


Input:  [[1,2],[3,4]]
Output: [[1,2],[3,4]]
Expected:   [[3,1],[4,2]]


'''

from math import floor, ceil
# first rotate clockwise? reverse
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, a):
        #a = zip(*a[::-1])

        n = len(a)
        f = int(floor(n/2.0))
        c = int(ceil(n/2.0))

        for x in range(f):
            for y in range(c):
                temp = a[x][y]
                a[x][y] = a[y][n-1-x]
                a[y][n-1-x] = a[n-1-x][n-1-y]
                a[n-1-x][n-1-y] = a[n-1-y][x]
                a[n-1-y][x] = temp



from math import floor, ceil

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, a):
        #a = zip(*a[::-1])

        n = len(a)
        f = int(floor(n/2.0))
        c = int(ceil(n/2.0))

        for x in range(f):
            for y in range(c):
                temp = a[x][y]
                a[x][y] = a[n-1-y][x]
                a[n-1-y][x] = a[n-1-x][n-1-y]
                a[n-1-x][n-1-y] = a[y][n-1-x]
                a[y][n-1-x] = temp


s = Solution()
import numpy as np
m = np.arange(1, 10).reshape(3, 3)
print m
print s.rotate(m)
print m
