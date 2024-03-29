class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = tail = ListNode(0)
        l1 = list1
        l2 = list2

        while l1 and l2:

            if l1.val <= l2.val:
                tail.next = l1 
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2 
                tail = l2 
                l2 = l2.next

        if l1:
            tail.next = l1
        
        if l2:
            tail.next = l2 
            
        return head.next