n1 = 4; k1 = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
n2 = 1; k2 = 1
# Output: [[1]]



def combinations(n, k):

    res = []
    perm = []

    def backtrack(start):

        if len(perm) == k:
            res.append(perm[:])
            return 
        
        for i in range(start, n + 1):
            perm.append(i)

            backtrack(i + 1)

            perm.pop()

    backtrack(1)

    return res

print(combinations(n1, k1))
print(combinations(n2, k2))