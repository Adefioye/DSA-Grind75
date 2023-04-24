nums1 = [1,1,2]
# Output:[[1,1,2], [1,2,1], [2,1,1]]
nums2 = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def uniquePermutations(nums):

    res = []
    nums.sort()

    def dfs(arr, path):

        if len(arr) == 0:
            res.append(path)
            return 
        
        for i in range(len(arr)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            dfs(arr[:i] + arr[i + 1:], path + [arr[i]])
    
    dfs(nums, [])

    return res

print(uniquePermutations(nums1))
print(uniquePermutations(nums2))


# BEATS 99% of solution BACKTRACKING SOLUTION WITH HEASHMAP
# def uniquePermutations(nums):

#     res = []
#     perm = []
#     count = {}

#     for num in nums:
#         if num not in count:
#             count[num] = 0 
#         count[num] += 1

#     def backtrack():

#         if len(perm) == len(nums):
#             res.append(perm[:])
#             return
        
#         for key in count:

#             if count[key] > 0:
#                 perm.append(key)
#                 count[key] -= 1

#                 backtrack()

#                 perm.pop()
#                 count[key] += 1

#     backtrack()

#     return res

# def uniquePermutations(nums):
#     res = []

#     def backtrack(nums, path):

#         if len(nums) == 0:
#             if path not in res:
#                 res.append(path)

#         for i in range(len(nums)):
#             backtrack(nums[:i] + nums[i+1:], path + [nums[i]])

#     backtrack(nums, [])

#     return res


# NON_BACKTRACKING SOLUTION

# def uniquePermutations(nums):

#     allPerms = permutations(nums)
#     res = []

#     for item in allPerms:
#         if item not in res:
#             res.append(item)

#     return res

# def permutations(nums):

#     if len(nums) == 0:
#         return [[]]
    
#     first = nums[0]
#     rest = nums[1:]
#     permsWithoutFirst = permutations(rest)
#     allPermutations = []

#     for i, item in enumerate(permsWithoutFirst):

#         for i in range(len(item) + 1):
#             permWithFirst = [*item[:i], first, *item[i:]]
#             allPermutations.append(permWithFirst)

#     return allPermutations

