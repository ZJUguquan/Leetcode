# modify and return the original matrix rotated 90 degrees clockwise in place
def rotate_in_place(matrix):
    return [[row[i] for row in reversed(matrix)] for i in range(len(matrix))]

matrix2 = [[1, 2],
           [3, 4]]

print(rotate_in_place(matrix2))

from unittest import TestCase
Test = TestCase()
# Test.describe("rotate_in_place")
matrix2 = [[1, 2],
           [3, 4]]
rmatrix2 = [[3, 1],
            [4, 2]]
# Test.it("should return the rotated matrices")
Test.assertEquals(rotate_in_place(matrix2), rmatrix2)