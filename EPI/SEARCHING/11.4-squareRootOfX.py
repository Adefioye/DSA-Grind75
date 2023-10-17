def sqrt(x):
    l, r = 0, x 

    while l <= r:

        mid = l + ((r - l) // 2)
        midSquared = mid * mid 

        if midSquared <= x:
            l = mid + 1 
        else:
            r = mid - 1 

    return r 

print(sqrt(8))
print(sqrt(32))
print(sqrt(100))
print(sqrt(7))