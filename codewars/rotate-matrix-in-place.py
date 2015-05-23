
# s
def rotate_in_place(matrix):
    rows = len(matrix)
    if rows == 1:
        return matrix
    return [[matrix[dec][i] for dec in range(rows - 1, -1, -1)] for i in range(rows)]


matrix2 = [[1, 2],
           [3, 4]]
rmatrix2 = [[3, 1],
            [4, 2]]

print rotate_in_place(matrix2)


# answers from SO.
#

def rotate_in_place(matrix):

  a = matrix
  n = len(a)
  c = (n+1) / 2
  f = n / 2
  for x in range(c):
    for y in range(f):
      a[x][y] = a[x][y] ^ a[n-1-y][x]
      a[n-1-y][x] = a[x][y] ^ a[n-1-y][x]
      a[x][y] = a[x][y] ^ a[n-1-y][x]

      a[n-1-y][x] = a[n-1-y][x] ^ a[n-1-x][n-1-y]
      a[n-1-x][n-1-y] = a[n-1-y][x] ^ a[n-1-x][n-1-y]
      a[n-1-y][x] = a[n-1-y][x] ^ a[n-1-x][n-1-y]

      a[n-1-x][n-1-y] = a[n-1-x][n-1-y]^a[y][n-1-x]
      a[y][n-1-x] = a[n-1-x][n-1-y]^a[y][n-1-x]
      a[n-1-x][n-1-y] = a[n-1-x][n-1-y]^a[y][n-1-x]
  return a