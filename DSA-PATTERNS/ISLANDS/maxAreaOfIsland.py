from collections import deque

grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#Output: 6
grid2 = [[0,0,0,0,0,0,0,0]]
#Output: 0


## DFS SOLUTION
def maxAreaOfIsland(grid):

    NROWS = len(grid)
    NCOLS = len(grid[0])
    maxSize = 0 

    def dfs(r, c):
        rowInBound = 0 <= r < NROWS 
        colInBound = 0 <= c < NCOLS 

        if not rowInBound or not colInBound:
            return 0 
        
        if grid[r][c] == 0:
            return 0 
        
        grid[r][c] = 0 

        size = 1 

        size += dfs(r - 1, c)
        size += dfs(r + 1, c)
        size += dfs(r, c - 1)
        size += dfs(r, c + 1)

        return size 
    

    for r in range(NROWS):
        for c in range(NCOLS):

            if grid[r][c] == 1:
                size = dfs(r, c)

                if size > maxSize:
                    maxSize = size 

    return maxSize


print(maxAreaOfIsland(grid1))
print(maxAreaOfIsland(grid2))


## BFS SOLUTION
# def maxAreaOfIsland(grid):

#     if len(grid) == 0 or len(grid[0]) == 0:
#         return 0

#     LAND = 1 
#     WATER = 0 
#     maxCount = 0
#     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     NROWS = len(grid)
#     NCOLS = len(grid[0])

#     for r in range(NROWS):
#         for c in range(NCOLS):

#             if grid[r][c] == LAND:
#                 count = 1 

#                 queue = deque()
#                 queue.append((r, c))
#                 grid[r][c] = WATER

#                 while queue:
#                     curPos = queue.popleft()

#                     for direction in directions:

#                         row = curPos[0] + direction[0]
#                         col = curPos[1] + direction[1]

#                         if row < 0 or row >= NROWS or col < 0 or col >= NCOLS or grid[row][col] == 0:
#                             continue

#                         count += 1
#                         queue.append((row, col))
#                         grid[row][col] = WATER 

#                 maxCount = max(count, maxCount)

#     return maxCount 