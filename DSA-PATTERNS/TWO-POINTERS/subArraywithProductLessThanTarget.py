A1 = [2, 5, 3, 10]; T1=30   # [2], [5], [2, 5], [3], [5, 3], [10]
A2 = [8, 2, 6, 5]; T2=50    # [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
""""
r = 3
30/2 = 15
2, 1

"""
# def subArrayWithProductLessThanTarget(array, target):
#     l = 0 
#     prod = 1 
#     res = []

#     for r in range(len(array)):
#         curNum = array[r]

#         prod *= curNum 

#         if curNum < target:
#             res.append([curNum]) 
        

#         while prod >= target:
#             prod /= array[l]
#             l += 1

#         if (r - l + 1 > 1):
#             res.append(array[l:r+1])

#     return res

def subArrayWithProductLessThanTarget(A, T):

    prod = 1
    res = []
    l = 0

    for r, num in enumerate(A):

        prod *= num

        while prod >= T:
            prod /= A[l]
            l += 1

        for i in range(l, r + 1):
            res.append(A[i : r + 1])

    return res

print(subArrayWithProductLessThanTarget(A1, T1))
print(subArrayWithProductLessThanTarget(A2, T2))
