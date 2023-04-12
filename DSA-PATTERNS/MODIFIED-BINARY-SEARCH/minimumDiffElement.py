nums1 = [4, 6, 10]; key1 = 7
# Output: 6 
nums2 = [4, 6, 10]; key2 = 4
# Output: 4
nums3 = [1, 3, 8, 10, 15]; key3 = 12
# Output: 10
nums4 = [4, 6, 10]; key4 = 17
# Output: 10

def minDiffElement(nums, key):

    # if key less than smallest element, return first element
    if key < nums[0]:
        return nums[0]
    
    # if key greater than last element in array, return last element
    if key > nums[-1]:
        return nums[-1]
    
    # Otherwise its in between
    # Since diff is in absolute values,
    # if key is found in array return it,

    l, r = 0, len(nums) - 1 

    while l <= r:

        mid = (l + r) // 2 

        if key < nums[mid]:
            r = mid - 1 
        elif key > nums[mid]:
            l = mid + 1 
        else:
            return nums[mid] 
        
    # array is split in 2, left < key, right > key 
    if abs(key - nums[l]) <= abs(key - nums[r]):
        return nums[l]
    
    return nums[r]

print(minDiffElement(nums1, key1))
print(minDiffElement(nums2, key2))
print(minDiffElement(nums3, key3))
print(minDiffElement(nums4, key4))
