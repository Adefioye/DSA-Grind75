nums1 = [1,1,2]
# Output:[[1,1,2], [1,2,1], [2,1,1]]
nums2 = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]



def uniquePermutations(nums):

    allPerms = permutations(nums)
    res = []

    for item in allPerms:
        if item not in res:
            res.append(item)

    return res

def permutations(nums):

    if len(nums) == 0:
        return [[]]
    
    first = nums[0]
    rest = nums[1:]
    permsWithoutFirst = permutations(rest)
    allPermutations = []

    for i, item in enumerate(permsWithoutFirst):

        for i in range(len(item) + 1):
            permWithFirst = [*item[:i], first, *item[i:]]
            allPermutations.append(permWithFirst)

    return allPermutations

print(uniquePermutations(nums1))
print(uniquePermutations(nums2))