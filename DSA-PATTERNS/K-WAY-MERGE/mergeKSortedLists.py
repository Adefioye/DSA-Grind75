from heapq import heapify, heappop, heappush

class ListNode:
    def __init__(self, val, next) -> None:
        self.val = val 
        self.next = next 

class Solution:
    def mergeKLists(self, lists):

        # Using minHeap 
        if lists is None or len(lists) == 0:
            return None 
        
        minHeap = []

        for i, pointer in enumerate(lists):
            if pointer:
                minHeap.append([pointer.val, i, pointer])

        # CReate a minHeap
        heapify(minHeap)

        head = tail = ListNode()

        while minHeap:
            _, i, pointer = heappop(minHeap)

            nxtPointer = pointer.next 

            if nxtPointer:
                heappush(minHeap, [nxtPointer.val, i, nxtPointer])
            
            tail.next = pointer 
            tail = pointer              

        return head.next 
    
