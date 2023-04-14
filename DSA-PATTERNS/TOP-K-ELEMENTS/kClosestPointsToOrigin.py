import random

points1 = [[1,3],[-2,2]]; k1 = 1
# Output: [[-2,2]]
points2 = [[3,3],[5,-1],[-2,4]]; k2 = 2
# Output: [[3,3],[-2,4]]
points3 = [[6,10],[-3,3],[-2,5],[0,2]]; k3 = 3
#Output: [[-3,3],[-2,5],[0,2]]

# USING QUICKSELECT
def kClosestToOrigin(points, k):

    points = [[dist(point), point] for point in points]

    def quickSelect(l, r, k):

        if r - l + 1 == k:
            return [point[1] for point in points[l : r + 1]]
        
        # Generate random index and swap with right value
        rIdx = random.randint(l, r)
        points[rIdx], points[r] = points[r], points[rIdx]
        pIndex = partition(points, l, r)

        kthPoints = pIndex - l + 1 

        if kthPoints == k:
            return [point[1] for point in points[l : pIndex + 1]]
        elif kthPoints > k:
            return quickSelect(l, pIndex - 1, k)
        else:
            return [point[1] for point in points[l : pIndex + 1]] + quickSelect(pIndex + 1, r, k - kthPoints)
        
    return quickSelect(0, len(points) - 1, k)

def partition(points, l, r):

    pIndex, pivot = l, points[r][0] 

    for i in range(l, r):

        if points[i][0] <= pivot:
            points[i], points[pIndex] = points[pIndex], points[i]
            pIndex += 1 

    # Swap the points at the current pIndex and the right value
    points[pIndex], points[r] = points[r], points[pIndex] 

    return pIndex

def dist(point):
    return point[0] ** 2 + point[1] ** 2

print(kClosestToOrigin(points1, k1))
print(kClosestToOrigin(points2, k2))
print(kClosestToOrigin(points3, k3))

