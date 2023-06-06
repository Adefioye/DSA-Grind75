"""
Problem statement:

Select a random subset of size k from an array A of length n
"""
import random 

def randomSampling(A, k):
    n = len(A)
    remove = None
    if k > (n // 2):
        k = n - k 
        remove = True 

    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

    if remove:
        # This helps with optimization and remove first k values
        return A[k:]

    return A[:k] 

print(randomSampling(["a", "b", "c", "d", "e", "f", "g"], 5))
print(randomSampling([3, 7, 5, 11], 3))