

def hasPathSum(root, targetSum):

    def dfs(root, targetSum, pathSum):

        if root is None:
            return False 
        
        if root.left is None and root.right is None:

            if (root.val + pathSum) == targetSum:
                return True 
            else:
                return False 
            
        leftRes = dfs(root.left, targetSum, pathSum + root.val)
        rightRes = dfs(root.right, targetSum, pathSum + root.val)

        return leftRes or rightRes 
    
    return dfs(root, targetSum, 0)

# def rootToLeafPathSum(root, targetSum, total):

#     if root == None:
#         return False

#     total += root.val

#     if root.left == None and root.right == None:
#         return total == targetSum

#     leftRes = rootToLeafPathSum(root.left, targetSum, total)
#     rightRes = rootToLeafPathSum(root.right, targetSum, total)

#     return leftRes or rightRes 


    

