nums1 = [2,7,11,15]; target1 = 9  # [0, 1]
nums2 = [3,2,4]; target2 = 6      # [1, 2]
nums3 = [3,3]; target3 = 6        # [0, 1]

def twoSum(nums, target):

    prevMap = {}

    for i, num in enumerate(nums):

        diff = target - num 

        if diff not in prevMap:
            prevMap[num] = i 
        else:
            return [prevMap[diff], i]


print(twoSum(nums1, target1))
print(twoSum(nums2, target2))
print(twoSum(nums3, target3))



