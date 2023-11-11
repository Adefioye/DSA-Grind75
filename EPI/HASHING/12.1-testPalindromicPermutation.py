from collections import defaultdict, Counter

s1 = "level"
s2 = "foobaraboof"

def canFormPalindrome(s):
    charMap = defaultdict(int)

    for char in s:
        if char in charMap:
            charMap[char] -= 1
            del charMap[char]
        else:
            charMap[char] += 1

    if len(s) % 2 == 0:
        # No more value in map if all characters are in pair
        return len(charMap) == 0
    
    return set(charMap.values()) == set([1])

def canFormPalindrome2(s):

    """
    A string can form a palindrome, if and only if the
    frequency of odd characters in string is at most one
    """
    sumOfOddChars = sum(v % 2 for v in Counter(s).values())
    print(sumOfOddChars)
    return sumOfOddChars <= 1

print(canFormPalindrome2(s1))
print(canFormPalindrome2(s2))
