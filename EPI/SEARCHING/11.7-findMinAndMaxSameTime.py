arr1 = [3, 2, 5, 1, 2, 4]
arr2 = [3, 6, 5, 1, 0]

def findMinAndMaxSimultaneously(arr):
    "Return array of [min, max]"
    globalMin = float("inf")
    globalMax = float("-inf")

    for i in range(0, len(arr), 2):
        a1, a2 = arr[i], arr[i + 1] if (i + 1) < len(arr) else arr[i]
        localMin = min(a1, a2)
        localMax = max(a1, a2)
        globalMin = min(localMin, globalMin)
        globalMax = max(localMax, globalMax)

    return [globalMin, globalMax]

print(findMinAndMaxSimultaneously(arr1))
print(findMinAndMaxSimultaneously(arr2))