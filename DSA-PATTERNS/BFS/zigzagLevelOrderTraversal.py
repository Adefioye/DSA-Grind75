from collections import deque

def zigzagLevelOrderTraversal(root):

    if root == None:
        return []

    queue = deque()
    queue.append(root)
    level = 0
    totalRes = []


    while queue:
        levelRes = []
        level += 1

        for _ in range(len(queue)):
            currentNode = queue.popleft()
            levelRes.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        
        if level % 2 == 0:
            totalRes.append(levelRes[::-1])
        else:
            totalRes.append(levelRes)

    return totalRes