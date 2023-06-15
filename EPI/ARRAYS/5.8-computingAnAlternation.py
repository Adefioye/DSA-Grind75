nums1 = [3, 5, 2, 1, 6, 4]
nums2 = [1, 2, 3, 4]


def wiggleSort(nums):

    for i in range(1, len(nums)):

        # if odd, value >= prev, otherwise swap 
        # if even, value <= prev, otherwise swap 
        if i % 2 != 0 and nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        elif i % 2 == 0 and nums[i] > nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums 

print(wiggleSort(nums1))
print(wiggleSort(nums2))