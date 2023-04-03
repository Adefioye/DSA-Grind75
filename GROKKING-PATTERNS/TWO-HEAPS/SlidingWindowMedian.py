from heapq import * 
import heapq

class SlidingWindowMedian:
    def medianOfSlidingWindow(self, nums, k):
        
        res = []
        maxHeap, minHeap = [], []

        for i in range(len(nums)):
            # Ensure maxHeap values <= minHeap 
            if not maxHeap or nums[i] <= -maxHeap[0]:
                # Insert value into maxHeap else minHeap
                heappush(maxHeap, -nums[i])
            else:
                heappush(minHeap, nums[i])

            # Rebalance the heaps to be properly sorted to compute median
            self.rebalanceHeap(minHeap, maxHeap)

            if i >= k - 1:
                res.append(self.findMedian(minHeap, maxHeap))

                elementToBeRemoved = nums[i-k+1]

                if elementToBeRemoved <= -maxHeap[0]:
                    self.removeElement(-elementToBeRemoved, maxHeap) 
                else:
                    self.removeElement(elementToBeRemoved, maxHeap)

            # Rebalance the heaps to be properly sorted to compute median
            self.rebalanceHeap(minHeap, maxHeap)


    def rebalanceHeap(self, minHeap, maxHeap):
        if len(maxHeap) > len(minHeap) + 1:
            heappush(minHeap, -heappop(maxHeap))
        elif len(maxHeap) < len(minHeap):
            heappush(maxHeap, -heappop(minHeap))
    
    def findMedian(self, minHeap, maxHeap):
        if len(minHeap) == len(maxHeap):
            return (-maxHeap[0] + minHeap) / 2 
        
        return -maxHeap[0]
    
    def removeElement(self, element, heap):
        idx = heap.index(element)

        heap[idx] = heap[-1]
        del heap[-1]

        if idx < len(heap):
            heapq._siftup(heap, idx)
            heapq._siftdown(heap, 0, idx)

