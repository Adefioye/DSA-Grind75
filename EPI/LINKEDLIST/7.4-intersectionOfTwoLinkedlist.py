class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def length(node):

            l = 0 

            while node:
                l += 1 
                node = node.next

            return l 

        sizehA, sizehB = length(headA), length(headB)
        # We always want to make headB the node with higher length

        if sizehA > sizehB:
            headA, headB = headB, headA 

        # Advance headB by the diff between the 2 
        for _ in range(abs(sizehA - sizehB)):
            headB = headB.next 

        while headA and headB and headA is not headB:
            headA, headB = headA.next, headB.next 

        if headA and headA == headB:
            return headA 

        return None