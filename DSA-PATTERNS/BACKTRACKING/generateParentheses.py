n3 = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
n2 = 2
# Output: ["()()", "(())"]
n1 = 1
# Output: ["()"]

## SECOND SOLUTION
def generateParentheses(n):

    res = []

    def dfs(open, close, path):

        if open == close == n:
            res.append(path)
            return 
        
        if open == close or open < n:
            dfs(open + 1, close, path + "(")
        if open > close and close < n:
            dfs(open, close + 1, path + ")")

    dfs(0, 0, "")

    return res 

print(generateParentheses(n1))
print(generateParentheses(n2))
print(generateParentheses(n3))


## FIRST SOLUTION
# def generateParentheses(n):

#     res = []
#     comb = []
#     OPEN = "("
#     CLOSE = ")"

#     def backtrack(openCount, closeCount):

#         if openCount == closeCount == n:
#             res.append("".join(comb))
#             return 
        
#         if openCount < n:
#             comb.append(OPEN)
#             backtrack(openCount + 1, closeCount)
#             comb.pop()

#         if closeCount < openCount:
#             comb.append(CLOSE)
#             backtrack(openCount, closeCount + 1)
#             comb.pop()

#     backtrack(0, 0)

#     return res 
