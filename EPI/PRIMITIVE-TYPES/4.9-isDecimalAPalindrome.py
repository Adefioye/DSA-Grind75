import math
"""
Check if decimal is a palindrome or not
inputs 0, 1, 7, 17, 727 and 333 return True
inputs -1, 12, 100 and 2147483647 return False

This works by leveraging understanding of LSB and MSB
if input = x and num of digits in input, n = log10(x) + 1
LSD = x mod 10
MSD = x / 10^(n - 1)
"""

def isNumberAPalindrome(x):

    if x <= 0:
        return x == 0 
    
    n = math.floor(math.log10(x)) + 1
    l, r = 0, n - 1 
    msdMask = 10 ** (n - 1)

    while l < r:

        # Check if MSD != LSD
        if (x // msdMask) != x % 10:
            return False
        
        # Remove MSD
        x = x % msdMask
        # Remove LSD
        x //= 10 

        # Update msdMask
        msdMask /= 100 

        # Update pointers
        l += 1
        r -= 1 

    return True 

print(isNumberAPalindrome(-1))          # False
print(isNumberAPalindrome(2147483647))  # False 
print(isNumberAPalindrome(2147447412)) # True
print(isNumberAPalindrome(333)) # True

