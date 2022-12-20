from typing import List 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:

            for i in range(r - l):
                top, bottom = l, r

                # Save top left item
                top_left = matrix[top][l + i]

                # Move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom right to bottom left 
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top right to bottom right 
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move top left to top right
                matrix[top + i][r] = top_left

            l += 1
            r -= 1

