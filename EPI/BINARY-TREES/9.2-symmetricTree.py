# BFS SOLUTION
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                curNode = q.popleft()
                
                if curNode:
                    level.append(curNode.val)
                    q.append(curNode.left)
                    q.append(curNode.right)
                else:
                    level.append(None)              

            if not self.isPalindrome(level):
                return False

        return True


    def isPalindrome(self, arr):
        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False 
            l, r = l + 1, r - 1
        return True
    
# DFS SOLUTION
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left, right):

            if not left and not right:
                return True 
            
            if not left or not right:
                return False 

            return (left.val == right.val and 
                    dfs(left.left, right.right) and 
                    dfs(right.left, left.right))

        return dfs(root.left, root.right)