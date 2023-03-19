nums1 = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
nums2 = [0,1]
# Output: [[0,1],[1,0]]
nums3 = [1]
# Output: [[1]]

def permutation(nums):

    if len(nums) == 0:
        return [[]]
    
    first = nums[0]
    rest = nums[1:]
    permsWithoutFirst = permutation(rest)
    allPermutations = []

    for i, item in enumerate(permsWithoutFirst):

        for i in range(len(item) + 1):
            permWithFirst = [*item[:i], first, *item[i:]]
            allPermutations.append(permWithFirst)

    return allPermutations

print(permutation(nums1))
print(permutation(nums2))
print(permutation(nums3))