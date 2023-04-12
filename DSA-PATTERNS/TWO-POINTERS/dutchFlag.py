A1 = [1, 0, 2, 1, 0] # [0 0 1 1 2]
A2 = [2, 2, 0, 1, 2, 0] # [0 0 1 2 2 2 ]

def dutch_flag(arr):

    l, r = 0, len(arr) - 1
    p = 0

    while p <= r:

        if arr[p] == 0:
            # Swap p and l
            arr[p], arr[l] = arr[l], arr[p]
            l += 1 
            p += 1 
        elif arr[p] == 2:
            # Swap r and p 
            arr[p], arr[r] = arr[r], arr[p]
            r -= 1 
        else:
            p += 1 

    
    return arr

print(dutch_flag(A1))
print(dutch_flag(A2))