class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def dfs(root):

            if not root:
                return 0

            leftH = dfs(root.left)
            rightH = dfs(root.right)
            res[0] = max(res[0], leftH + rightH)

            return 1 + max(leftH, rightH)

        dfs(root)
        return res[0]