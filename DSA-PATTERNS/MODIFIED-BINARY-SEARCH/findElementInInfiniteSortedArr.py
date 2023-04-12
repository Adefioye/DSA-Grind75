nums1 = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]; key1 = 16
# Output: 6
nums2 = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]; key2 = 11
# Output: -1
nums3 = [1, 3, 8, 10, 15]; key3 = 15
# Output: 4
nums4 = [1, 3, 8, 10, 15]; key4 = 200
# Output: -1

class ArrayReader:

    def __init__(self, arr):
        self.arr = arr 

    def get(self, index):

        if index >= len(self.arr):
            return float("inf")
        return self.arr[index] 
    
    
def binarySearch(reader, key, start, end):

    while start <= end:

        mid = (start + end) // 2 

        if key < reader.get(mid):
            end = mid - 1 
        elif key > reader.get(mid):
            start = mid + 1 
        else:
            return mid 
        
    return -1 

def findElementInInfiniteSortedArray(reader, key):

    start, end = 0, 1 

    while key > reader.get(end):
        start = end 
        end = 2 * end

    return binarySearch(reader, key, start, end)


print(findElementInInfiniteSortedArray(ArrayReader(nums1), key1))
print(findElementInInfiniteSortedArray(ArrayReader(nums2), key2))
print(findElementInInfiniteSortedArray(ArrayReader(nums3), key3))
print(findElementInInfiniteSortedArray(ArrayReader(nums4), key4))
