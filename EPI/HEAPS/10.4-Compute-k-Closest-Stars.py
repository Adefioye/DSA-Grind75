import math
from heapq import heappush, heappop

class Star:

    def __init__(self, x, y, z) -> None:
        self.x, self.y, self.z = x, y, z 

    @property
    def distance(self) -> int:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __lt__(self, rhs) -> bool:
        return self.distance < rhs.distance 
    
def kClosestStars(stars, k):

    minHeap = []

    for star in stars:

        heappush(minHeap, [-star.distance, star])

        if len(minHeap) > k:
            heappop(minHeap)

    return [item[1] for item in minHeap]
