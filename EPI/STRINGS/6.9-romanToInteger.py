def romanToInt(s: str) -> int:

    i = 0
    res = 0 
    romanToNumMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }

    while i < len(s):

        if i + 1 < len(s) and romanToNumMap[s[i + 1]] > romanToNumMap[s[i]]:
            res += romanToNumMap[s[i + 1]] - romanToNumMap[s[i]] 
            i += 2
        else:
            res += romanToNumMap[s[i]] 
            i += 1 

    return res 

print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))