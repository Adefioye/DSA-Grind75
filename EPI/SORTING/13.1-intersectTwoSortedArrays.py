from bisect import bisect_left 

def intersection_of_two_sorted_arrays_1(A, B):
    """
    This approach works for arrays with varying lengths. Especially
    when one is significantly longer than the other
    """
    def isPresent(k):
        i = bisect_left(B, k)
        return i < len(B) and B[i] == k 
    
    res = []
    for i, a in enumerate(A):
        if (i == 0 or a != A[i - 1]) and isPresent(a):
            res.append(a)

    return res 

def intersection_of_two_sorted_arrays_2(A, B):

    l, r, res = 0, 0, []

    while l < len(A) and r < len(B):

        if A[l] == B[r]:

            if (l == 0 or (A[l] != A[l - 1])):
                res.append(A[l])
            
            l, r = l + 1, r + 1
        elif A[l] < B[r]:
            l += 1 
        else:
            r += 1 

    return res 

arr1, arr2 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12], [5, 5, 6, 8, 8, 9, 10, 10]

print(intersection_of_two_sorted_arrays_2(arr1, arr2))
# print(intersection_of_two_sorted_arrays_1(arr1, arr2))