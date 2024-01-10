# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, maxValSoFar):
            if not root:
                return 0
            res = 1 if root.val >= maxValSoFar else 0

            maxValSoFar = max(root.val, maxValSoFar)
            res += dfs(root.left, maxValSoFar)
            res += dfs(root.right, maxValSoFar)

            return res

        return dfs(root, float("-inf"))
        