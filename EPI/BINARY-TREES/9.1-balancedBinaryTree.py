# SOLUTION 1
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bF = 0
        def dfs(root):

            if root == None:
                return 0 

            left, right = dfs(root.left), dfs(root.right)
            self.bF = max(self.bF, abs(left - right) )
            
            return 1 + max(left, right)

        dfs(root)

        print(self.bF)
        return self.bF <= 1
    
# SOLUTION 2
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            if root == None:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = ( left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
            height = 1 + max(left[1], right[1])

            return [balanced, height]

        return dfs(root)[0]