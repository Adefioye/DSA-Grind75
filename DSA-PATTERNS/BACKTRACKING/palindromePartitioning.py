s1 = "aab"
# Output: [["a","a","b"],["aa","b"]]
s2 = "a"
# Output: [["a"]]
s3 = "efe"
# Output: [["e", "f", "e"], ["efe"]]

## SECOND SOLUTION

def palindromePartitioning(s):

    res = []
    part = []

    def dfs(i):

        if i >= len(s):
            res.append(part[:])
            return 
        
        for j in range(i, len(s)):
            if isPalindrome(s, i, j):
                part.append(s[i : j + 1])
                dfs(j + 1)
                part.pop()

    dfs(0)

    return res

def isPalindrome(s, l, r):

    while l <= r:

        if s[l] != s[r]:
            return False 
        
        l += 1 
        r -= 1

    return True

print(palindromePartitioning(s1))
print(palindromePartitioning(s2))
print(palindromePartitioning(s3))

## FIRST SOLUTION
# def palindromePartitioning(s):

#     res = []
#     comb = []

#     def backtrack(s):

#         if len(s) == 0:
#             res.append(comb[:])
#             return 
        
#         for i in range(len(s)):
#             curSubString = s[:i + 1]
#             rest = s[i + 1:]

#             if isPalindrome(curSubString):
#                 comb.append(curSubString)
#                 backtrack(rest)
#                 comb.pop()

#     backtrack(s)

#     return res
