########################################################################
# Remove duplicates from sorted array
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        turtle, hare = 0, 0
        for hare in range(1, len(A)):
            if A[turtle] != A[hare]:
                A[turtle] = A[hare]
                turtle += 1
        return turtle


    # def removeDuplicates(self, A):
    #     buffer = A[-1]
    #     for idx, elem in enumerate(A[::-1]):
    #         if idx > 0:
    #             print(idx, elem)
    #             if elem == buffer:
    #                 A.pop(-idx)
    #                 print('deleting...')
    #             buffer = elem
    #     return A


s = Solution()
A = [4, 5, 6, 7, 7, 7, 8 ,8]
print(s.removeDuplicates(A))