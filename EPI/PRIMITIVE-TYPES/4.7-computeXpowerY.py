
# time = O(log y)


def myPow(x: float, n: int) -> float:

    def helper(x, n):

        if n == 0:
            return 1
        
        if n % 2 == 0:
            return helper(x * x, n/2)
        
        return x * helper(x, n - 1)

        
    if n < 0:
        x, n = 1/ x, -n
        
    sign = 1
    if x < 0 and (n % 2 != 0):
        sign = -1
        x = -x

    print(sign)   
    return sign * helper(x, n)
        

# def power(x, y):

#     res, power = 1, y 

#     if y < 0:
#         power, x = -power, 1/x 

#     while power:

#         if power & 1:
#             res *= x
        
#         x, power = x * x, power >> 1 

#     return res 



