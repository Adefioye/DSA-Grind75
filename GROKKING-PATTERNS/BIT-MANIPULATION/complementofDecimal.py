num1 = 8
# Output: 7
num2 = 10
# Output: 5


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
    

print(complementOfDecimal(num1))
print(complementOfDecimal(num2))