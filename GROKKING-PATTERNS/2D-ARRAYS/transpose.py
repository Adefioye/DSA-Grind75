# from typing import List 

matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
matrix_2 = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

# ANOTHER TRANSPOSE METHOD
def transpose(matrix):
    NROWS = len(matrix)
    NCOLS = len(matrix[0])

    res = [[0] * NROWS for _ in range(NCOLS)]

    for r in range(NROWS):
        for c in range(NCOLS):

            res[c][r] = matrix[r][c]

    return res

# def transpose(matrix):
#     ROWS, COLS = len(matrix), len(matrix[0])
#     res = [[0] * ROWS for _ in range(COLS)] 

#     col = 0
#     for nums in matrix:

#         for i, num in enumerate(nums):
#             res[i][col] = num

#         col += 1

#     return res

print(transpose(matrix_1))
print(transpose(matrix_2))