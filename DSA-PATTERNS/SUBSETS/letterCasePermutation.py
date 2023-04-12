s1 = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
s2 = "3z4"
# Output: ["3z4","3Z4"]

# time: n * 2^n ; space: 2^n
def letterCasePermutation(s):

    res = []

    def dfs(i, path):

        if len(path) == len(s):
            res.append(path)
            return 
        
        curChar = s[i]

        if curChar.isalpha():
            dfs(i + 1, path + curChar.lower())
            dfs(i + 1, path + curChar.upper())
        else:
            dfs(i + 1, path + curChar)

    dfs(0, "")

    return res 

print(letterCasePermutation(s1))
print(letterCasePermutation(s2))
