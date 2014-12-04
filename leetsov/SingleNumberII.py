class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        i, j , k = 0, 0, 0
        for ai in A:
            k = ai & j
            j = (j | (i & ai)) & (~k)
            i = (i | ai) & (~k)
        return i


'Still Confused'

