arr1 = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8] # 6
arr2 = [10, 5, 3, 11, 6, 100, 4]           # 4

def lengthOfContainedIntervalIntuitive(arr):

    hashSet = set(arr)
    size = 0 

    for num in arr:

        if num in hashSet:
            containedSet = set()
            containedSet.add(num)
            hashSet.remove(num)

            c = 1
            while (num + c) in hashSet:
                containedSet.add(num + c)
                hashSet.remove(num + c)
                c += 1 
            
            c = 1
            while (num - c) in hashSet:
                containedSet.add(num - c)
                hashSet.remove(num - c)
                c += 1 
            
            size = max(size, len(containedSet))

    return size 

# print(lengthOfContainedInterval(arr1))
# print(lengthOfContainedInterval(arr2))

def lengthOfContainedIntervalSmartApproach(arr):
    unprocessedEntries = set(arr)
    size = 0

    while unprocessedEntries:
        val = unprocessedEntries.pop()

        lowerBound = val - 1
        while lowerBound in unprocessedEntries:
            unprocessedEntries.remove(lowerBound)
            lowerBound -= 1 

        upperBound = val + 1
        while upperBound in unprocessedEntries:
            unprocessedEntries.remove(upperBound)
            upperBound += 1 

        size = max(size, upperBound - lowerBound - 1)

    return size 

print(lengthOfContainedIntervalSmartApproach(arr1))
print(lengthOfContainedIntervalSmartApproach(arr2))