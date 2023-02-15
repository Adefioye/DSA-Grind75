from collections import deque

def zigzagLevelOrderTraversal(root):

    
    return

# def zigzagLevelOrderTraversal(root):

#     if root == None:
#         return []

#     queue = deque()
#     queue.append(root)
#     level = 1
#     levelCount = 0
#     totalCount = len(queue)
#     levelRes = []
#     totalRes = []


#     while queue:
#         currentNode = queue.popleft()
#         leveCount += 1
#         levelRes.append(currentNode.val)

#         if currentNode.left:
#             queue.append(currentNode.left)
#         if currentNode.right:
#             queue.append(currentNode.right)
        
#         if levelCount == totalCount:
            
#             if level % 2 != 0:
#                 totalRes.append(levelRes)
#             else:
#                 totalRes.append(levelRes[::-1])
            
#             level += 1
#             levelRes = []
#             levelCount = 0 
#             totalCount = len(queue)

#     return totalRes