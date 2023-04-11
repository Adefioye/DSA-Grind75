num1 = 8
# Output: 7
num2 = 10
# Output: 5

def complementOfDecimal(num):

    bitCount, n = 0, num 

    while n:
        bitCount += 1 
        n >>= 1 

    allBitsSet = 2 ** bitCount - 1 

    return num ^ allBitsSet

print(complementOfDecimal(num1))
print(complementOfDecimal(num2))

## BRUTE FORCE SOLUTION
# def complementOfDecimal(num):

#     binary = ""

#     while num:

#         if num & 1:
#             binary += "0"
#         else:
#             binary += "1"

#         num >>= 1

    
#     return int(binary[::-1], 2)
    