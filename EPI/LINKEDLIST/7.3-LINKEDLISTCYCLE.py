class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                break 

        if fast is None or fast.next is None:
            return None 
            
        if slow != fast:
            return None 

        p1 = head
        p2 = slow 

        while p1 != p2:
            p1, p2 = p1.next, p2.next

        return p1
