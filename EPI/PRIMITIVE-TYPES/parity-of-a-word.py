"""
Parity of a binary word is 1 if number of 1s in the word is odd.
Otherwise is 0. Parity checks are used to detect single bit errors in 
data storage and communication.

NB: x & (x - 1) is used to clear the lowest set bit
"""

# SOLUTION 1
# time = O(n) where n - number of bits
def parity(x):
    res = 0
    while x:

        if x & 1:
            res ^= 1
        
        x >>= 1

    return res

# SOLUTION 2
# time = O(k) where k is number of set bits
# Hint x & (x - 1). This cancels out lowest set bit
def parity(x):

    res = 0 

    while x:
        res ^= 1 
        x &= (x - 1) # This drops lowest set bit
    
    return res

# SOLUTION 3
# time = O(logn) where n is number of bits 
def parity(x):

    x ^= x >> 32
    x ^= x >> 16 
    x ^= x >> 8 
    x ^= x >> 4 
    x ^= x >> 2 
    x ^= x >> 1

    return x & 1 




