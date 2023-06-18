class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0

        if len(s)==1 and not s[0].isdigit():
            return 0

        i = 0
        sign = 1
        if s[i]=="+":
            i+=1
        if s[i]=="-":
            sign = -1
            i+=1

        # To handle + and - showing up together
        if i==2:
            return 0

        parsed = 0
        while i<len(s):
            if not (s[i]).isdigit():
                break
            else:
                parsed = parsed*10 + int(s[i])
            i+=1

        parsed = sign*parsed
        
        if parsed>2**31-1:
            return 2**31-1
        elif parsed<=-2**31:
            return -2**31
        else:
            return parsed












string1 = "-314"
int1 = -314 

import string

string.ascii_letters

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