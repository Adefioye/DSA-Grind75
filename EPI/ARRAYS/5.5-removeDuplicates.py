nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums) -> int:

    if len(nums) == 1:
        return 1

    i = 1
    l = 1

    while i < len(nums):

        if nums[i - 1] == nums[i]:
            i += 1 
        else:
            nums[l] = nums[i]
            l += 1 
            i += 1 

    return l


print(removeDuplicates(nums1))
print(removeDuplicates(nums2))