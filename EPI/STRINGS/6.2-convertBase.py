import string

num = "-615"; b1 = 7; b2 = 13 

def baseConversion(numAsStr, b1, b2):

    def convertToBase(numAsInt, base):

        if numAsInt == 0:
            return ""
        
        return (
            convertToBase(numAsInt // base, base) + 
            string.hexdigits[numAsInt % base].upper()
        )

    isNeg = numAsStr[0] == "-"
    numAsStr = numAsStr[isNeg:]
    numAsInt = 0 

    for c in numAsStr:
        numAsInt = numAsInt * b1 + string.hexdigits.index(c.lower()) 

    return (("-" if isNeg else "") + 
            ("0" if numAsInt == 0 else convertToBase(numAsInt, b2)))

print(baseConversion(num, b1, b2))
