perm1 = [3, 2, 1, 0]; A1 = ["a", "b", "c", "d"]
perm2 = [4, 2, 0, 3, 1]; A2 = ["a", "b", "c", "d", "e"]

def permuteAnArray(perm, A):

    for i in range(len(A)):
        nxt = i 

        while perm[nxt] >= 0:
            A[i], A[perm[nxt]] = A[perm[nxt]], A[i]
            temp = perm[nxt]

            perm[nxt] -= len(A)
            nxt = temp

    return A


print(permuteAnArray(perm1, A1)) # [d, c b a]
print(permuteAnArray(perm2, A2)) # [c e b d a]
