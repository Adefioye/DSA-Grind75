class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = ROWS - 1, 0

        while r >= 0 and c < COLS:
            val = matrix[r][c]

            if target < val:
                # decrease row
                r -= 1
            elif target > val:
                # increase col
                c += 1
            else:
                return True 

        return False