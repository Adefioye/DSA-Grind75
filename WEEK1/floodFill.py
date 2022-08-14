# SOLUTION 1: USing DFS

# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         row_size = len(image)
#         col_size = len(image[0])
#         visited = set()
#         target = image[sr][sc]
#         dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
#         def dfs(row, col, visited):
#             visited.add((row, col))
#             image[row][col] = color
                
#             for dir in dirs:
#                 r = row + dir[0]
#                 c = col + dir[1]
                
#                 if r < 0 or r >= row_size or c < 0 or c >= col_size or (r, c) in visited or image[r][c] != target:
#                     continue
                    
#                 dfs(r, c, visited)
          
#         dfs(sr, sc, visited)
#         return image


# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         row_size = len(image)
#         col_size = len(image[0])
#         target = image[sr][sc]
#         dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
#         def dfs(row, col):
#             image[row][col] = color
                
#             for dir in dirs:
#                 r = row + dir[0]
#                 c = col + dir[1]
                
#                 print(r, c)
#                 if (0 >= r < row_size) and (0 >= c < col_size) and (image[r][c] == target):
#                     dfs(r, c)
          
#         dfs(sr, sc)
#         return image


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        source = image[sr][sc]
        if image[sr][sc] == color:
            return image
        else:
            self.dfss(image, sr , sc, rows, cols, source, color)
        return image
    
    def dfss(self, image, sr , sc, rows, cols, source, color):
        if (sr<0 or sc<0 or sr>= rows or sc>=cols):
            return None
        if image[sr][sc] != source:
            return None
        image[sr][sc] = color
        self.dfss(image, sr+1 , sc, rows, cols, source, color)
        self.dfss(image, sr , sc+1, rows, cols, source, color)
        self.dfss(image, sr-1 , sc, rows, cols, source, color)        
        self.dfss(image, sr , sc-1, rows, cols, source, color)
