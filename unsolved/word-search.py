'word search'




'think about a word a consider its all adjacent '

'a dp question'

class Solution:
	used = None
	board = None
	word = None
	def isInboard(self,i, j):
		if i < 0 or i >= len(self.board) or j < 0 or j >= len(self.board[i]):
			return False
		return True

	def DFS(self,si, sj, n):
		if n == len(self.word):
			return True
		if self.isInboard(si, sj):
			if (not self.used[si][sj]) and self.board[si][sj] == self.word[n]:
				self.used[si][sj] = True
				ret = False
				if self.DFS(si-1, sj, n+1):
					ret = True
				elif self.DFS(si+1, sj, n+1):
					ret = True
				elif self.DFS(si, sj-1, n+1):
					ret = True
				elif self.DFS(si, sj+1, n+1):
					ret = True
				self.used[si][sj] = False
				return ret
		return False

	def exist(self, board, word):
		self.board = board
		self.word = word
		if len(board) == 0:
			return False
		self.used = [ [False for i in range(len(board))] for j in range(len(board[0])) ]
		for i in range(0, len(board)):
			for j in range(0, len(board[i])):
				if self.DFS(i,j, 0):
					return True
		return False

s = Solution()


board = [
	["ABCE"],
  	["SFCS"],
  	["ADEE"]
]

word = "ABCCED"
print(s.exist(board, word))