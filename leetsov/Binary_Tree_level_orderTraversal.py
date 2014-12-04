
'Discuss Solution not me'
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if (root == None):
            return [];
        else:
            all_levels = [[root.val]]
            left_levels = self.levelOrder(root.left)
            right_levels = self.levelOrder(root.right)
            m = min(len(left_levels), len(right_levels))
            for i in range(m):
                all_levels.append( left_levels[i] + right_levels[i])
            if (len(left_levels)>m):
                for j in range(m, len(left_levels)):
                    all_levels.append(left_levels[j])

            if (len(right_levels)>m):
                for k in range(m, len(right_levels)):
                    all_levels.append(right_levels[k])
            return all_levels