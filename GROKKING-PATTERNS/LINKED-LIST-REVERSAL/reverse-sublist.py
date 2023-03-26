from typing import ListNode 

def reverseBetween(head, left, right):

    dummyNode = ListNode(0, head)
    prevLeftNode = head 
    pos = 0 
    current = head

    while current and pos < left:
        prevLeftNode = current
        current = current.next
        pos += 1

    tailNode = current 
    prev = None

    while current and pos >= left and pos <= right:
        nxt = current.next
        current.next = prev 
        prev = current 
        current = nxt 

    prevLeftNode.next = prev 
    tailNode.next = current 

    if left > 1:
        return head 
    
    return prev



    return
# def reverseBetween(head, left, right):

#     current = head
#     pos = 1
#     startNode = head

#     while pos < left:
#         startNode = current
#         current = current.next
#         pos += 1

#     tailNode = current
#     prevNode = None

#     while pos >= left and pos <= right:
#         nextNode = current.next
#         current.next = prevNode
#         prevNode = current
#         current = nextNode
#         pos += 1

#     startNode.next = prevNode
#     tailNode.next = current

#     if left > 1:
#         return head

        
#     return prevNode



