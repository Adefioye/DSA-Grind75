class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.balanceFactor = 0
        def dfs(root):

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.balanceFactor = max(self.balanceFactor, abs(left - right))

            return 1 + max(left, right)
        
        dfs(root)

        return self.balanceFactor <= 1