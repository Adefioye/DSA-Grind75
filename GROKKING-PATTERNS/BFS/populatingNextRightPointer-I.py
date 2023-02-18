from collections import deque

def populatingNextRightPointers(root):

    if root == None:
        return []

    queue = deque()
    queue.append(root)

    while queue:

        levelRes = queue()

        for _ in range(len(queue)):
            currentNode = queue.popleft()
            levelRes.append(currentNode)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        
        
        prev = levelRes.popleft()
        while levelRes:
            currentNode = levelRes.popleft()
            prev.next = currentNode 
            prev = currentNode


    return root