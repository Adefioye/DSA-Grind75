# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(head):

    visit = []
    current = head
    length = 0

    if current == None:
        return None

    while current != None and current not in visit:
        visit.append(current)
        length += 1
        current = current.next

    if length % 2 != 0:
        return visit[(length // 2)]
    else:
        return visit[int(length / 2)]

def optimalmiddleNode(head):

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow 


