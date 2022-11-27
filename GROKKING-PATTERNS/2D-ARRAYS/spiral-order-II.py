

def spiral_order_II(n):

    matrix = [[0]*n for _ in range(n)]
    item = 0

    left, right = 0, len(matrix[0]) - 1 
    top, bottom = 0, len(matrix) - 1 

    while top <= bottom and left <= right:

        # Place all elements in the top row

        for i in range(left, right+1):
            item += 1
            matrix[top][i] = item
        top += 1

        # Place all elements in the rightmost column

        for i in range(top, bottom + 1):
            item += 1
            matrix[i][right] = item
        right -= 1

        if not (top <= bottom and left <= right):
            break 

        # Place all bottom elements
        for i in range(right, left - 1, -1):
            item += 1
            matrix[bottom][i] = item
        bottom -= 1 

        # Place all elemnts in the left most column 

        for i in range(bottom, top - 1, -1):
            item += 1
            matrix[i][left] = item
        left += 1

    return matrix

# print(spiral_order_II(1))
print(spiral_order_II(3))
print(spiral_order_II(4))