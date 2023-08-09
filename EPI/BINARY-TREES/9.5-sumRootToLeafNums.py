class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, path):

            if not root:
                return 0

            path = path * 10 + root.val
            if not root.left and not root.right:
                return path

            return dfs(root.left, path) + dfs(root.right, path)

        return dfs(root, 0)