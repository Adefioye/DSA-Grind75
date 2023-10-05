from heapq import heappop, heappush

def sortKSortedArray(arr, k):

    minHeap = []
    res = []

    for item in arr:
        heappush(minHeap, item)

        if len(minHeap) > k:
            smallest = heappop(minHeap)
            res.append(smallest)

    while minHeap:
        smallest = heappop(minHeap)
        res.append(smallest)

    return res

arr1, k1 = [3, -1, 2, 6, 4, 5, 8], 2
print(sortKSortedArray(arr1, k1)) 