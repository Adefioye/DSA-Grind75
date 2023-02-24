
def sumNumbers(root):

    return dfs(root, "", 0)

def dfs(root, res, total):

    if root == None:
        return 0 

    if root.left is None and root.right is None:
        return total + int(res + str(root.val))
    
    leftRes = dfs(root.left, res + str(root.val), total)
    rightRes = dfs(root.right, res + str(root.val), total)

    return leftRes + rightRes
