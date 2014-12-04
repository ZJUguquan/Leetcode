"""

Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""

'Accept'

'use'

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        return  any( [target in row  for row in matrix]  )

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
    	# matrix m * n
    	pass
    	for row in range(len(matrix)-1, -1,-1 ):
    		pos = matrix[row][0]
    		if target == pos:
    			return True
    		elif target > pos:
    			return True



matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
for row in range(len(matrix)-1, -1,-1 ):
	print(row)

print(len(matrix))
target= 3
s = Solution()

print(  any( [target in row  for row in matrix]  ))