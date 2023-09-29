class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: TreeNode
        """

        # Create a stack for holding the vals
        i = 0 
        stack = []
        
        while i < len(traversal):

            # Compute level based on number of dashes
            level = 0
            while i < len(traversal) and traversal[i] == "-":
                level += 1
                i += 1

            # Find val
            val = ""
            while i < len(traversal) and traversal[i] != "-":
                val += traversal[i]
                i += 1
            
            # Create a node for the val 
            newNode = TreeNode(int(val))

            print(level, int(val))
            while len(stack) > level:
                stack.pop()

            # Peek and add to left or right
            if len(stack) == 0:
                stack.append(newNode)
            else:
                node = stack[-1]

                if node.left:
                    node.right = newNode 
                else:
                    node.left = newNode 

                stack.append(newNode)

        return stack[0]