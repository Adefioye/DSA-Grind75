matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def spiralOrder(squareMatrix):
    
    def matrixLayerInClockwise(offset):

        if offset == len(squareMatrix) - offset - 1:
            res.append(squareMatrix[offset][offset])
            return 
        
        res.extend(
            squareMatrix[offset][offset:-1-offset]
        )

        res.extend(
            list(zip(*squareMatrix))[-1 - offset][offset:-1-offset]
        )

        res.extend(
            squareMatrix[-1 -offset][-1 - offset: offset : -1]
        )

        res.extend(
            list(zip(*squareMatrix))[offset][-1 - offset: offset : -1]
        )


    res = []
        
    for offset in range((len(squareMatrix) + 1) // 2):
        matrixLayerInClockwise(offset)

    return res 

print(spiralOrder(matrix1)) # [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiralOrder(matrix2)) # [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]