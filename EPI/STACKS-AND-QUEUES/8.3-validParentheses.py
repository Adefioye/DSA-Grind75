class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for char in s:

            if char in bracketMap.values():
                stack.append(char)
            else:

                if len(stack) == 0:
                    return False

                openBracket = stack.pop()

                if openBracket != bracketMap[char]:
                    return False 

        return True if len(stack) == 0 else False