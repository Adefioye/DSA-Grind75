# USing two heaps
from heapq import *

## SECOND SOLUTION 
class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num):
        # Ensure maxHeap nums <= minHeap nums 
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        # This ensures size of maxHeap = size of minHeap
        # and size of maxHeap is not more than one greater size of minHeap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self):

        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2 
        
        return -self.maxHeap[0]


## FIRST SOLUTION
# class MedianFinder:

#     def __init__(self):
#         # using small and large heap
#         # small(max heap) and large(min heap)
#         self.small, self.large = [], []

#     def addNum(self, num):
#         heapq.heappush(self.small, -1 * num)

#         # Check if small <= large 
#         if (self.small and self.large 
#             and ((-1 * self.small[0]) > self.large[0])):
#             val = -1 * heapq.heappop(self.small)
#             heapq.heappush(self.large, val)

#         # if small has more one value than large,
#         # pop and push element from small to large
#         if len(self.small) > len(self.large) + 1:
#             val = -1 * heapq.heappop(self.small)
#             heapq.heappush(self.large, val)

#         # if large has more one value than small,
#         # pop and push element from large to small
#         if len(self.large) > len(self.small) + 1:
#             val = -1 * heapq.heappop(self.large)
#             heapq.heappush(self.small, val)
        

#     def findMedian(self):

#         if len(self.small) > len(self.large):
#             return -1 * self.small[0]
#         if len(self.large) > len(self.small):
#             return self.large[0]
#         if len(self.small) == len(self.large):
#             return  ((-1 * self.small[0]) + self.large[0]) / 2 
        

