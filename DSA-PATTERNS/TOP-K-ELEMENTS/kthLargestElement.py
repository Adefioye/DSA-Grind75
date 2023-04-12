from heapq import * 

nums1 = [3,2,1,5,6,4]; k1 = 2
# Output: 5

nums2 = [3,2,3,1,2,4,5,5,6]; k2 = 4
# Output: 4
def kthLargestElement(nums, k):

    minHeap = []

    for num in nums:
        heappush(minHeap, num)

        if len(minHeap) > k:
            heappop(minHeap)

    return minHeap[0]

print(kthLargestElement(nums1, k1))
print(kthLargestElement(nums2, k2))

