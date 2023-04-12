# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# SOLUTION 2
def levelOrderBottom(root):

    if root == None:
        return []

    queue = deque()
    queue.append(root)
    totalRes = []

    while queue:

        levelRes = []

        for _ in range(len(queue)):
            currentNode = queue.popleft()
            levelRes.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        totalRes.append(levelRes)

    return totalRes[::-1]



# def levelOrderBottom( root):
#     if root == None:
#         return []

#     queue = deque()
#     queue.append(root)
#     totalRes = deque()
#     levelRes = []
#     levelCount = 0
#     totalCount = len(queue)

#     while queue:
#         currentNode = queue.popleft()
#         levelCount += 1
#         levelRes.append(currentNode.val)

#         if currentNode.left:
#             queue.append(currentNode.left)
#         if currentNode.right:
#             queue.append(currentNode.right)

#         if levelCount == totalCount:
#             totalRes.appendleft(levelRes)
#             levelRes = []
#             levelCount = 0
#             totalCount = len(queue)

#     return totalRes
