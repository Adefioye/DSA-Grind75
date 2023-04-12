A1 = [-1, 0, 2, 3]; T1=3    # 2 [-1, 0, 3], [-1, 0, 2]
A2 = [-1, 4, 2, 1, 3]; T2=5 # 4 [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
A3 = [-1, -1, 4, 2, 2, 1, 3]; T3=5


def tripleSumLessThanTarget(array, target):
    # result = []
    total = 0 

    array.sort()

    for i, num in enumerate(array):

        l = i + 1 
        r = len(array) - 1 

        while l < r:

            tripleSum = num + array[l] + array[r]

            if tripleSum < target:
                total += (r - l)
                l += 1
            else:
                r -= 1



    return total


print(tripleSumLessThanTarget(A1, T1))
print(tripleSumLessThanTarget(A2, T2))
print(tripleSumLessThanTarget(A3, T3))

