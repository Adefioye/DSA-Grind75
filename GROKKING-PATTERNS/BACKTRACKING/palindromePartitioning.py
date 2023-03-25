s1 = "aab"
# Output: [["a","a","b"],["aa","b"]]
s2 = "a"
# Output: [["a"]]
s3 = "efe"
# Output: [["e", "f", "e"], ["efe"]]

def palindromePartitioning(s):

    res = []
    comb = []

    def backtrack(s):

        if len(s) == 0:
            res.append(comb[:])
            return 
        
        for i in range(len(s)):
            curSubString = s[:i + 1]
            rest = s[i + 1:]

            if isPalindrome(curSubString):
                comb.append(curSubString)
                backtrack(rest)
                comb.pop()

    backtrack(s)

    return res

def isPalindrome(s):

    l = 0
    r = len(s) - 1

    while l <= r:

        if s[l] != s[r]:
            return False 
        
        l += 1 
        r -= 1

    return True

print(palindromePartitioning(s1))
print(palindromePartitioning(s2))
print(palindromePartitioning(s3))