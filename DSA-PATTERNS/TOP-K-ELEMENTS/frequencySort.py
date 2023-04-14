import heapq 

s1 = "tree"
# Output: "eert"
s2 = "cccaaa"
# Output: "aaaccc"
s3 = "Aabb"
# Output: "bbAa"

def frequencySort(s):

    count = {}

    for char in s:
        count[char] = 1 + count.get(char, 0)

    minHeap = [[-freq, key] for key, freq in count.items()]

    # Heapify 
    heapq.heapify(minHeap)

    res = ""

    for _ in range(len(minHeap)):
        freq, key = heapq.heappop(minHeap)
        freq = -freq 

        while freq > 0:
            res += key 
            freq -= 1 
        
    return res

print(frequencySort(s1))
print(frequencySort(s2))
print(frequencySort(s3))