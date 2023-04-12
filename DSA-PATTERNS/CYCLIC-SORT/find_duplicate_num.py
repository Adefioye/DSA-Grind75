nums1 = [1, 4, 4, 3, 2]     #   4
nums2 = [2, 1, 3, 3, 5, 4]  # 3
nums3 = [2, 4, 1, 4, 4]     #    4

def findDuplicateNum(nums):

    i = 0

    while i < len(nums):
        newSpot = nums[i] - 1

        if nums[i] != i + 1 and nums[newSpot] != newSpot + 1:
            nums[i], nums[newSpot] = nums[newSpot], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]

print(findDuplicateNum(nums1))
print(findDuplicateNum(nums2))
print(findDuplicateNum(nums3))