S1 = "aabccbb"  # 3
S2 = "abbbb"    # 2
S3 = "abccde"   # 3

# def longestSubStringWithKDistinctChar(S):
#     maxL = float("-inf")
#     left = 0 
#     char_map = {}

#     for right in range(len(S)):

#         cur_char = S[right]
#         if cur_char not in char_map:
#             char_map[cur_char] = 1
#         else:
#             char_map = {}
#             char_map[cur_char] = 1
#             left = right 

#         maxL = max(maxL, right - left + 1)

#     return maxL if maxL != float("-inf") else 0 

def longestSubStringWithDistinctChar(S):

    maxL = float("-inf")
    left = 0
    right = 0
    char_map = {}

    for right in range(len(S)):

        cur_char = S[right]

        while cur_char in char_map:
            del char_map[S[left]]
            left += 1

        char_map[cur_char] = right

        maxL = max(maxL, right - left + 1)

    return maxL if maxL != float("-inf") else 0 

print(longestSubStringWithDistinctChar(S1))
print(longestSubStringWithDistinctChar(S2))
print(longestSubStringWithDistinctChar(S3))

