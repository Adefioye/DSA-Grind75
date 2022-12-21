from typing import List 

matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix_2 = [[1,2,3],[4,5,6]]

def transpose(matrix: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(matrix), len(matrix[0])
    res = [[0] * ROWS for _ in range(COLS)] 

    col = 0
    for nums in matrix:

        for i, num in enumerate(nums):
            res[i][col] = num

        col += 1

    return res

print(transpose(matrix_1))
print(transpose(matrix_2))