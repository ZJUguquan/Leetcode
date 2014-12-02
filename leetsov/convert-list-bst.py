class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param num, a list of integers
# @return a tree node
class Solution:
    def convert_array(self, left, right):
            """Convert num[left:right] to a (sub)tree."""
            # num[x:x] is an empty list (x is any number)
            if left >= right:
                return None
            mid = (left + right) // 2
            root = TreeNode(self.num[mid])
            root.left = self.convert_array(left, mid)
            root.right = self.convert_array(mid + 1, right)
            return root
    def sortedArrayToBST(self, num):
        self.num = num
        if len(num) < 1:
            return None
        if len(num) == 1:
            return TreeNode(num[0])
        return self.convert_array(0, len(num))


ls = [1,2,3,4]

s = Solution()
s.sortedArrayToBST(ls)
