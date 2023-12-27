
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return 

        root.right, root.left = root.left, root.right

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        