arr1 = ["a", "c", "d", "b", "b", "c", "a"]
arr2 = ["a", "c", "a", "a"]

def replaceAndRemove(s):
    """
    1. Perform forward iteration and remove b's and count # of a
    2. Perform backward iteration to replace a's with dd's
    """
    writeIdx, aCount = 0, 0 

    for i in range(len(s)):

        if s[i] != "b":
            s[writeIdx] = s[i]
            writeIdx += 1

        if s[i] == "a":
            aCount += 1 

    curIdx = writeIdx - 1 
    writeIdx = curIdx + aCount 
    finalSize = writeIdx + 1
    # finalSize = writeIdx + 1
    # curSize = len(s)
    # Add zeros = finalSize - curSize
    for i in range(finalSize - len(s)):
        s.append(0)

    while curIdx >= 0:
        if s[curIdx] == "a":
            s[writeIdx - 1: writeIdx + 1] = "dd"
            writeIdx -= 2 
        else:
            s[writeIdx] = s[curIdx] 
            writeIdx -= 1 

        curIdx -= 1 

    return [s, len(s)]

print(replaceAndRemove(arr1))
print(replaceAndRemove(arr2))