from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        time = 0
        counts = Counter(tasks)
        maxHeap = [-c for c in counts.values()]
        # Create a heap
        heapify(maxHeap)
        q = deque() # [-cnt, delayTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])

        return time