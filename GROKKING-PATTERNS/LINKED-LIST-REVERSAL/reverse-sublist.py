
def reverseBetween(head, left, right):

    current = head
    pos = 1
    startNode = head

    while pos < left:
        startNode = current
        current = current.next
        pos += 1

    tailNode = current
    prevNode = None

    while pos >= left and pos <= right:
        nextNode = current.next
        current.next = prevNode
        prevNode = current
        current = nextNode
        pos += 1

    startNode.next = prevNode
    tailNode.next = current

    if left > 1:
        return head

        
    return prevNode



