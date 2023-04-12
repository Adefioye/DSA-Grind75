nums1 = [1, 3, 8, 12, 4, 2]
# Output: 12
nums2 = [3, 8, 3, 1]
# Output: 8
nums3 = [1, 3, 8, 12]
# Output: 12
nums4 = [10, 9, 8]
# Output: 10

def maxElementInBitonicArr(nums):

    findMax = nums[-1] > nums[0]
    l, r = 0, len(nums) - 1 
    maxV = float("-inf")

    while l <= r:

        mid = (l + r) // 2 

        if nums[mid] > maxV:
            maxV = nums[mid]

        # Search left or right side 
        if mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
            l = mid + 1 
        elif mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
            r = mid - 1
        else:

            if findMax:
                l = mid + 1 
            else:
                r = mid - 1 

    return maxV 

print(maxElementInBitonicArr(nums1))
print(maxElementInBitonicArr(nums2))
print(maxElementInBitonicArr(nums3))
print(maxElementInBitonicArr(nums4))
