
matrix = [[0, 1, 1], [1, 0, 0], [1, 0, 1]]

print sum([True, True, False])
from pprint import pprint


def next_gen(cells):
    n = len(cells)
    matrix = [[False] * (n + 2) for i in range(n + 2)]
    for i in range(0, n):
        for j in range(0, n):
            matrix[i + 1][j + 1] = cells[i][j]
    # pprint(matrix)

    for row in range(1, n + 1):
        for column in range(1, n + 1):
            count_alive = sum(matrix[row - 1][column - 1:column + 1] + [matrix[row][
                              column - 1]] + [matrix[row][column + 1]] + matrix[row + 1][column - 1:column + 1])
            if count_alive < 2:
                matrix[row][column] = 0
            elif count_alive in (2, 3):
                matrix[row][column] = 1
            elif count_alive > 3:
                matrix[row][column] = 0

            count_dead = sum(cell for cell in matrix[row - 1][column - 1:column + 1] + [matrix[row][
                             column - 1]] + [matrix[row][column + 1]] + matrix[row + 1][column - 1:column + 1] if cell == 0)
            if count_dead == 3:
                matrix[row][column] = 1
    # pprint(matrix)
    return [[matrix[i][j] for j in range(1, n + 1)] for i in range(1, n + 1)]

print next_gen(matrix)




########################################################################
#
#

def next_gen(cells):
    N = len(cells)
    M = len(cells[0]) if N else 0
    def count_neighbours(i, j):
        indices = ((i+di,j+dj) for di in (-1,0,1) for dj in (-1,0,1) if di!=0 or dj!=0)
        return sum(cells[k][l] for (k,l) in indices if 0<=k<N and 0<=l<M)
    return [[(2 if cells[i][j] else 3)<=count_neighbours(i,j)<=3 for j in xrange(M)] for i in xrange(N)]
