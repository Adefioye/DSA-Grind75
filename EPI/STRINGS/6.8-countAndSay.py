
def countAndSay(n: int) -> str:

    res = "1"
    if n == 1:
        return res 

    nextNumber = 1
    temp = ""
    while nextNumber < n:
        count = 1

        for i in range(len(res)):
            if i + 1 < len(res) and res[i + 1] == res[i]:
                count += 1 
            else:
                temp += (str(count) + res[i])
                count = 1

        res = temp 
        nextNumber += 1 
        temp = ""

    return res 

print(countAndSay(1))
print(countAndSay(3))
print(countAndSay(5))
print(countAndSay(7))
print(countAndSay(9))
print(countAndSay(10))
    

