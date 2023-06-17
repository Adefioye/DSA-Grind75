string1 = "-314"
int1 = -314 

import string

def intToStr(num):

    isNeg = False 

    if num < 0:
        num, isNeg = -num, True 

    res = []
    while num:
        res.append(chr(ord("0") + num % 10))
        num //= 10

    return ("-" if isNeg else "") + "".join(res[::-1])

def strToInt(s):

    isNeg = False 

    if s[0] == "-":
        s, isNeg = s[1:], True 

    res = 0
    for c in s:
        res = res * 10 + string.digits.index(c)

    return -res if isNeg else res

print(intToStr(int1))
print(strToInt(string1))