import heapq 

nums1 = [1,1,1,2,2,3]; k1 = 2
# Output: [1,2]
nums2 = [1]; k2 = 1
# Output: [1]

# HEAP
def topKFrequent(nums, k):
    countMap = {}

    for num in nums:
        countMap[num] = 1 + countMap.get(num, 0)
    
    minHeap = [[-freq, key] for key, freq in countMap.items()]

    # Heapify
    heapq.heapify(minHeap)

    res = []

    while k > 0:
        _, key = heapq.heappop(minHeap)
        res.append(key)
        k -= 1

    return res



print(topKFrequent(nums1, k1))
print(topKFrequent(nums2, k2))

# def topKFrequent(nums, k):
        
#     countMap = {}
#     freq = [[] for _ in range(len(nums) + 1)]

#     for num in nums:
#          countMap[num] = 1 + countMap.get(num, 0)

#     for n, c in countMap.items():
#         freq[c].append(n)

#     res = []
#     for i in range(len(freq) - 1, 0, -1):
#         keys = freq[i]
#         if keys:
#             for key in keys:
#                 res.append(key)
#                 if len(res) == k:
#                     return res
            


# QUICKSELECT METHOD HINT
# def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count=list(Counter(nums).items())
#         def quick(l,r):
#             pivot,p = count[r][1],l
#             for i in range(l,r):
#                 if pivot>=count[i][1]:
#                     count[i], count[p] = count[p], count[i]
#                     p+=1
#             count[r], count[p] = count[p], count[r]
#             if p>len(count)-k:
#                 return quick(l,p-1)
#             if p<len(count)-k:
#                 return quick(p+1,r)
#             else:
#                 return p
#         ind=quick(0,len(count)-1)
#         return [k for i,(k,_) in enumerate(count) if i>=ind]