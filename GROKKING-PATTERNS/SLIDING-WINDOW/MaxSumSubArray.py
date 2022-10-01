array1 = [2, 1, 5, 1, 3, 2]
k1 = 3
array2 = [2, 3, 4, 1, 5]
k2 = 2 

def maxSumSubArray(array, k):
    maxSum = 0
    newSum = 0
    for i in range(len(array)):
        lastWindowIndex = i + k - 1

        newSum = sum(array[i:lastWindowIndex + 1])
        maxSum = max(newSum, maxSum)

    return maxSum;

def maxSumSubArray1(array, k):

    left = 0
    right = 0
    maxSum = 0
    currentSum = 0

    while right < len(array):
        currentSum += array[right]

        if right >= k - 1:
            maxSum = max(currentSum, maxSum)
            currentSum -= array[left]
            left += 1

        right += 1

    return maxSum


print(maxSumSubArray(array1, k1)) # 9
print(maxSumSubArray(array2, k2))  # 7

print("Using left and right pointer")
print(maxSumSubArray1(array1, k1)) # 9
print(maxSumSubArray1(array2, k2))