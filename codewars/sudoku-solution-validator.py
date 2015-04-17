
def is9(list):
    if set(list) == set([i for i in range(1, 10)]) and len(list) == 9:
        return True
    return False


def validSolution(board):
    # row valid
    for i in range(9):
        if not is9(board[i]):
            return  False

    # column valid
    for j in range(9):
        if not is9([board[i][j] for i in range(9)]):
            return False

    # block valid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is9([board[i+m][j+n] for m in range(3) for n in range(3)]):
                return False
    return True

s = validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]])

print(s)