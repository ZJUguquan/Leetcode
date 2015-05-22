# coding: utf-8


# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


note = '将一个排序好的列表转为BST'
test = range(1,11)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        count = len(nums)
        if count == 0: return None
        if count == 1:
            root = TreeNode(nums[0])
        elif count <=4:
            root = TreeNode(nums[1])
            root.left = self.sortedArrayToBST(nums[:1])
            root.right = self.sortedArrayToBST(nums[2:])
        else:
            root = TreeNode(nums[count//2])
            root.left = self.sortedArrayToBST(nums[:count//2])
            root.right = self.sortedArrayToBST(nums[count//2+1:])
        return root