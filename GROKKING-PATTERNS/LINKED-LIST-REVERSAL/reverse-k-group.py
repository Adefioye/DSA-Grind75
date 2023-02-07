# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    dummyNode = ListNode(0, head)
    grpPrev = dummyNode 

    while True:
        kth = kthNode(grpPrev, k)

        if not kth:
            break
            
        grpNext = kth.next

        prev, curr = grpNext, grpPrev.next

        while curr != grpNext:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        tmp = grpPrev.next
        grpPrev.next = kth
        grpPrev = tmp

    return dummyNode.next
    
def kthNode(curr, k):

    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr
                