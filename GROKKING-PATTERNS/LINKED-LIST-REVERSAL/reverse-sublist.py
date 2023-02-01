def reverseBetween(self, head, left, right):

    beforeLeftPos = left - 1
    afterRightPos = right + 1
    pos = 1
    current = head
    beforeLeftNode = None
    afterRightNode = None

    while beforeLeftPos >= 1 and current != None and pos != left:

        if pos == beforeLeftPos:
            beforeLeftNode = current

        current = current.next
        pos += 1

    tail = current
    prev = None
    while current != None and pos != afterRightPos:
        next = current.next
        current.next = prev
        prev = current
        current = next
        pos += 1

    afterRightNode = current

    # Tack on the nodes
    #

    if beforeLeftNode and left > 1:
        beforeLeftNode.next = prev 

    if tail and afterRightNode:
         tail.next = afterRightNode 

    
    if left > 1:
        return head

    return prev