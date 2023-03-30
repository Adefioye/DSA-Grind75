
## FIRST SOLUTION: time = O(n ^ 2)
class Solution:
    def pathSumIII(self, root, targetSum):

        self.total = 0

        def helper(root, pathSum):
            if root is None:
                return 
            
            helper(root.left, pathSum + root.val)
            helper(root.right, pathSum + root.val)

            if (root.val + pathSum) == targetSum:
                self.total += 1

        def dfs(root):

            if root is None:
                return 
            
            helper(root, 0)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return self.total
