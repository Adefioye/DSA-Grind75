from heapq import * 

class Solution:
    def __init__(self, k, nums):
        self.minHeap, self.k = nums, k 
        heapify(self.minHeap)

        while len(self.minHeap) > k:
            heappop(self.minHeap)

    def add(self, val):
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]
    

