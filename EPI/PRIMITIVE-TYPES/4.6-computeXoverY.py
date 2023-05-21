"""
Compute x over y (Using addition, subtraction and shifting operator)

time = O(n), where n = # of bits to represent x/y

NB: The general idea is do the following
1. Initialize quotient, res = 0
2. Find k for which 2^k * y <= x
3. Add 2^k to res
4. Update x as (x - (2^k * y)) 
5. Continue step 2 - 4 until updated x < y
"""

def divide(x, y):
    res, k = 0, 32 
    yPower = y << k 

    while x >= y:

        while yPower > x:
            yPower >>= 1 
            k -= 1 

        res += 1 << k 
        x -= yPower 

    return res 

print(divide(11, 2))    # 5
print(divide(11, 3))    # 3