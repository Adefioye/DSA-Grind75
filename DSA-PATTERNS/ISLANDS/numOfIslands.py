grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
#Output: 1

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
#Output: 3

from collections import deque

def numIslands(grid):

    NROWS = len(grid)
    NCOLS = len(grid[0])
    count = 0

    def dfs(r, c):
        rowInBounds = 0 <= r < NROWS 
        colInBounds = 0 <= c < NCOLS 

        if not rowInBounds or not colInBounds:
            return 
        
        if grid[r][c] == "0":
            return 
        
        grid[r][c] = "0"

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in range(NROWS):
        for c in range(NCOLS):

            if grid[r][c] == "1":
                dfs(r, c)
                count += 1

    return count

print(numIslands(grid1))
print(numIslands(grid2))

# def numIslands(grid):

#     if len(grid) == 0 or len(grid[0]) == 0:
#         return 0 
    
#     count = 0
#     NROWS = len(grid)
#     NCOLS = len(grid[0])
#     LAND = "1"
#     WATER = "0"
#     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#     for r in range(NROWS):
#         for c in range(NROWS):

#             if grid[r][c] == LAND:
#                 count += 1 

#                 queue = deque()
#                 queue.append((r, c))
#                 grid[r][c] = WATER 


#                 while queue:
#                     curPos = queue.popleft()

#                     for direction in directions:
#                         row = curPos[0] + direction[0]
#                         col = curPos[1] + direction[1]

#                         if row < 0 or row >= NROWS or col < 0 or col >= NCOLS or grid[row][col] == WATER:
#                             continue 

#                         queue.append((row, col))
#                         grid[row][col] = WATER 

#     return count

# print(numIslands(grid1))
# print(numIslands(grid2))