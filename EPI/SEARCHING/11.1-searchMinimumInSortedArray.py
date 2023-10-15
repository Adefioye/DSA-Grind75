
def searchFirstOccurenceOfKInSortedArray(arr, k):

    l, r = 0, len(arr) - 1 

    while l <= r:

        mid = int(l + ((r - l) / 2))

        if k <= arr[mid]:
            r = mid - 1
        else:
            l = mid + 1 

    if l >= 0 and l <= len(arr) - 1 and arr[l] == k:
        return l 
    
    return -1
a = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
print(searchFirstOccurenceOfKInSortedArray(a, 108))
print(searchFirstOccurenceOfKInSortedArray(a, 285))
print(searchFirstOccurenceOfKInSortedArray(a, 2))
print(searchFirstOccurenceOfKInSortedArray(a, 401))
print(searchFirstOccurenceOfKInSortedArray(a, 4))
