# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root, minVal, maxVal):
            if not root:
                return True
            isNodeValueValid = minVal < root.val < maxVal
            left = dfs(root.left, minVal, root.val)
            right = dfs(root.right, root.val, maxVal)

            return isNodeValueValid and left and right 

        return dfs(root, float("-inf"), float("inf"))
        