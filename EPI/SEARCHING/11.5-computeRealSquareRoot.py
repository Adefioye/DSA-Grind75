import math 

def computeRealSquareRoot(x):
    """
    This works for computing real numbers(positve integers
    and floating point numbers)
    """
    l, r = (1, x) if x >= 1 else (x, 1)

    while not math.isclose(l, r):
        mid = 0.5 * (l + r)
        midSquared = mid * mid 

        if midSquared <= x:
            l = mid
        else:
            r = mid

    return r

print(computeRealSquareRoot(0.25))
# print(computeRealSquareRoot(1))