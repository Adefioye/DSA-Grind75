def isValid(s: str) -> bool:
    parentheses = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
    stack = []
        
    for i in range(len(s)):
        curr_char = s[i]
            
        if curr_char in parentheses:
                stack.append(curr_char)
        else:

            if len(stack) == 0:
                return False 
            
            last_open_bracket = stack.pop()
            matching_pair = parentheses[last_open_bracket]

            if curr_char != matching_pair:
                return False
                
    return True if len(stack) == 0 else False 

s1 = "()"
s2 = "()[]{}"
s3 = "(]"

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))