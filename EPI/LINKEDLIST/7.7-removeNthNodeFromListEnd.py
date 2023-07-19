class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(0, head)
        left = dummyNode
        right = head

        for _ in range(n):
            right = right.next

        while right:
           left, right = left.next, right.next

        left.next = left.next.next

        return dummyNode.next