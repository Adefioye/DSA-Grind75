from heapq import heapify, heappop, heappush

s1 = "abbabbaaab"
# Output: "ababababab"
s2 = "aab"
# Output: "aba"
s3 = "aaab"
# Output: ""

def reorganizeString(s):

    count = {}
    for char in s:
        count[char] = 1 + count.get(char, 0)

    maxHeap = [[-f, k] for k, f in count.items()]

    # Create a heap using heapify
    heapify(maxHeap)
    res = ""
    
    while len(maxHeap) > 1:
        curF, curC = heappop(maxHeap)
        nxtF, nxtC = heappop(maxHeap)

        res += (curC + nxtC)

        curF += 1
        nxtF += 1

        if curF != 0:
            heappush(maxHeap, [curF, curC])
        if nxtF != 0:
            heappush(maxHeap, [nxtF, nxtC])

    # If maxHeap has one more value in maxHeap
    if maxHeap:
        lastF, lastC = heappop(maxHeap)
        lastF = -lastF
        if lastF > 1:
            return ""
        
        res += lastC 

    return res

print(reorganizeString(s1))
print(reorganizeString(s2))
print(reorganizeString(s3))