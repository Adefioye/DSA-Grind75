A1 = [2, 3, 1, 8, 2, 3, 5, 1]   #  4, 6, 7
A2 = [2, 4, 1, 2]               #  3
A3 = [2, 3, 2, 1]               #  4

def find_missing_nums(A):
    missingNums = []
    i = 0

    # Sort using cyclical sort
    while i < len(A):
        newSpot = A[i] - 1

        if A[i] != i + 1 and A[newSpot] != newSpot + 1:
            A[i], A[newSpot] = A[newSpot], A[i]
        else:
            i += 1

    # After sorting, Iterate and add numbers not equal to A[i] != i

    for i, num in enumerate(A):
        if i + 1 != num:
            missingNums.append(i + 1)
    
    return missingNums

print(find_missing_nums(A1))
print(find_missing_nums(A2))
print(find_missing_nums(A3))