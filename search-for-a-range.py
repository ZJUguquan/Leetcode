class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if target not in A:
            return [-1,-1]
        pos = 0
        first = A.index(target)
        for i in  range(first+1, len(A)):
            if A[i] == target:
                pos +=1
            if A[i] > target:
                break
        return [first, first +pos]