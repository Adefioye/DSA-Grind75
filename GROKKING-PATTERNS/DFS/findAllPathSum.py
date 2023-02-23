
def pathSum(root, targetSum):

    if root is None:
        return []

    return findPaths(root, targetSum, [], [])

def findPaths(node, sums, res, total):

    if node.left is None and node.right is None:
        if sums == node.val:
            res.append(node.val)
            total.append(total)

    if node.left:
        findPaths(node.left, sums - node.val, res + [node.val], total)
    if node.right:
        findPaths(node.right, sums - node.val, res + [node.val], total)

    return total

