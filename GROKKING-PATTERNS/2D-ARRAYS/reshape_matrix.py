from typing import List 

mat1 = [[1,2],[3,4]]; r1 = 1; c1 = 4    #  [[1,2,3,4]]
mat2 = [[1,2],[3,4]]; r2 = 2; c2 = 4    # [[1,2],[3,4]]

def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:

    # Check if dimensions are not same so return original matrix
    # Else, flatten and loop and add to new matrix
    ROW, COL = len(mat), len(mat[0])

    if (ROW * COL != r * c):
        return mat
    else:

        flat_mat = []
        res = []
        for row in mat:
            flat_mat.extend(row)

        col = 0

        for _ in range(r):
            res.append(flat_mat[col : col + c])
            col += c

    return res


print(matrixReshape(mat1, r1, c1))
print(matrixReshape(mat1, r2, c2))