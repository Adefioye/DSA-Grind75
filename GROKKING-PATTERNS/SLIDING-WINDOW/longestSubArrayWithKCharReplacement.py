S1="aabccbb"; k1=2   # 5
S2="abbcb"; k2=1     # 4
S3="abccde"; k3=1    # 3


def characterReplacement(string, k):

    left = 0
    fMap = {}
    maxL = 0

    for right in range(len(string)):
        curChar = string[right]

        if curChar not in fMap:
            fMap[curChar] = 0
        fMap[curChar] += 1


        while ((right - left + 1) - max(fMap.values())) > k:
            fMap[string[left]] -= 1 
            left += 1
        
        maxL = max(maxL, right - left + 1)


    return maxL

print(characterReplacement(S1, k1))
print(characterReplacement(S2, k2))
print(characterReplacement(S3, k3))
