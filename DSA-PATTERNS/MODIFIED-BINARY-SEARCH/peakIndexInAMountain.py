arr1 = [0,1,0]
# Output: 1
arr2 = [0,2,1,0]
# Output: 1
arr3 = [1, 2, 3, 4, 9, 8, 7, 6, 5]
# Output: 4
arr4 = [3,5,3,2,0]
# Output: 1

def peakIndexInAMountain(arr):
    # Ignore extremes since they cannot be answer
    l, r = 1, len(arr) - 2

    while l <= r:
        mid = (l + r) // 2

        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid 
        elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
            l = mid + 1 
        else:
            r = mid - 1

print(peakIndexInAMountain(arr1))
print(peakIndexInAMountain(arr2))
print(peakIndexInAMountain(arr3))
print(peakIndexInAMountain(arr4))