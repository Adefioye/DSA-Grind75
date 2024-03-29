nums1 = [4, 0, 3, 1]                #   2
nums2 = [8, 3, 5, 2, 4, 6, 0, 1]    #   7

def missing_num(nums):

    i = 0
    nums_length = len(nums)

    while i < nums_length:
        newSpot = nums[i]

        if nums[i] != i and newSpot < nums_length:
            nums[newSpot], nums[i] = nums[i], nums[newSpot]
        else:
            i += 1

    for i, item in enumerate(nums):
        if item != i:
            return i
        
    return nums_length


# def missing_num(nums):
#     #1. nums range from 0 to n
#     # Use cyclic sort to sort the array in-place
#     # Iterate over the array and return index where A[i] != i

#     i = 0
#     while i < len(nums):

#         if nums[i] != i:
#             newSpot = nums[i]

#             if newSpot < len(nums):
#                 nums[i], nums[newSpot] = nums[newSpot], nums[i]
#             else:
#                 i += 1
#         else:
#             i += 1

#     for i, num in enumerate(nums):
#         if num != i:
#             return i


print(missing_num(nums1))
print(missing_num(nums2))