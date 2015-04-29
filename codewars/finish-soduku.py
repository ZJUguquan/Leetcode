'simpler!!'

def done_or_not(board):
  rows = board
  cols = [map(lambda x: x[i], board) for i in range(9)]
  squares = [
    board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
      for i in range(0, 9, 3)
      for j in range(0, 9, 3)]

  for clusters in (rows, cols, squares):
    for cluster in clusters:
      if len(set(cluster)) != 9:
        return 'Try again!'
  return 'Finished!'




'my first'
def done_or_not(board): #board[i][j]
	def is_validad(nineNumbers):
		if max([nineNumbers.count(i) for i in nineNumbers]) > 1:
			return False
		return True
	# row check
	for c in range(9):
		if not is_validad(board[c]):
			return 'Tray again!'

	# column check and region check
	columns = [ [] for i in range(9)]
	regions = [ [ [],[], [] ] for i in range(3)]
	for i in range(9):
		for j in range(9):
			regions[i//3][j//3].append(board[i][j])
			columns[j].append(board[i][j])

	# print(columns)
	if any([ not is_validad(c) for c in columns]):
		return 'Try again!'
	for i in range(3):
		for j in range(3):
			if not is_validad(regions[i][j]):
				return 'Try again!'
	# print(regions)
	return 'Finished!'


board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]

board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
print(done_or_not(board)
)
a = [  [[ ], [], []] for i in range(3)]
# print(a)

