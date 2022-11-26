A1=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]; k1=2          #6
A2=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]; k2=3     #9

def OnesReplacement(array, k):

    left = 0 
    numOfOnes = 0
    maxL = 0

    for right in range(len(array)):
        curNum = array[right]

        if curNum == 1:
            numOfOnes += 1

        while (right - left + 1) - numOfOnes > k:
            if array[left] == 1:
                numOfOnes -= 1
            left += 1 
        
        maxL = max(maxL, right - left + 1)
        # print(left, right, maxL, fMap)

    return maxL

print(OnesReplacement(A1, k1))
print(OnesReplacement(A2, k2))
