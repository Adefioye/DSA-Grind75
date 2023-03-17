nums1 = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums2 = [0]
# Output: [[],[0]]

def subsets(nums):

    if len(nums) == 0:
        return [ [] ]
    
    first = nums[0]
    rest = nums[1:]
    combsWithoutFirst = subsets(rest)
    combsWithFirst = []

    for item in combsWithoutFirst:
        combWithFirst = [*item, first]
        combsWithFirst.append(combWithFirst)

    return [*combsWithFirst, *combsWithoutFirst]

print(subsets(nums1))
print(subsets(nums2))