from heapq import heapify, heappop

arr1 = [1,2,3,4,5]; k1 = 4; x1 = 3
# Output: [1,2,3,4]
arr2 = [1,2,3,4,5]; k2 = 4; x2 = -1
# Output: [1,2,3,4]

def distance(num, x):
    return abs(num - x)

def findKClosestElements(nums, k, x):

    lst = [[distance(num, x), num] for num in nums]

    # Sort by heapifying
    heapify(lst)
    res = []

    while k > 0:
        _, val = heappop(lst)
        res.append(val)
        k -= 1 

    return sorted(res)



print(findKClosestElements(arr1, k1, x1))
print(findKClosestElements(arr2, k2, x2))