class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd = head
        evenStart = evenEnd = head.next if head else None
        if not evenStart:
            return head 
            
        curr = head.next.next if head.next else None 
        pos = 2 

        while curr:
            pos += 1 

            if pos % 2 != 0:
                nxt = curr.next 
                odd.next = curr 
                curr.next = evenStart 
                evenEnd.next = nxt
                odd = curr 
                curr = nxt 
            else:
                evenEnd = curr 
                curr = curr.next 

        return head