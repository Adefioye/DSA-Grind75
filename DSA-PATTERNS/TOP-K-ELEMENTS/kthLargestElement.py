from heapq import * 
import random

nums1 = [3,2,1,5,6,4]; k1 = 2
# Output: 5

nums2 = [3,2,3,1,2,4,5,5,6]; k2 = 4
# Output: 4
def partition(nums, l, r):

    pIndex, pivot = l, nums[r]

    for i in range(l, r):

        if nums[i] <= pivot:
            nums[i], nums[pIndex] = nums[pIndex], nums[i]
            pIndex += 1 

    # Swap rightmost value with pIndex value 
    nums[pIndex], nums[r] = nums[r], nums[pIndex]

    return pIndex 

def kthLargestElement(nums, k):

    kth = len(nums) - k 

    def quickSelect(l, r):

        rIdx = random.randint(l, r)
        # Swap end value for rIdx
        nums[rIdx], nums[r] = nums[r], nums[rIdx]
        pIndex = partition(nums, l, r)

        if pIndex == kth:
            return nums[pIndex]
        elif pIndex < kth:
            return quickSelect(pIndex + 1, r)
        else:
            return quickSelect(l, pIndex - 1)
    
    return quickSelect(0, len(nums) - 1)



print(kthLargestElement(nums1, k1))
print(kthLargestElement(nums2, k2))


# def kthLargestElement(nums, k):

#     minHeap = []

#     for num in nums:
#         heappush(minHeap, num)

#         if len(minHeap) > k:
#             heappop(minHeap)

#     return minHeap[0]

# print(kthLargestElement(nums1, k1))
# print(kthLargestElement(nums2, k2))

