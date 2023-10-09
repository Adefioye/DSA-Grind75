from heapq import heappop, heappush

def computeKLargestWithoutModifyingHeap(maxHeap, k):

    # (-value, idx)
    candidateMaxHeap = []
    res = []
    candidateMaxHeap.append((-maxHeap[0], 0))

    for _ in range(k):
        parentIdx = candidateMaxHeap[0][1]
        res.append(-heappop(candidateMaxHeap)[0])
        leftChildIdx = 2 * parentIdx + 1
        rightChildIdx = 2 * parentIdx + 2 

        if leftChildIdx < len(maxHeap):
            heappush(candidateMaxHeap, (-maxHeap[leftChildIdx], leftChildIdx)) 

        if rightChildIdx < len(maxHeap):
            heappush(candidateMaxHeap, (-maxHeap[rightChildIdx], rightChildIdx))

        
    return res 

arr1 = [561, 314, 401, 28, 156, 359, 271, 11, 3]

print(computeKLargestWithoutModifyingHeap(arr1, 4))
