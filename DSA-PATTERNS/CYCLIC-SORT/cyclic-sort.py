A1 = [3, 1, 5, 4, 2]    #   [1, 2, 3, 4, 5]
A2 = [2, 6, 4, 3, 1, 5] #   [1, 2, 3, 4, 5, 6]
A3 = [1, 5, 6, 4, 3, 2] #   [1, 2, 3, 4, 5, 6]

def cyclicSort(A):

    i = 0

    while i < len(A):

        if A[i] != i + 1:
            # Put the number in current index to its right spot
            newSpot = A[i] - 1
            # Swap the value in this index to value in the newSpot
            A[i], A[newSpot] = A[newSpot], A[i]
        else:
            i += 1
    
    return A

print(cyclicSort(A1))
print(cyclicSort(A2))
print(cyclicSort(A3))