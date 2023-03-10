s1 = "a1b2"
#Output: ["a1b2","a1B2","A1b2","A1B2"]
s2 = "3z4"
#Output: ["3z4","3Z4"]

def letterCasePermutation(chars):

    outputs = [""]

    for char in chars:
        temp = []

        if char.isalpha():

            for output in outputs:
                temp.append(output + char.lower())
                temp.append(output + char.upper())
        else:
            for output in outputs:
                temp.append(output + char)

        outputs = temp 

    return outputs

print(letterCasePermutation(s1))
print(letterCasePermutation(s2))

# def letterCasePermutation(chars: str):

#     if len(chars) == 0:
#         return [""]
    
#     firstChar = chars[0]
#     rest = chars[1:]

#     permsWithoutFirst = letterCasePermutation(rest)
#     allPermutations = []

#     if firstChar.isalpha():
#         # Its a character 
#         for item in permsWithoutFirst:
#             allPermutations.append(firstChar.lower() + item)
#             allPermutations.append(firstChar.upper() + item)
#     else:
#         for item in permsWithoutFirst:
#             allPermutations.append(firstChar + item)


#     return allPermutations 
