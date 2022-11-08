A1=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]; k1=2          #6
A2=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]; k2=3     #9

def OnesReplacement(array, k):

    left = 0 
    fMap = {}
    maxL = 0

    for right in range(len(array)):
        curNum = array[right]

        if curNum == 1 and curNum not in fMap:
            fMap[curNum] = 0

        if curNum == 1:
            fMap[curNum] += 1

        while (right - left + 1) - fMap.get(1, 0) > k:
            if array[left] == 1:
                fMap[array[left]] -= 1
            left += 1 
        
        maxL = max(maxL, right - left + 1)
        # print(left, right, maxL, fMap)

    return maxL

print(OnesReplacement(A1, k1))
print(OnesReplacement(A2, k2))
