class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def pathWithGivenSequence(root, array):
    
    return dfs(root, [], array)

def dfs(root, res, array):

    if root is None:
        return False 
    
    if root.left is None and root.right is None:
        res.append(root.val)
        return res == array 
    
    leftRes = dfs(root.left, res + [root.val], array)
    rightRes = dfs(root.right, res + [root.val], array)

    return leftRes or rightRes

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: ", pathWithGivenSequence(root, [1, 0, 7]))
  print("Tree has path sequence: ", pathWithGivenSequence(root, [1, 1, 6]))


main()