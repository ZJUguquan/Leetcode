class Sudoku():
    def __init__(self, data):
      self.data =data

    def is_valid(self):
      board = self.data
      rows = board
      N = len(board)
      if len(set(len(row) for row in board ) ) > 1: return False
      n = int(N**.5)
      cols = [map(lambda x: x[i], board) for i in range(N)]
      squares = [
        board[i][j:j + n] + board[i + 1][j:j + n] + board[i + 2][j:j + n]
          for i in range(0, N, n)
          for j in range(0, N, n)
          ]

      for clusters in (rows, cols, squares):
        for cluster in clusters:
          if len(set(cluster)) != N:
            return False
      return True

print(int(9**.5))

board = [
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

print(Sudoku(board))