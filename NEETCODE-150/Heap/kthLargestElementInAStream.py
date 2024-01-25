from heapq import heappush, heappop

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        self.minHeap = []
        for num in self.nums:
            heappush(self.minHeap, num)
            if len(self.minHeap) > self.k:
                heappop(self.minHeap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
                heappop(self.minHeap)
        
        return self.minHeap[0]
        