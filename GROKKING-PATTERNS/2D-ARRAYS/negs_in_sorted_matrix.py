from typing import List 

grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] # 8
grid2 = [[3,2],[1,0]]

def countNegatives(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])

    r = 0
    c = COLS - 1
    negatives = 0

    while c >= 0 and r < ROWS:

        if grid[r][c] < 0:
            negatives += ROWS - r 
            c -= 1 
        else:
            r += 1

    return negatives