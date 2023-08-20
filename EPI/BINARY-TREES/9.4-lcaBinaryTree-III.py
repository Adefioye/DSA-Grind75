def lCAWithParentPointer(node0, node1):
    # Find depth of node 
    def getDepth(node):
        depth = 0 
        while node:
            depth += 1 
            node = node.parent 
        return depth 
    
    depthNode0, depthNode1 = getDepth(node0), getDepth(node1)

    # To simplify code, we make node0 the one with higher depth
    if depthNode1 > depthNode0:
        node0, node1 = node1, node0 

    depthDiff = abs(depthNode0 - depthNode1)

    # if node0 depth is higher, we make sure to make its depth level with node1
    while depthDiff:
        depthDiff -= 1 
        node0 = node0.parent 
    
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent 

    return node0