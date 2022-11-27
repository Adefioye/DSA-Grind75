from typing import List 

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        
        0, 0, 0
        1, 0, 1
        0, 1, 2
        1, 1, 3
        """
        rows, cols = len(board), len(board[0])
        
        def get_live_cells(r, c):
            lives = 0
            positions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
            for position in positions:
                row, col = position
                row, col = row + r, col + c
                
                if 0 <= row < rows and 0 <= col < cols :
                    
                    # if one
                    if board[row][col] in [1, 3]:
                        lives += 1
                        
            return lives
                        
        
        for r in range(rows):
            for c in range(cols):
                
                num_of_lives = get_live_cells(r, c)
                
                if board[r][c] == 1:
                    
                    if num_of_lives in [2, 3]:
                        board[r][c] = 3
                    else:
                        board[r][c] = 1
                else:
                    
                    if num_of_lives == 3:
                        board[r][c] = 2
                        
        for r in range(rows):
            for c in range(cols):
                
                if board[r][c] == 1:
                    board[r][c] = 0 
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1
                    
        
        return board
                        
                        
        
        