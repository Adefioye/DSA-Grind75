# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# USING DFS 

def minDepth(root):

    minLevel = float("inf")

    def dfs(root, level):

        if root is None:
            return
        
        if root.left is None and root.right is None:
            minLevel = min(minLevel, level)
            return 
        
        dfs(root.left, level + 1)
        dfs(root.right, level + 1)

    dfs(root, 1)

    return minLevel
# USING BFS
# def minDepth(root):

#     if root == None:
#         return 0

#     queue = deque()
#     queue.append(root)
#     depth = 0
        
#     while queue:
#         depth += 1

#         for _ in range(len(queue)):

#             currentNode = queue.popleft()

#             if currentNode.left == None and currentNode.right == None:
#                 return depth 
#             if currentNode.left:
#                 queue.append(currentNode.left)
#             if currentNode.right:
#                 queue.append(currentNode.right)


                    