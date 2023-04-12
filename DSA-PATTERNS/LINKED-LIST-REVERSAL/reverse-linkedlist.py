

def reverseList(head):

    current = head
    prev = None
    next = None

    while current != None:
        next = current.next
        current.next = prev 
        prev = current 
        current = next


    return prev