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
