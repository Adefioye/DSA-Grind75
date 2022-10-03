S1 ="araaci"; K1=2   # 4
S2 ="araaci"; K2=1   # 2
S3 ="cbbebi"; K3=3   # 3

# Brute force solution t = (O^2); s = O(n)
def BruteLongestSubStringWithKChars(S, K):
    maxL = float("-inf")

    for left in range(len(S)):
        char_map = {}

        for right in range(left, len(S)):
            cur_char = S[right]

            if cur_char not in char_map:
                char_map[cur_char] = 1
            else:
                char_map[cur_char] = char_map.get(cur_char) + 1

            if len(char_map.keys()) == K:
                maxL = max(maxL, right - left + 1)
            elif len(char_map.keys()) > K:
                break;

    return maxL if maxL != float("-inf") else 0

print("Brute force solution")
print(BruteLongestSubStringWithKChars(S1, K1))
print(BruteLongestSubStringWithKChars(S2, K2))
print(BruteLongestSubStringWithKChars(S3, K3))

# Optimal solution t = O(n) s = O(n)

def OptimalLongestSubstringWithKChars(S, K):
    maxL = float("-inf")
    char_map = {}
    left = 0

    for right in range(len(S)):
        cur_char = S[right]

        if cur_char not in char_map:
            char_map[cur_char] = 1
        else:
            char_map[cur_char] = char_map.get(cur_char) + 1

        if len(char_map.keys()) == K:
            maxL = max(maxL, right - left + 1)
        elif len(char_map.keys()) > K:
            char_map = {}
            char_map[cur_char] = 1
            left = right 
    
    return maxL if maxL != float("-inf") else 0

print("Optimal Solution")
print(OptimalLongestSubstringWithKChars(S1, K1))
print(OptimalLongestSubstringWithKChars(S2, K2))
print(OptimalLongestSubstringWithKChars(S3, K3))


