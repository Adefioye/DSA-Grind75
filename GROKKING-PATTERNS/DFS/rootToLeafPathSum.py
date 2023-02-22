def rootToLeafPathSum(root, targetSum, total):

    if root == None:
        return False

    total += root.val

    if root.left == None and root.right == None:
        return total == targetSum

    leftRes = rootToLeafPathSum(root.left, targetSum, total)
    rightRes = rootToLeafPathSum(root.right, targetSum, total)

    return leftRes or rightRes 


    

