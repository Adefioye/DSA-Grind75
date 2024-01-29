from heapq import heappop, heappush, heapify

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # Prepare weight of stones for minHeap by adding negative to all weight
        stones = [-weight for weight in stones]
        # Heapify
        heapify(stones)
        # Pop heaviest weights
        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)

            if x != y:
                diff = y - x
                heappush(stones, -diff)

        return abs(stones[0]) if stones else 0