'other solution'


def isSolved(board):
  for i in range(0,3):
    if board[i][0] == board[i][1] == board[i][2] != 0:
      return board[i][0]
    elif board[0][i] == board[1][i] == board[2][i] != 0:
      return board[0][i]

  if board[0][0] == board[1][1] == board[2][2] != 0:
    return board[0][0]
  elif board[0][2] == board[1][1] == board[2][0] != 0:
    return board[0][0]

  elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
    return 0
  else:
    return -1




'勉强勉强通过'


def alleq(lis):
    if max(lis) == min(lis) and min(lis) > 0:
        return max(lis)
    return False

# print(alleq([1,1,1]))

def isSolved(board):

    for i in range(3):
        if alleq(board[i]):
            return alleq(board[i])
    for j in range(3):
        column = [ board[0][j], board[1][j], board[2][j]]
        if alleq(column):
            return alleq(column)
    left = [board[0][0], board[1][1], board[2][2]]
    if alleq(left): return alleq(left)
    right = [board[0][2], board[1][1], board[2][0]]
    if alleq(right): return alleq(right)
    if any([ 0 in row for row in board]): return -1
    return 0





def alleq(lis):
    if max(lis) == min(lis):
        return max(lis)
    return False

# print(alleq([1,1,1]))

def isSolved(board):
    if any([ 0 in row for row in board]): return -1
    for i in range(3):
        if alleq(board[i]):
            return alleq(board[i])
    for j in range(3):
        column = [ board[0][j], board[1][j], board[2][j]]
        if alleq(column):
            return alleq(column)
    left = [board[0][0], board[1][1], board[2][2]]
    if alleq(left): return alleq(left)
    right = [board[0][2], board[1][1], board[2][0]]
    if alleq(right): return alleq(right)
    return 0

board = [[1,1,2],
                      [2,1,2],
                      [2,1,2]]
# print(any ([ i for i in  [1,True, False]  if i < 1 ]))
print(isSolved(board))
'''
# You can use test.expect(boolean, [optional] string) to test your code
test.expect(isSolved(  [[1,1,1],
                      [2,1,2],
                      [2,1,2]]  ) is -1)
'''
'''descriptor  tic-tac-toe checker

If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an X, or 2 if it is an O, like so:

[[0,0,1],
 [0,1,2],
 [2,1,0]]

We want our function to return -1 if the board is not solved yet, 1 if X won, 2 if O won, or 0 if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.


'''

