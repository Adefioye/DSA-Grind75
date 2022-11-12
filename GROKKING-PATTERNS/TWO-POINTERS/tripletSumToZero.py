from typing import List

A1 = [-3, 0, 1, 2, -1, 1, -2]
# [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
A2 = [-5, 2, -1, -2, 3]
# [[-5, 2, 3], [-2, -1, 3]]

# Brute force O(n^2)
def bruteTripletSumToZero(array):
    res = []
    for i in range(len(array)):
       for j in range(i+1, len(array)):
        for k in range(j+1, len(array)):
            threeSum = array[i] + array[j] + array[k]
            
            ls = [array[i], array[j], array[k]]
            listPresent = False 

            for item in res:
                if set(ls) == set(item):
                    listPresent = True

            if threeSum == 0 and not listPresent:
                res.append(ls)

    return res 

print(bruteTripletSumToZero(A1))
print(bruteTripletSumToZero(A2))

print("OPTIMAL SOLUTION")
print("++++++++++++++++++++++++++")
def optimalTripleSumToZero(array):

    res = []
    array.sort()

    for i, num in enumerate(array):

        if i > 0 and array[i] == array[i - 1]:
                continue 

        l = i + 1
        r = len(array) - 1 

        while l < r:

            threeSum = num + array[l] + array[r]

            if threeSum > 0:
                r -= 1 
            elif threeSum < 0: 
                l += 1 
            else:
                res.append([num, array[l], array[r]])
                l += 1 

                if array[l] == array[l - 1] and l < r:
                    l += 1

    return res 

print(optimalTripleSumToZero(A1))
print(optimalTripleSumToZero(A2))