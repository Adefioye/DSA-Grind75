
## THIRD SOLUTION: time = O (n)
class Solution:
    def pathSum(self, root, targetSum):

        self.count = 0 
        freq = {0 : 1} 

        def dfs(root, prevSum):

            if root is None:
                return 
            
            curSum = root.val + prevSum 
            x = curSum - targetSum 

            if x in freq:
                self.count += freq[x]

            if curSum in freq:
                freq[curSum] += 1 
            else:
                freq[curSum] = 1 

            dfs(root.left, curSum)
            dfs(root.right, curSum)
            freq[curSum] -= 1 

        dfs(root, 0) 

        return self.count

## SECOND SOLUTION: time = O (nlogn)
# class Solution:
#     def pathSum(self, root, targetSum):

#         self.total = 0 
#         self.path = []

#         def dfs(root):

#             if root is None:
#                 return 
            
#             self.path.append(root.val)

#             dfs(root.left)
#             dfs(root.right)

#             tempSum = 0
#             for i in range(len(self.path) - 1, -1, -1):
#                 tempSum += self.path[i]

#                 if tempSum == targetSum:
#                     self.total += 1 

#             # For removing last item added the path
#             self.path.pop()

#         dfs(root)

#         return self.total 
    

## FIRST SOLUTION: time = O(n ^ 2)
# class Solution:
#     def pathSumIII(self, root, targetSum):

#         self.total = 0

#         def helper(root, pathSum):
#             if root is None:
#                 return 
            
#             helper(root.left, pathSum + root.val)
#             helper(root.right, pathSum + root.val)

#             if (root.val + pathSum) == targetSum:
#                 self.total += 1

#         def dfs(root):

#             if root is None:
#                 return 
            
#             helper(root, 0)
#             dfs(root.left)
#             dfs(root.right)

#         dfs(root)

#         return self.total
