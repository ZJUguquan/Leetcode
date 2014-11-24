"""


Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if A == [] or min(A) == 2 :return 1
        #A = sorted(A)
        for i in range(1,max(A) +1):
        	if i not in A:
        		return i
        return max(A) + 1