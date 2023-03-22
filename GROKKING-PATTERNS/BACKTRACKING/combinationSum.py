candidates1 = [2,3,6,7]; target1 = 7
# Output: [[2,2,3],[7]]
candidates2 = [2,3,5]; target2 = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
candidates3 = [2]; target3 = 1
# Output: []

def combinationSum(candidates, target):

    res = []
    comb = []

    def backtrack(i, comb, total):

        if total == target:
            res.append(comb[:])
            return 
        
        if i >= len(candidates) or total > target:
            return 
        
        comb.append(candidates[i])
        backtrack(i, comb, total + candidates[i])
        
        comb.pop()
        backtrack(i + 1, comb, total)

    backtrack(0, [], 0)

    return res


print(combinationSum(candidates1, target1))
print(combinationSum(candidates2, target2))
print(combinationSum(candidates3, target3))

## FIRST BACKTRACKING SOLUTION
# def combinationSum(candidates, target):
    
#     res = []
#     comb = []

#     def backtrack(start):
        
#         if sum(comb) > target:
#             return 
    
#         if sum(comb) == target:
#             res.append(comb[:])
#             return 
    
#         for i in range(start, len(candidates)):
#             comb.append(candidates[i])

#             backtrack(i)

#             comb.pop()

#     backtrack(0)

#     return res
