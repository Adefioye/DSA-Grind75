import math

n1 = 10 
n2 = 18

# trial-division approach
# time = ~O(n ^ (3/2)) space = O(n)
def generateAllPrimes(n):
    res = []
    divisorFlag = False
    for i in range(2, n + 1):

        squareRoot = math.floor(i ** (1/2))

        for j in range(2, squareRoot + 1):

            if i % j == 0:
                divisorFlag = True
                break
        
        # print(i, divisorFlag)
        if not divisorFlag:
            res.append(i)
        
        divisorFlag = False

    return res

print(generateAllPrimes(n1))
print(generateAllPrimes(n2))