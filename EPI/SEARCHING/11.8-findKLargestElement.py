import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        kth  = len(nums) - k 

        def quickSelect(nums, l, r):

            # Create a random idx and swap with end value
            rIdx = random.randint(l, r)
            nums[rIdx], nums[r] = nums[r], nums[rIdx]
            pIdx = self.partition(nums, l, r)

            if kth == pIdx:
                return nums[pIdx]
            elif kth < pIdx:
                return quickSelect(nums, l, pIdx - 1)
            else:
                return quickSelect(nums, pIdx + 1, r)
        
        return quickSelect(nums, 0, len(nums) - 1)
        
    def partition(self, nums, l, r):
        pIdx, pivot = l, nums[r]

        for i in range(l, r):

            if nums[i] <= pivot:
                nums[i], nums[pIdx] = nums[pIdx], nums[i]
                pIdx += 1
        
        # Swap with end value 
        nums[pIdx], nums[r] = nums[r], nums[pIdx]

        return pIdx
        