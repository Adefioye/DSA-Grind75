"""
Problem statement

Compute the random subset of an array while making sure that each combination and permutation
have equal probability. This will be achieved using a hash set as it helps to keep track
of elements in the array that has been visited.


"""
import random

def randomSubset(n, k):

    changedElements = {}

    for i in range(k):
        randIdx = random.randrange(i, n)
        randIdxMapped = changedElements.get(randIdx, randIdx) 
        iMapped = changedElements.get(i, i)
        changedElements[randIdx] = iMapped 
        changedElements[i] = randIdxMapped

    return [changedElements[i] for i in range(k)]

print(randomSubset(100, 4))

