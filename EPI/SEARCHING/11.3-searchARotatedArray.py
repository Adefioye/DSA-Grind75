A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]

# This works only when values in the array are distinct
def searchMinimumInSortedArray(arr):

    l, r = 0, len(arr) - 1 

    while l < r:

        mid = l + ((r - l) // 2)

        if arr[mid] > arr[r]:
            # HEnce min is to the right, arr[mid + 1, r+1]
            l = mid + 1
        else:
            r = mid

    return l 

print(searchMinimumInSortedArray(A))
