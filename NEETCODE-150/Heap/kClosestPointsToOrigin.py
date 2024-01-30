from heapq import heapify, heappop

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dist_points_pair = [[self.dist(x, y), [x, y]] for x, y in points]

        heapify(dist_points_pair)

        res = []

        while k != 0:
            _, point = heappop(dist_points_pair)
            res.append(point)
            k -= 1

        return res