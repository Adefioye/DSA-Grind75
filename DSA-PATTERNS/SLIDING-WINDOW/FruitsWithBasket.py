Array1 = ['A', 'B', 'C', 'A', 'C']
Array2 = ['A', 'B', 'C', 'B', 'B', 'C']

def fruitsInBasket(A):
    maxL = float("-inf")
    char_map = {}
    left = 0

    for right in range(len(A)):
        cur_char = A[right]

        if cur_char not in char_map:
            char_map[cur_char] = 1
        else:
            char_map[cur_char] = char_map[cur_char] + 1
            
        while len(char_map.keys()) > 2:
            char_map[A[left]] -= 1

            if char_map[A[left]] == 0:
                del char_map[A[left]]

            left += 1

        maxL = max(maxL, right - left + 1)

    return maxL if maxL != float("-inf") else 0

print(fruitsInBasket(Array1))
print(fruitsInBasket(Array2))
