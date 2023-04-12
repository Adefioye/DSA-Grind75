digits1 = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
digits2 = ""
# Output: []
digits3 = "2"
# Output: ["a","b","c"]

def letterCombinations(digits):

    res = []
    digitToCharMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
    
    def backtrack(i, comb):

        if len(comb) == len(digits):
            res.append(comb)
            return 
        
        for char in digitToCharMap[digits[i]]:
            backtrack(i + 1, comb + char)

    if digits:
        backtrack(0, "")

    return res 


print(letterCombinations(digits1))
print(letterCombinations(digits2))
print(letterCombinations(digits3))