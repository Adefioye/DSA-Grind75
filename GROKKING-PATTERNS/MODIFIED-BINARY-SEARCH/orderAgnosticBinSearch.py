nums1 = [4, 6, 10]; key1 = 10
# Output: 2
nums2 = [1, 2, 3, 4, 5, 6, 7]; key2 = 5
# Output: 4
nums3 = [10, 6, 4]; key3 = 10
# Output: 0
nums4 = [10, 6, 4]; key4 = 4
# Output: 2



def orderAgnosticBinSearch(nums, target):

    l = 0 
    r = len(nums) - 1 

    while l <= r:

        mid = (l + r) // 2
        if target > nums[mid]:
            # Maybe go left or right 
            temp = mid + 1 
            while nums[mid] == nums[temp]:
                temp += 1 

            if nums[temp] > nums[mid]:
                # It means target is to right
                l = mid + 1
            else:
                # target is to left
                r = mid - 1
        elif target < nums[mid]:
            # Maybe go left or right 
            temp = mid - 1 
            while nums[mid] == nums[temp]:
                temp -= 1 

            if nums[temp] < nums[mid]:
                # It means target is to left
                r = mid - 1
            else:
                # target is to right
                l = mid + 1
        else:
            return mid 
        
    return -1

print(orderAgnosticBinSearch(nums1, key1))
print(orderAgnosticBinSearch(nums2, key2))
print(orderAgnosticBinSearch(nums3, key3))
print(orderAgnosticBinSearch(nums4, key4))


