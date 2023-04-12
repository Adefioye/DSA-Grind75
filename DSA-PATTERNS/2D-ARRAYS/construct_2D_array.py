from typing import List 

original1 = [1,2,3,4]; m1 = 2; n1 = 2   # [[1,2],[3,4]]
original2 = [1,2,3]; m2 = 1; n2 = 3      # [[1,2,3]]
original3 = [1,2]; m3 = 1; n3 = 1       #  []

def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:

    total = len(original)

    if total != m * n:
        return []

    res = []
    col = 0

    for _ in range(m):
        res.append(original[col : col + n])
        col += n
        
    return res

print(construct2DArray(original1, m1, n1))
print(construct2DArray(original2, m2, n2))
print(construct2DArray(original3, m3, n3))