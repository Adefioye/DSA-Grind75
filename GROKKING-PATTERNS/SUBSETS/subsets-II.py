def subsets2(nums):

    res = []
    subset = []

    # Sorting is important to keep track of duplicates
    nums.sort()

    def dfs(i):

        if i >= len(nums):
            res.append(subset[:])
            return 
        
        # Decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()

        # Decision not to include nums[i]
        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i += 1 
        dfs(i + 1) 
        
    dfs(0)

    return res 