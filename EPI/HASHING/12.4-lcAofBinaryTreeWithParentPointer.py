
def lcAOfBinaryTreeWithParentPointer(node1, node2):
    """
    This approach optimizes for nodes with lowest distance to LCA
    """
    node_to_root_path = set()
    node1, node2 = iter1, iter2 
    while iter1 or iter2:

        if iter1:
            if iter1 in node_to_root_path:
                return iter1 
            node_to_root_path.add(iter1)
            iter1 = iter1.parent 
        
        if iter2:
            if iter2 in node_to_root_path:
                return iter2 
            node_to_root_path.add(iter2)
            iter2 = iter2.parent 

    raise ValueError("node1 and node2 not in the same tree")
