# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True 

        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, root, subRoot):

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
            
        left = self.isSameTree(root.left, subRoot.left)
        right = self.isSameTree(root.right, subRoot.right)

        return root.val == subRoot.val and left and right