
def searchEntryEqualToItsIndex(arr):

    l, r = 0, len(arr) - 1

    while l <= r:

        mid = int(l + ((r - l) / 2))
        diff = arr[mid] - mid 

        if diff == 0:
            return mid 
        elif diff > 0:
            # No elemnt on the right can have a diff = 0 so we move left
            r = mid - 1 
        else:
            l = mid + 1

    return -1 

arr = [-2, 0, 2, 3, 6, 7, 9]
print(searchEntryEqualToItsIndex(arr))

