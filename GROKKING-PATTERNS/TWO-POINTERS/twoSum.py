nums1 = [2,7,11,15]; target1 = 9  # [0, 1]
nums2 = [3,2,4]; target2 = 6      # [1, 2]
nums3 = [3,3]; target3 = 6        # [0, 1]

def twoSum(nums, target):

    numMap = {}

    for i, num in enumerate(nums):

        if num in numMap:
            return [numMap[num], i]
        
        diff = target - num 
        numMap[diff] = i

print(twoSum(nums1, target1))
print(twoSum(nums2, target2))
print(twoSum(nums3, target3))



