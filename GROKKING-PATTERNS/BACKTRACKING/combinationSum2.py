candidates1 = [10,1,2,7,6,1,5]; target1 = 8
#[[1,1,6],[1,2,5],[1,7],[2,6]]
candidates2 = [2,5,2,1,2]; target2 = 5
#[[1,2,2],[5]]

def combinationSum2(candidates, target):

    res = []
    comb = []

    candidates.sort()

    def backtrack(start, total):

        if total == target:
            res.append(comb[:])
            return 
        
        if total > target:
            return 
        
        prev = float("inf")

        for i in range(start, len(candidates)):
            
            if candidates[i] == prev:
                continue
            comb.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            comb.pop()
            prev = candidates[i]

    backtrack(0, 0)

    return res

print(combinationSum2(candidates1, target1))
print(combinationSum2(candidates2, target2))