matrix1 = [[1,2,3],[4,5,6],[7,8,9]]             # [1,2,3,6,9,8,7,4,5]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]    # [1,2,3,4,8,12,11,10,9,5,6,7]

def spiral_order_I(matrix):
    res = []

    top, bottom = 0, len(matrix) - 1 
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Get all elements from top row 
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1 

        # Get all element from the rightmost column
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1 

        if not (top <= bottom and left <= right):
            break 

        # Get all elements at the bottom
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1 

        # Get all elements from leftmost column
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res 

print(spiral_order_I(matrix1))
print(spiral_order_I(matrix2))

