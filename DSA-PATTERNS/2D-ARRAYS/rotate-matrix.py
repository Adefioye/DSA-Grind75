from typing import List 

# Method 2 
# This involves transposing the matrix and reversing every row of the matrix
def rotate(matrix):
    """
    This is done in-place
    """
    # Transpose and reverse 

    # Transpose 
    for r in range(len(matrix)):
        for c in range(r, len(matrix)):
            temp = matrix[c][r]
            matrix[c][r] = matrix[r][c]
            matrix[r][c] = temp 

    # Reverse 
    for row in matrix:
        row.reverse()

    return matrix 



# Method 1 involving rotating the matrix by moving elements clockwisely along edges
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         l, r = 0, len(matrix) - 1

#         while l < r:

#             for i in range(r - l):
#                 top, bottom = l, r

#                 # Save top left item
#                 top_left = matrix[top][l + i]

#                 # Move bottom left to top left
#                 matrix[top][l + i] = matrix[bottom - i][l]

#                 # Move bottom right to bottom left 
#                 matrix[bottom - i][l] = matrix[bottom][r - i]

#                 # Move top right to bottom right 
#                 matrix[bottom][r - i] = matrix[top + i][r]

#                 # Move top left to top right
#                 matrix[top + i][r] = top_left

#             l += 1
#             r -= 1

