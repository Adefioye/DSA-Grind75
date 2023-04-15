from heapq import heapify, heappop

arr1 = [1,2,3,4,5]; k1 = 4; x1 = 3
# Output: [1,2,3,4]
arr2 = [1,2,3,4,5]; k2 = 4; x2 = -1
# Output: [1,2,3,4]
arr3 = [1,1,1,10,10,10]; k3 = 1; x3 = 9

def distance(num, x):
    return abs(num - x)

def findKClosestElements(nums, k, x):

    pivot = closestElementToTarget(nums, x)
    l = max(0, pivot - k)
    r = min(len(nums) - 1, pivot + k)

    while r - l + 1 > k:

        if abs(nums[l] - x) <= abs(nums[r] - x):
            r -= 1 
        else:
            l += 1 

    return nums[l : r + 1]

def closestElementToTarget(nums, target):

    l, r = 0, len(nums) - 1 

    if target < nums[l]:
        return l 
    if target > nums[r]:
        return r 
    
    while l <= r:

        mid = ( l + r) // 2 

        if target < nums[mid]:
            r = mid - 1 
        elif target > nums[mid]:
            l = mid + 1 
        else:
            return mid 
        
    return r


print(findKClosestElements(arr1, k1, x1))
print(findKClosestElements(arr2, k2, x2))
print(findKClosestElements(arr3, k3, x3))

# def findKClosestElements(nums, k, x):

#     lst = [[distance(num, x), num] for num in nums]

#     # Sort by heapifying
#     heapify(lst)
#     res = []

#     while k > 0:
#         _, val = heappop(lst)
#         res.append(val)
#         k -= 1 

#     return sorted(res)