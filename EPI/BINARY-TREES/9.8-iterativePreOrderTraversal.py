class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        cur, stack, res = root, [], []

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()

        return res