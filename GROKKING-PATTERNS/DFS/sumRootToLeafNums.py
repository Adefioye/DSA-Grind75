#OPTIMAL SOLUTION

def sumNumbers(root):

    return dfs(root, 0)

def dfs(root, pathSum):

    if root is None:
        return 0
    
    pathSum = (pathSum * 10) + root.val

    if root.left is None and root.right is None:
        return pathSum

    leftRes = dfs(root.left, pathSum)
    rightRes = dfs(root.right, pathSum)

    return leftRes + rightRes


#   NON OPTIMAL solution

# def sumNumbers(root):

#     return dfs(root, "", 0)

# def dfs(root, res, total):

#     if root == None:
#         return 0 

#     if root.left is None and root.right is None:
#         return total + int(res + str(root.val))
    
#     leftRes = dfs(root.left, res + str(root.val), total)
#     rightRes = dfs(root.right, res + str(root.val), total)

#     return leftRes + rightRes
