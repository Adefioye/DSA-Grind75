from collections import Counter
def isLetterConstructibleFromMagazine(letter, magazine):

    # Get a freq map for letter
    charFreqFromLetter = Counter(letter)

    # Iterate through magazine abd be sure all chars
    # in letters are in there
    for char in magazine:

        if char in charFreqFromLetter:
            charFreqFromLetter[char] -= 1 

            if charFreqFromLetter[char] == 0:
                del charFreqFromLetter[char]

            if not charFreqFromLetter:
                return True 
            
    return not charFreqFromLetter

print(isLetterConstructibleFromMagazine("a", "b"))
print(isLetterConstructibleFromMagazine("aa", "ab"))
print(isLetterConstructibleFromMagazine("aa", "aab"))

# Pythonic solution (Simple and crisp)
print(not (Counter("aa") - Counter("aab")))