"""

x & (x - 1) clear lowest set bit
x & ~(x - 1) extract lowest set bit
"""
n = int("1110000000000001", 2)
# Output 1000000000000111

def swap(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        # Flip the bits at l and r
        bitMask = (1 << i) | (1 << j)
        x ^= bitMask
    return x

def reverseBits(x):
    # For 16-bit input
    l, r = 15, 0

    while r < l:
        # Extract bit in l and r and check if they are unequal
        # if unequal, flip the bits using XOR operation
        x = swap(x, l, r)
         
        l -= 1 
        r += 1

    return x

res = reverseBits(n)
print(bin(res).replace("0b", ""))
# Output 1000000000000111

# def setBitSize(x):
#     count = 0

#     while x:
#         count += 1 
#         x &= (x - 1)

#     return count

# print(setBitSize(n))