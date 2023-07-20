class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        #1. Find the middle of linked list
        #2. Reverse second half of linked list
        #3. Check if 1st half = 2nd half

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt 

        left, right = head, prev 

        while right:
            if right.val != left.val:
                return False 

            left, right = left.next, right.next

        return True