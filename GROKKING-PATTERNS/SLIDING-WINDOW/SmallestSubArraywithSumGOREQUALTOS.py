array1 = [2, 1, 5, 2, 3, 2]
S1 = 7
array2 = [2, 1, 5, 2, 8]
S2 = 7
array3 = [3, 4, 1, 1, 6]
S3 = 8 

# Brute force O(n^2)
def BruteSmallestSubArrayWithSumGreaterOrEqualToS(A, S):
    minL = float("inf")

    for left in range(len(A)):
        curSum = 0

        for right in range(left, len(A)):
            curSum += A[right]

            if curSum >= S:
                curL = right - left + 1
                minL = min(curL, minL)

    return minL if minL != float("inf") else 0 

print("Brute force Solution")
print(BruteSmallestSubArrayWithSumGreaterOrEqualToS(array1, S1))
print(BruteSmallestSubArrayWithSumGreaterOrEqualToS(array2, S2))
print(BruteSmallestSubArrayWithSumGreaterOrEqualToS(array3, S3))

def OptimalSmallestSubArrayWithSumGreaterOrEqualToS(A, S):
    minL = float("inf")
    left = 0
    right = 0
    while right < len(A):

        windowSum = sum(A[left : right + 1])

        if windowSum >= S:

            curL = right - left + 1 
            minL = min(curL, minL)

            if windowSum == S:
                right += 1
            else:
                left += 1 

        else:
            right += 1

    return minL if minL != float("inf") else 0


print("Optimal solution")
print(OptimalSmallestSubArrayWithSumGreaterOrEqualToS(array1, S1))
print(OptimalSmallestSubArrayWithSumGreaterOrEqualToS(array2, S2))
print(OptimalSmallestSubArrayWithSumGreaterOrEqualToS(array3, S3))