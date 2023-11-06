from collections import namedtuple
arr = [5, 3, 0, 3, 1, 2]
# arr2 = [4, 3, 6, 2, 1, 1]

def findDuplicateAndMissing(arr):

    DuplicateAndMissing = namedtuple("DuplicateAndMissing",
                                     ("duplicate", "missing"))
    dupMissingXOR = 0
    for i, a in enumerate(arr):
        dupMissingXOR ^= i 
        dupMissingXOR ^= a 

    # Find the differBit
    differBit = dupMissingXOR & ~(dupMissingXOR - 1)
    dupOrMissing = 0 

    for i, a in enumerate(arr):
        # Focus on entries and numbers that have set bit in same position as
        # as that of differBit
        if a & differBit:
            dupOrMissing ^= a 
        if i & differBit:
            dupOrMissing ^= i

    # print("differ bit, XOR ", differBit, dupMissingXOR)
    if dupOrMissing in arr:
        return DuplicateAndMissing(dupOrMissing, dupOrMissing ^ dupMissingXOR)

    return DuplicateAndMissing(dupOrMissing ^ dupMissingXOR, dupOrMissing) 

print(findDuplicateAndMissing(arr))