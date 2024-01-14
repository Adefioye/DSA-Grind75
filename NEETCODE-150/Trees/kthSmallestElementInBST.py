# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        def dfs(root):

            if not root:
                return 0
            
            
            left = dfs(root.left)
            if left:
                return left

            self.k -= 1
            if self.k == 0:
                return root.val

            right = dfs(root.right)

            return right

        return dfs(root)