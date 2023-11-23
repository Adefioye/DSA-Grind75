arr = ["all", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]

def nearestRepeatedEntries(arr):
    wordToLatestIndex, minEntriesDistance = {}, float("inf")

    for i, word in enumerate(arr):

        if word in wordToLatestIndex:
            lastestIndex = wordToLatestIndex[word]
            minEntriesDistance = min(minEntriesDistance, i - lastestIndex)

        wordToLatestIndex[word] = i 

    return minEntriesDistance if minEntriesDistance != float("inf") else -1 

print(nearestRepeatedEntries(arr))