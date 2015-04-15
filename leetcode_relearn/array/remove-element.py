

########################################################################
## remove - element

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, j = 0, 0
        for i in  range(len(A)):
            if A[i] == elem:
                continue
            A[j] = A[i]
            j += 1
        return j

########################################################################
s = Solution()
A = [4, 5]
elem = 4
print(s.removeElement(A, elem))

