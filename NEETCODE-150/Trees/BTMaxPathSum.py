# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = root.val
        def dfs(root):
            if not root:
                return 0

            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))

            self.max = max(self.max, leftMax + rightMax + root.val)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return self.max
        