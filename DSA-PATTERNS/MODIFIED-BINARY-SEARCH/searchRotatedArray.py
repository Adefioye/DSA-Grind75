nums1 = [4,5,6,7,0,1,2]; target1 = 0
# Output: 4
nums2 = [4,5,6,7,0,1,2]; target2 = 3
# Output: -1
nums3 = [1]; target3 = 0
# Output: -1

# SECOND SOLUTION
class Solution:
    def search(self, nums, target):

        l, r = 0, len(nums) - 1 

        while l <= r:

            mid = (l + r) // 2 

            if target == nums[mid]:
                return mid 
            
            elif nums[l] <= nums[mid]:
                # Search left sorted portion

                if nums[l] <= target <= nums[mid]:
                    r = mid - 1 
                else:
                    l = mid + 1
            else:
                # Search right sorted portion
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1 

        return -1


        return 
    


# FIRST SOLUTION
# time = O(2logn) and space = O(logn)

# class Solution:
#     def search(self, nums, target):

#         peak = self.peakIndex(nums)

#         if peak is not None and nums[peak] == target:
#             return peak 
        
#         # For non-rotated sorted arrays
#         if peak is None or peak == len(nums) - 1:
#             return self.binarySearch(0, len(nums) - 1, nums, target)
        
#         # For rotated sorted arrays, Search left or right 
#         if nums[0] <= target <= nums[peak - 1]:
#             # Search left 
#             return self.binarySearch(0, peak - 1, nums, target)
#         # Search right
#         return self.binarySearch(peak + 1, len(nums) - 1, nums, target)
    
#     def peakIndex(self, nums):

#         l, r = 0, len(nums) - 1 
#         lastIdx = r

#         if nums[l] < nums[r]:
#             return r 
        
#         while l <= r:

#             mid = (l + r) // 2 
#             # Find peak
#             if nums[mid - 1] < nums[mid] > nums[mid + 1]:
#                 return mid 
#             elif nums[mid] < nums[lastIdx]:
#                 r = mid - 1 
#             else:
#                 l = mid + 1 

#     def binarySearch(self, l, r, nums, target):

#         while l <= r:

#             mid = (l + r) // 2 

#             if target > nums[mid]:
#                 l = mid + 1 
#             elif target < nums[mid]:
#                 r = mid - 1 
#             else:
#                 return mid 
            
#         return -1

solution = Solution()
print(solution.search(nums1, target1))
print(solution.search(nums2, target2))
print(solution.search(nums3, target3))