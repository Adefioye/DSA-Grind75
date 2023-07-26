class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = collections.deque()
        q.append(root)
        allLevel = []

        if not root:
            return allLevel

        while q:
            curLevel = []
            for _ in range(len(q)):
                curr = q.popleft()
               
                curLevel.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            allLevel.append(curLevel)

        return allLevel