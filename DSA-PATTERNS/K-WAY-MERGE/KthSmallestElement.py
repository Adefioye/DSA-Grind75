matrix1 = [[1,5,9],[10,11,13],[12,13,15]]; k1 = 8
# Output: 13
matrix2 = [[-5]]; k2 = 1
# Output: -5

from heapq import heappop, heapify, heappush

class Solution:
    def kthSmallest(self, matrix, k) -> int:

        minHeap = []

        for i, arr in enumerate(matrix):
            if arr:
                minHeap.append([arr[0], i, 0]) # [firstVal, ]

        # create a heap
        heapify(minHeap)

        counter = 0 

        while minHeap:
            val, i, curIdx = heappop(minHeap)

            counter += 1 

            if counter == k:
                return val 

            if curIdx + 1 < len(matrix[i]):
                heappush(minHeap, [matrix[i][curIdx + 1], i, curIdx + 1])

ans = Solution()
print(ans.kthSmallest(matrix1, k1))
print(ans.kthSmallest(matrix2, k2))