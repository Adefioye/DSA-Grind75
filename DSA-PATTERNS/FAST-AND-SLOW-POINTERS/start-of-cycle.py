
def detectCycle(head):

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
        
    if fast == None or fast.next == None:
        return None

    p1 = head
    p2 = slow

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1