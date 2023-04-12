nums1 = [3, 4, 4, 5, 5]         #`[4, 5]
nums2 = [5, 4, 7, 2, 3, 5, 3]   # [3, 5]

def findAllDuplicates(nums):

    minNum = min(nums)
    i = 0

    while i < len(nums):
        newSpot = nums[i] - minNum
        
        if nums[i] != i + minNum and nums[newSpot] != newSpot + minNum:
            nums[i], nums[newSpot] = nums[newSpot], nums[i]
        else:
            i += 1

    duplicates = []        

    for i in range(len(nums)):

        if nums[i] != i + minNum:
            duplicates.append(nums[i])

    return duplicates 


print(findAllDuplicates(nums1))
print(findAllDuplicates(nums2))