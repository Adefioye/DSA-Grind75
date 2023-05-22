"""
Instead of treating the integer inputs as a string. We can 
use modular arithmetic. By dividing input by 10
"""

def reverseDigits(x):

    res, xRemainder = 0, abs(x)

    while xRemainder:
        quotient = xRemainder // 10
        rem = xRemainder % 10
        res = res * 10 + rem 
        xRemainder = quotient 

    return -res if x < 0 else res 

print(reverseDigits(111345))
print(reverseDigits(-4356))
