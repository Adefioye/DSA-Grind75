class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack, res = root, [], []

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left 
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res