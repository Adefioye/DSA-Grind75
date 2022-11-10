from typing import List

A1 = [-2, -1, 0, 2, 3]  # [0, 1, 4, 4, 9]
A2 = [-3, -1, 0, 1, 2]  # [0 1 1 4 9]

def SquaringASortedArray(array: List[int]) -> List[int]:

    left = 0
    right = len(array) - 1 
    newArray = [0] * len(array)
    k = len(array) - 1 

    while left <= right:
        
        leftSquare = array[left] ** 2
        rightSquare = array[right] ** 2

        if leftSquare >= rightSquare:
            newArray[k] = leftSquare 
            left += 1 
            k -= 1 
        else:
            newArray[k] = rightSquare 
            right -= 1
            k -= 1

    return newArray 

print(SquaringASortedArray(A1))
print(SquaringASortedArray(A2))