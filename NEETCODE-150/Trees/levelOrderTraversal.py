from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []

        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                curNode = q.popleft()
                level.append(curNode.val)

                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)

            res.append(level)

        return res
        