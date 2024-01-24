import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "X,"
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return str(root.val) + "," + left + right
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q = collections.deque(data.split(","))

        def deserializeHelper(q):
            val = q.popleft() if q else None
            if val == "X" or None:
                return None

            tree = TreeNode(val)
            tree.left = deserializeHelper(q)
            tree.right = deserializeHelper(q)

            return tree

        return deserializeHelper(q)


