from typing import List

A1 = [3, 2, 3, 6, 3, 10, 9, 3]; T1 = 3  # 4
A2 = [2, 11, 2, 2, 1]; T2 = 2           # 2

def removeTarget(array: List[int], target: int) -> int:

    l = 0 

    for r in range(len(array)):

        if array[r] != target:
            array[l] = array[r]
            l += 1 

    return l 

print(removeTarget(A1, T1))
print(removeTarget(A2, T2))
