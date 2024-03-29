A1 = [-2, 0, 1, 2]; t1=2        # 1
A2 = [-3, -1, 1, 2]; t2=1       # 0
A3 = [1, 0, 1, 1]; t3=100   # 3


def tripleSumCloseToTarget(array, target):

    minDiff = float("inf")
    minTripletSum = float("inf")

    array.sort()

    for i, num in enumerate(array):

        if i > 0 and array[i] == array[i - 1]:
            continue 

        l = i + 1
        r = len(array) - 1 

        while l < r:

            tripletSum = num + array[l] + array[r]
            diff = abs(target - tripletSum)
            
            if diff < minDiff:
                minDiff = diff 
                minTripletSum = tripletSum 
            elif diff == minDiff:
                minTripletSum = min(tripletSum, minTripletSum)

            if tripletSum < target:
                l += 1
            elif tripletSum > target:
                r -= 1
            else:
                l += 1

                while array[l - 1] == array[l] and l < r:
                    l += 1

    return minTripletSum

print(tripleSumCloseToTarget(A1, t1))
print(tripleSumCloseToTarget(A2, t2))
print(tripleSumCloseToTarget(A3, t3))
