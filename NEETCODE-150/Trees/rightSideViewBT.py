# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def dfs(root, level):
            if not root: 
                return 

            if level == len(res):
                res.append(root.val)

            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 0)

        return res       