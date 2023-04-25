k1 = 3; n1 = 7
# Output: [[1,2,4]]
k2 = 3; n2 = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
k3 = 4; n3 = 1
# Output: []

def combinationSum3(k, n):

    res = []
    comb = []
    def dfs(i, total):

        if total == n and len(comb) == k:
            res.append(comb[:])
            return 

        if i > 9:
            return

        # Decision to include i
        comb.append(i)
        dfs(i + 1, total + i)

        # Decision not to include i
        comb.pop()
        dfs(i + 1, total)

    dfs(1, 0)

    return res

## FIRST SOLUTION
# def combinationSum3(k, n):

#     res = []
#     comb = []

#     def backtrack(start, total):

#         if len(comb) == k and total == n:
#             res.append(comb[:])
#             return 
        
#         if len(comb) > k or total > n or (len(comb) == k and total < n):
#             return 
        
#         for i in range(start, 10):
#             comb.append(i)
#             backtrack(i + 1, total + i)
#             comb.pop() 

#     backtrack(1, 0)

#     return res 

print(combinationSum3(k1, n1))
print(combinationSum3(k2, n2))
print(combinationSum3(k3, n3))