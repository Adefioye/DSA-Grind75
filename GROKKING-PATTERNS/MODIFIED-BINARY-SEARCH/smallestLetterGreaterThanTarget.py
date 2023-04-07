letters1 = ['a', 'c', 'f', 'h']; key1 = 'f'
# Output: 'h'
letters2 = ['a', 'c', 'f', 'h']; key2 = 'b'
# Output: 'c'
letters3 = ['a', 'c', 'f', 'h']; key3 = 'm'
# Output: 'a'
letters4 = ['a', 'c', 'f', 'h']; key4 = 'h'
# Output: 'a'

def smallestLetterGreaterThanTarget(letters, target):
    """
    Smallest letter greater than target
    if present, return the letter, otherwise return first letter in the array
    """
    l, r = 0, len(letters) - 1 

    if target < letters[l] or target >= letters[r]:
        return letters[l]
    
    while l <= r:

        mid = (l + r) // 2 
        if target < letters[mid]:
            r = mid - 1 
        else:
            l = mid + 1 

    return letters[l]

print(smallestLetterGreaterThanTarget(letters1, key1))
print(smallestLetterGreaterThanTarget(letters2, key2))
print(smallestLetterGreaterThanTarget(letters3, key3))
print(smallestLetterGreaterThanTarget(letters4, key4))