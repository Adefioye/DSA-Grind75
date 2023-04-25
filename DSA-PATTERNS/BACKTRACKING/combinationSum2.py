candidates1 = [10,1,2,7,6,1,5]; target1 = 8
#[[1,1,6],[1,2,5],[1,7],[2,6]]
candidates2 = [2,5,2,1,2]; target2 = 5
#[[1,2,2],[5]]

## SOLUTION 2 (Involving making just 2 decisions)

def combinationSum2(candidates, target):

    res = []
    comb = []
    candidates.sort()

    def dfs(i, total):

        if total == target:
            res.append(comb[:])
            return 
        
        if i >= len(candidates) or total > target:
            return 
        
        # Decision to include candidates[i]
        comb.append(candidates[i])
        dfs(i + 1, total + candidates[i])

        # Decision not to include candidates[i]
        comb.pop()

        while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
            i += 1
        dfs(i + 1, total)

    dfs(0, 0)

    return res

print(combinationSum2(candidates1, target1))
print(combinationSum2(candidates2, target2))

## SOLUTION 1
# def combinationSum2(candidates, target):

#     res = []
#     comb = []

#     candidates.sort()

#     def backtrack(start, total):

#         if total == target:
#             res.append(comb[:])
#             return 
        
#         if total > target:
#             return 
        
#         prev = float("inf")

#         for i in range(start, len(candidates)):
            
#             if candidates[i] == prev:
#                 continue
#             comb.append(candidates[i])
#             backtrack(i + 1, total + candidates[i])
#             comb.pop()
#             prev = candidates[i]

#     backtrack(0, 0)

#     return res