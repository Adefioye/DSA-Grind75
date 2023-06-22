
def letterCombinations(digits):
    numToChars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    res = [] 

    def df(i, path):

        if i == len(digits):
            res.append(path)
            return 

        for c in numToChars[digits[i]]:
            df(i + 1, path + c)

    if not digits:
        return res
            
    df(0, "")

    return res