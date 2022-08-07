class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_string = ""
        
        for i in range(len(s)):
            if s[i].isalnum():
                new_string += s[i]
            
        left = 0
        right = len(new_string) - 1
        new_string = new_string.lower()
        copy_new_string = new_string 
        new_string = list(new_string)
        
        if len(new_string) == 1:
            return True
        
        while left < right:
            temp = new_string[left]
            new_string[left] = new_string[right]
            new_string[right] = temp
            left += 1
            right -= 1
            
        if copy_new_string == "".join(new_string):
            return True
        else:
            return False
        
        