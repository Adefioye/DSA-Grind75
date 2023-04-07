nums1 = [4, 6, 6, 6, 9]; key1 = 6
# Output: [1, 3]
nums2 = [1, 3, 8, 10, 15]; key2 = 10
# Output: [3, 3]
nums3 = [1, 3, 8, 10, 15]; key3 = 12
# Output: [-1, -1]

## FIRST SOLUTION WITHOUT FLAG
# def numberRange(nums, key):

#     l, r = 0, len(nums) - 1 

#     if key < nums[0] or key > nums[r]:
#         return [-1, -1]
    
#     while l <= r:

#         mid = (l + r) // 2 

#         if key < nums[mid]:
#             r = mid - 1 
#         elif key > nums[mid]:
#             l = mid + 1 
#         else:
#             # Break array into right /left
#             res = []
#             while l <= mid:

#                 midL = (l + mid) // 2 

#                 if key <= nums[midL]:
#                     mid = midL - 1 
#                 else:
#                     l = midL + 1 
#             res.append(l)

#             while mid <= r:

#                 midR = (mid + r) // 2 

#                 if key >= nums[midR]:
#                     mid = midR + 1 
#                 else:
#                     r = midR - 1 
#             res.append(r)
#             return res 
        
#     return [-1, -1]

# print(numberRange(nums1, key1))
# print(numberRange(nums2, key2))
# print(numberRange(nums3, key3))

