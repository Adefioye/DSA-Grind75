n1 = 14
n2 = 15 


def countSetBits(n):
    """
    Using & and masking 
    O(number of set bits)
    """
    count = 0
    while n:
        count += 1 
        n &= (n-1)

    return count

print(countSetBits(n1))
print(countSetBits(n2))
# def countSetBits(n):
#     """
#     This using & and << operator
#     O(number of bits)
#     """
#     count = 0
#     while n:
#         if n & 1 == 1:
#             count += 1
        
#         n >>= 1

#     return count 