
## SECOND SOLUTION 

def pathSum(root, targetSum):

    res = [] 

    def findPaths(root, pathSum, path):

        if root is None:
            return 
        
        if root.left is None and root.right is None:

            if (root.val + pathSum) == targetSum:
                res.append(path + [root.val]) 
                return 
            
        findPaths(root.left, pathSum + root.val, path + [root.val])
        findPaths(root.right, pathSum + root.val, path + [root.val])

    findPaths(root, 0, [])

    return res

## FIRST SOLUTION 

# def pathSum(root, targetSum):

#     if root is None:
#         return []

#     return findPaths(root, targetSum, [], [])

# def findPaths(node, sums, res, total):

#     if node.left is None and node.right is None:
#         if sums == node.val:
#             res.append(node.val)
#             total.append(total)

#     if node.left:
#         findPaths(node.left, sums - node.val, res + [node.val], total)
#     if node.right:
#         findPaths(node.right, sums - node.val, res + [node.val], total)

#     return total

