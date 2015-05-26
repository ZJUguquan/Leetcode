

def done_or_not(board):
    rows = board
    cols = [map(lambda x: x[i], board) for i in range(9)]
    squares = [
        board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
        for i in range(0, 9, 3)
        for j in range(0, 9, 3)]

    for clusters in (rows, cols, squares):
        for cluster in clusters:
            if sum(cluster) != 45 or len(set(cluster)) != 9:
                return False
    return True


def fill8(_list):
    if len([i for i in _list if i > 0]) == 8:
        _list[_list.index(0)] = 45 - sum(_list)
    return None


def flush(puzzle):
    for row in puzzle:
        fill8(row)
    for c in range(9):
        fill8([puzzle[i][c] for i in range(9)])

    return puzzle


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    flush(puzzle)
    while not done_or_not(puzzle):
        # zero existed
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    break

        in_row = puzzle[i]
        in_col = [puzzle[k][j] for k in range(9)]
        in_square = [puzzle[i // 3 * 3 + m][j // 3 * 3 + n]
                     for m in range(3)
                     for n in range(3)
                     ]
        occurence_neighbors = (
            set(in_row).union(set(in_col))).union(set(in_square))
        options = set(range(1, 10)) - (occurence_neighbors)

        for option in options:
            # try brute ,

            puzzle[i][j] = option
            if done_or_not(sudoku(puzzle)) == False:
                continue
            else:
                return sudoku(puzzle)


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print sudoku(puzzle)
