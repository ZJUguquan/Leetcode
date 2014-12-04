# class Solution:
# # @param A a list of integers
# # @return nothing, sort in place
def sortColors(self, A):
    if A != None and len(A) > 1:
        A, one, two = self._sort(A)
        # one is the place to insert 1, two is the place to insert 2

def _sort(self, A):
    if len(A) == 1:
        if A[0] == 0:
            return A, 1, 1
        if A[0] == 1:
            return A, 0, 1
        if A[0] == 2:
            return A, 0, 0

    tmp = A[-1]
    A, one, two = self._sort(A[:-1])
    if tmp == 0:
        A.insert(0, tmp)
        return A, one+1, two+1
    if tmp == 1:
        A.insert(one,tmp)
        return A, one, two+1
    if tmp == 2:
        A.insert(two,tmp)
        return A, one, two

def test(A):
	if A > 0:
		return A,1,1
print test(3)

import math
print math.log(64,2)