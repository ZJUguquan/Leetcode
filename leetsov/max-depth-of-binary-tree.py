# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            l, r = 1, 1
            if root.left != None:
                l = l + self.maxDepth(root.left)
            if root.right != None:
                r = r + self.maxDepth(root.right)
       #


        if l > r:
            return l
        else:
            return r

