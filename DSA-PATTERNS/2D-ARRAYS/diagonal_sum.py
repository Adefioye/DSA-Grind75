from typing import List 

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        total_sum = 0
        rows, cols = len(mat), len(mat[0])
        
        # Lets run sum along primary diagonal
        
        r, c = 0, 0 
        
        while r < rows and c < cols:
            total_sum += mat[r][c]
            r += 1 
            c += 1 

        # Lets run sum along secondary diagonal
        r, c = 0, cols - 1
        
        while r < rows and 0 <= c < cols:
            total_sum += mat[r][c]
            r += 1
            c -= 1

        
        if rows % 2 != 0:
            total_sum -= mat[rows // 2][cols // 2]
        
        return total_sum