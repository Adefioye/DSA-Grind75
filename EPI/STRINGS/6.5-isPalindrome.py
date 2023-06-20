s1 = "A man, a plan, a canal: Panama"
# Output: true
s2 = "race a car"
# Output: false
s3 = " "
# Output: true


def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1 

    while l < r:

        while not s[l].isalnum() and l < r:
            l += 1 
        while not s[r].isalnum() and l < r:
            r -= 1 

        if s[l].lower() != s[r].lower():
            return False 

        l += 1 
        r -= 1
        
    return True

print(isPalindrome(s1))     # True
print(isPalindrome(s2))     # False
print(isPalindrome(s3))     # True