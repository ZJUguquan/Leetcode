# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",

# When s3 = "aadbbcbcac", return true.
#   aa(s1)   db(s2)
# When s3 = "aadbbbaccc", return false.


"""
Here is some explanation:

DP table represents if s3 is interleaving at (i+j)th position when s1 is at ith position, and s2 is at jth position. 0th position means empty string.

So if both s1 and s2 is currently empty, s3 is empty too, and it is considered interleaving. If only s1 is empty, then if previous s2 position is interleaving and current s2 position char is equal to s3 current position char, it is considered interleaving. similar idea applies to when s2 is empty. when both s1 and s2 is not empty, then if we arrive i, j from i-1, j, then if i-1,j is already interleaving and i and current s3 position equal, it s interleaving. If we arrive i,j from i, j-1, then if i, j-1 is already interleaving and j and current s3 position equal. it is interleaving.
"""


class Solution:
	def isInterleave(self, s1, s2, s3):
		if len(s1) + len(s2) != len(s3):
			return False
		if not s1: return s2 == s3
		if not s2: return s1 == s3
		matrix = [ [0 for i in range(len(s1) + 1) ] for j in range(len(s2) + 1)]

		for i in range(len(s1)+1):
			for j in range(len(s2)+1):
				if i == 0 and j ==0:
					matrix[i][j] = True
				elif i == 0:
					# s3 top ~ k  substring come from one string (s1 or s2)
					matrix[0][j] = (matrix[0][j-1] and s2[j-1] == s3[j-1] )
				elif j == 0:
					matrix[i][0] = (matrix[i-1][0] and s1[i-1] == s3[i-1] )
				else:
					matrix[i][j] = (matrix[i-1][j] and s1[i-1] == s3[i+j-1]) or (matrix[i][j-1] and s2[j-1] == s3[i+j-1])

		return matrix[len(s1)][len(s2)]

s = Solution()
# s1 = "aabcc"
s1 = "aabaac"
# s2 = "dbbca"
s2 = "aadaaeaaf"
# s3 = "aadbbcbcac"
s3 = "aadaaeaabaafaac"
print(s.isInterleave(s1,s2,s3))