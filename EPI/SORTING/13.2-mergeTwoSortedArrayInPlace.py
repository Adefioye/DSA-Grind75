nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3

def mergeTwoSortedArrays(A, m, B, n):
    l, r = m - 1, n - 1
    writeIdx = m + n - 1 

    while l >= 0 and r >= 0:

        if A[l] >= B[r]:
            A[writeIdx] = A[l]
            l -= 1
        else:
            A[writeIdx] = B[r]
            r -= 1 

        writeIdx -= 1

    while r >= 0:
        A[writeIdx] = B[r]
        writeIdx, r = writeIdx - 1, r - 1 

    return A

print(mergeTwoSortedArrays(nums1, m, nums2, n))
