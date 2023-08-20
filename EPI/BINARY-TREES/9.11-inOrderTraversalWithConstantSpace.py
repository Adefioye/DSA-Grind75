def InOrderTravesalUsingConstantSpace(root):

    cur, prev, res = root, None, []

    while cur:

        if prev is cur.parent:
            if cur.left:
                nxt = cur.left
            else:
                res.append(cur.val)
                nxt = cur.right or cur.parent
        elif prev is cur.left:
            res.append(cur.val)
            nxt = cur.right or cur.parent 
        else:
            nxt = cur.parent 

        prev, root = root, nxt 

    return res 

