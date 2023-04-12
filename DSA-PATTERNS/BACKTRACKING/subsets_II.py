

nums1 = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
nums2 = [0]
# Output: [[],[0]]

def subsets_II(nums):

    nums.sort()

    powerSet = [[]]

    for num in nums:
        temps = [*powerSet]

        for temp in temps:
            setToAdd = temp + [num]

            if setToAdd not in powerSet:
                powerSet.append(setToAdd)

    return powerSet 

print(subsets_II(nums1))
print(subsets_II(nums2))