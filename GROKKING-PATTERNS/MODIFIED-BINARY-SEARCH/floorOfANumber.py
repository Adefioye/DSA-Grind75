nums1 = [4, 6, 10]; key1 = 6
# Output: 1
nums2 = [1, 3, 8, 10, 15]; key2 = 12
# Output: 3
nums3 = [4, 6, 10]; key3 = 17
# Output: 2
nums4 = [4, 6, 10]; key4 = -1
# Output: -1

def floorOfANumber(nums, key):
    """
    Floor of a key is greatest number <= key
    if present, return index, otherwise return -1
    """
    l, r = 0, len(nums) - 1 

    if key > nums[r]:
        return r 
    
    if key < nums[l]:
        return -1 
    
    while l <= r:
        
        mid = (l + r) // 2 

        if key > nums[mid]:
            l = mid + 1 
        elif key < nums[mid]:
            r = mid - 1 
        else:
            return mid
        
    return r

print(floorOfANumber(nums1, key1))
print(floorOfANumber(nums2, key2))
print(floorOfANumber(nums3, key3))
print(floorOfANumber(nums4, key4))