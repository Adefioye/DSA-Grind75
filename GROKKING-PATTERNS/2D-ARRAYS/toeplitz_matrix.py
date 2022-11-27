from typing import List 

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])
        
        def is_diagonal_same(r, c):
            val = matrix[r][c]
            r += 1
            c += 1
            
            while r < rows and c < cols:
                
                if matrix[r][c] != val:
                    return False 
                
                r += 1 
                c += 1 
                
            return True
        
        
        # Scan the rows
        for c in range(cols):
            
            if not is_diagonal_same(0, c):
                return False 
        
        # Scan cols leaving first row
        for r in range(1, rows):
            
            if not is_diagonal_same(r, 0):
                return False 
            
        return True
        