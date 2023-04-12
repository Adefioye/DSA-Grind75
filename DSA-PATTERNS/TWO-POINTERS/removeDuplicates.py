from typing import List

A1 = [2, 3, 3, 3, 6, 9, 9]  #4
A2 = [2, 2, 2, 11]          #2

# def removeDuplicates(array: List[int]) -> int:

#     left = 0
#     right = 1 

#     while right < len(array):
        
#         if array[right] != array[left]:
#             left += 1
#             right += 1
#         else:
#             array.pop(right)

#     return len(array)

# def removeDuplicates(array: List[int]) -> int:

#     l = 1 

#     for r in range(1, len(array)):

#         if array[r] != array[r - 1]:
#             array[l] = array[r]
#             l += 1 

#     return l

def removeDuplicates(nums):

    l = 0
    r = l + 1

    while r < len(nums):

        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
        
        r += 1

    return l + 1



print(removeDuplicates(A1))
print(removeDuplicates(A2))


