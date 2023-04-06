nums1 = [4, 6, 10]; key1 = 6
# Output: 1
nums2 = [1, 3, 8, 10, 15]; key2 = 12
# Output: 4
nums3 = [4, 6, 10]; key3 = 17
# Output: -1
nums4 = [4, 6, 10]; key4 = -1
# Output: 0

def ceilingOfANumber(nums, key):
    """
    The ceiling of a number is smallest number >= key
    if present, return its index, otherwise return -1
    """
    l, r = 0, len(nums) - 1 

    if key > nums[r]:
        return -1 
    if key <= nums[l]:
        return 0 
    
    while l <= r:
        
        mid = (l + r) // 2 

        if key > nums[mid]:
            l = mid + 1 
        elif key < nums[mid]:
            r = mid - 1 
        else:
            return mid 
        
    return l 

print(ceilingOfANumber(nums1, key1))
print(ceilingOfANumber(nums2, key2))
print(ceilingOfANumber(nums3, key3))
print(ceilingOfANumber(nums4, key4))
