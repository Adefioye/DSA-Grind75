from heapq import heapify, heappop, heappush

arr1 = [5,5,4]; k1 = 1
# Output: 1
arr2 = [4,3,1,1,3,3,2]; k2 = 3
# Output: 2
arr3 = [1]; k3 = 0
# Output: 1
def findLeastNumOfUniqueInts(nums, k):
    count = {}

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    minHeap = [[c, n] for n, c in count.items()]

    heapify(minHeap)
    counter = 0 

    while minHeap and counter < k:
        freq, num = heappop(minHeap)
        counter += 1 

        if freq > 1:
            heappush(minHeap, [freq - 1, num])
    
    return len(minHeap)

print(findLeastNumOfUniqueInts(arr1, k1))
print(findLeastNumOfUniqueInts(arr2, k2))
print(findLeastNumOfUniqueInts(arr3, k3))