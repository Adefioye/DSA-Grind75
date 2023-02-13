

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


def levelOrder(root):

    if root == None:
        return []

    queue = deque()
    queue.append(root)
    totalCount = len(queue)
    levelCount = 0
    levelRes = []
    totalRes = []

    while len(queue) > 0:

        # Increse level count upon proccesing item from the queue
        # and append value to result
        current = queue.popleft()
        levelCount += 1
        levelRes.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        # After adding children, we check if level count is equal to total count
        # Hence add level result to total res and re-instantiate res array and level count
        # While also recomputing item on the queue which is to be processed in the next level
        if levelCount == totalCount:
            totalRes.append(levelRes)
            levelRes = []
            levelCount = 0
            totalCount = len(queue)

    return totalRes
