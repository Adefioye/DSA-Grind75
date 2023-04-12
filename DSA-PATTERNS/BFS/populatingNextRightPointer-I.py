from collections import deque


## OPTIMAL SOLUTION

def populatingNextRightPointers(root):
    curr, nxt = root, root.left if root else None

    while curr and nxt:

        curr.left.next = curr.right 

        if curr.next:
            curr.right.next = curr.next.left

        curr = curr.next

        if not curr:
            curr = nxt
            nxt = curr.left

    return root

# def populatingNextRightPointers(root):

#     if root == None:
#         return []

#     queue = deque()
#     queue.append(root)

#     while queue:

#         levelRes = queue()

#         for _ in range(len(queue)):
#             currentNode = queue.popleft()
#             levelRes.append(currentNode)

#             if currentNode.left:
#                 queue.append(currentNode.left)
#             if currentNode.right:
#                 queue.append(currentNode.right)
        

#         prev = levelRes.popleft()
#         while levelRes:
#             currentNode = levelRes.popleft()
#             prev.next = currentNode 
#             prev = currentNode


#     return root

