# SOLUTION 1 using arrays

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        new_s = list(s)
        
        if len(s) != len(t):
            return False
        
        for i in range(len(t)):
            cur_char = t[i]
            
            if cur_char in new_s:
                new_s.remove(cur_char)
            else:
                return False
        
        return True if len(new_s) == 0 else False
        

# SOLUTION 2 using hash map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        char_map = {}

        for char in s:
            if char in char_map:
                char_map[char] += 1 
            else:
                char_map[char] = 1 

        for char in t:
            if char not in char_map:
                return False 
            else:
                char_map[char] -= 1

                if char_map[char] == 0:
                    del char_map[char]

        return not char_map