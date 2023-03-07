from collections import deque

grid1 = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
grid2 = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
grid3 = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
# Output: 2

def numOfClosedIslands(grid):

    NROWS = len(grid)
    NCOLS = len(grid[0])
    count = 0 
    q = deque()
    LAND = 0
    WATER = 1

    if NROWS == 0 or NCOLS == 0:
        return count 
    
    for r in range(NROWS):
        for c in range(NCOLS):

            if grid[r][c] == LAND:
                isClosed = True 

                q.append((r, c))
                grid[r][c] = WATER 


                while q:
                    curRow, curCol = q.popleft()

                    if curRow in (0, NROWS - 1) or curCol in (0, NCOLS - 1):
                        isClosed = False 

                    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

                    for direction in directions:
                        row = curRow + direction[0]
                        col = curCol + direction[1]

                        if 0 <= row < NROWS and 0 <= col < NCOLS and grid[row][col] == LAND:
                            q.append((row, col))
                            grid[row][col] = WATER 

                
                if isClosed:
                    count += 1

    return count 

print(numOfClosedIslands(grid1))
print(numOfClosedIslands(grid2))
print(numOfClosedIslands(grid3))

