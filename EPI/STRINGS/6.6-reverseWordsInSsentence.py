s1 = "Alice likes Bob"

def reverseWords(str: str) -> str:
        # write your code here

    s = list(str)

    s.reverse()

    def reverse_range(s, l, r):

        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1 

    start = 0

    while True:
        try:
            end = s.index(' ', start)
            reverse_range(s, start, end - 1)
            start = end + 1
        except:
            break
            
        # Reverse final word 
    reverse_range(s, start, len(s) - 1)
    return "".join(s)

print(reverseWords(s1))


# def reverseWordsInSentence(s):

#     finalRes = ""
#     curRes = ""
#     for i in range(len(s) - 1, -1, -1):

#         if s[i] != " ":
#             curRes += s[i]
#         else:
#             finalRes += (curRes[::-1] + s[i])
#             curRes = ""

    
#     finalRes += curRes[::-1]

#     return finalRes 