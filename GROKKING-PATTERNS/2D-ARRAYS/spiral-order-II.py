

def spiral_order_II(n):

    nums = [i for i in range(1, n**2 + 1)]
    matrix = [[0]*n for _ in range(n)]
    nums_used = 0

    left, right = 0, len(matrix[0]) - 1 
    top, bottom = 0, len(matrix) - 1 

    while top <= bottom and left <= right:

        # Place all elements in the top row
        count = right - left + 1
        top_elements = nums[nums_used:nums_used + count]
        print(top_elements)
        nums_used += count

        for i in range(left, right+1):
            matrix[top][i] = top_elements.pop(0)
        top += 1

        # Place all elements in the rightmost column
        count = bottom - top + 1 
        rightmost_elements = nums[nums_used: nums_used + count]
        nums_used += len(rightmost_elements)

        for i in range(top, bottom + 1):
            matrix[i][right] = rightmost_elements.pop(0)
        right -= 1

        if not (top <= bottom and left <= right):
            break 

        # Place all bottom elements
        count = right - left + 1
        bottom_elements = nums[nums_used: nums_used + count]
        nums_used += count 

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = bottom_elements.pop(0)
        bottom -= 1 

        # Place all elemnts in the left most column
        count = bottom - top + 1 
        leftmost_elements = nums[nums_used : nums_used + count]
        nums_used += count 

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = leftmost_elements.pop(0)
        left += 1

    return matrix

# print(spiral_order_II(1))
print(spiral_order_II(3))