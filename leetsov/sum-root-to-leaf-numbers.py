# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
    	self.ans = 0
    def dfs(self,root, prefix):

    	if root is None:
    		return None
    	if root.left is None and root.right is None:
    		self.ans += prefix * 10 + root.val
    		return None
    	if root.left is not None:
    		self.dfs(root.left, prefix*10 + root.val)
    	if root.right is not None:
    		self.dfs(root.right, prefix*10+root.val)
    	return None
    def sumNumbers(self, root):
    	#ans = self.ans
    	self.dfs(root, 0)
    	return self.ans

s = Solution()
t1 = TreeNode(9)
t2 = TreeNode(2)
t3 = TreeNode(1)
t1.left = t2
t1.right = t3

a=s.sumNumbers(t1)
print(a)