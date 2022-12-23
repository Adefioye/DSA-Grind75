from typing import List 

matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    ROWS, COLS = len(matrix), len(matrix[0])
    INF = float("inf")

    for i in range(ROWS):
        for j in range(COLS):

            if matrix[i][j] == 0:

                # Change all values in rows except 0
                # Traverse to right
                # row is constant and col is changing
                col = j + 1

                while col < COLS:

                    if matrix[i][col] != 0:
                        matrix[i][col] = INF
                            
                    col += 1
                # Traverse to left
                col = j - 1

                while col >= 0:
                        
                    if matrix[i][col] != 0:
                        matrix[i][col] = INF
                            
                    col -= 1

                # Change all values in columns except 0
                # row is changing and column is constant
                # Traverse top
                row = i - 1

                while row >= 0:

                    if matrix[row][j] != 0:
                        matrix[row][j] = INF

                    row -= 1

                # Traverse down
                row = i + 1

                while row < ROWS:

                    if matrix[row][j] != 0:
                        matrix[row][j] = INF

                    row += 1
        

    # Replace infinity with zero
    for i in range(ROWS):
        for j in range(COLS):

            if matrix[i][j] == INF:
                matrix[i][j] = 0

    return matrix 


print(setZeroes(matrix1))
print(setZeroes(matrix2))