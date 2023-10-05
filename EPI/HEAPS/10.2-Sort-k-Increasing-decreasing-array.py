# # merg
# from .10.1-Merge-Sorted-Files import mergeSortedArrs;
from heapq import heappop, heappush, heapify

def mergeSortedArrs(sortedArrays):

    minHeap = []
    sortedArrayIters = [iter(arr) for arr in sortedArrays]
    
    for i, it in enumerate(sortedArrayIters):
        firstElement = next(it, None)
        if firstElement is not None:
            minHeap.append([firstElement, i])

    # Heapify the operation
    heapify(minHeap)
    res = []

    while minHeap:
        smallestEntry, smallestEntryArrayIdx = heappop(minHeap)
        smallestEntryArrayIter = sortedArrayIters[smallestEntryArrayIdx]
        res.append(smallestEntry)
        nextElement = next(smallestEntryArrayIter, None)

        if nextElement is not None:
            heappush(minHeap, [nextElement, smallestEntryArrayIdx])

    return res

def sortIncreasingDecreasingArray(arr):
    sortedSubArrays = []
    INCREASING, DECREASING = range(2)
    subArrType = INCREASING 
    startIdx = 0

    for i in range(1, len(arr) + 1):

        if (i == len(arr) or 
            (arr[i] < arr[i - 1] and subArrType == INCREASING) or 
            (arr[i] >= arr[i - 1] and subArrType ==  DECREASING)):

            sortedSubArrays.append(arr[startIdx:i] 
                                   if subArrType == INCREASING else arr[i - 1: startIdx - 1: -1])
            
            subArrType = DECREASING if subArrType == INCREASING else INCREASING 
            startIdx = i 

    return mergeSortedArrs(sortedSubArrays)

arr1 = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
print(sortIncreasingDecreasingArray(arr1))