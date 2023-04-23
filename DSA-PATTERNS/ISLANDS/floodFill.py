from collections import deque 

image1 = [[1,1,1],[1,1,0],[1,0,1]]; sr1 = 1; sc1 = 1; color1 = 2
#Output: [[2,2,2],[2,2,0],[2,0,1]]
image2 = [[0,0,0],[0,0,0]]; sr2 = 0; sc2 = 0; color2 = 0
#Output: [[0,0,0],[0,0,0]]

def floodFill(image, sr, sc, color):

    if image[sr][sc] == color:
        return image 
    
    target = image[sr][sc]
    NROWS, NCOLS = len(image), len(image[0])

    def dfs(r, c):

        rowInBound = 0 <= r < NROWS
        colInBound = 0 <= c < NCOLS 

        if not rowInBound or not colInBound or image[r][c] != target:
            return 
        
        image[r][c] = color 

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    dfs(sr, sc)

    return image


print(floodFill(image1, sr1, sc1, color1))
print(floodFill(image2, sr2, sc2, color2))

## BFS SOLUTION
# def floodFill(image, sr, sc, color):

#     NROWS = len(image)
#     NCOLS = len(image[0])

#     if image[sr][sc] == color:
#         return image

#     queue = deque()
#     # visited = set()

#     queue.append((sr, sc))
#     # visited.add((sr, sc))

#     startingColor = image[sr][sc]
#     image[sr][sc] = color 

#     while queue:
#         curPos = queue.popleft()

#         directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#         for direction in directions:
#             row = curPos[0] + direction[0]
#             col = curPos[1] + direction[1]

#             if row < 0 or row >= NROWS or col < 0 or col >= NCOLS or image[row][col] != startingColor:
#                 continue
                
#             image[row][col] = color 
#             queue.append((row, col))
#             # visited.add((row, col))

#     return image
    