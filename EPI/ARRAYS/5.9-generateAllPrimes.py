import math

n1 = 10 
n2 = 18

def countPrimes(n: int) -> int:

    primeCount = 0

    if n <= 2:
        return primeCount 

    tab = [True] * (n) 
    tab[0] = False 
    tab[1] = False 

    for i in range(2, n):

        if tab[i]:
            primeCount += 1 

            # Sieve out multiples of i
            for j in range(i, n, i):
                tab[j] = False

    return primeCount

print(countPrimes(n1))
print(countPrimes(n2))

# trial-division approach
# time = ~O(n ^ (3/2)) space = O(n)
# def generateAllPrimes(n):
#     res = []
#     divisorFlag = False
#     for i in range(2, n + 1):

#         squareRoot = math.floor(i ** (1/2))

#         for j in range(2, squareRoot + 1):

#             if i % j == 0:
#                 divisorFlag = True
#                 break
        
#         # print(i, divisorFlag)
#         if not divisorFlag:
#             res.append(i)
        
#         divisorFlag = False

#     return res

# sieving approach (DP)
# time = O(nloglogn) space = O(n) 
# def generateAllPrimes(n):
#     tab = [True] * (n + 1) 
#     res = []

#     for i in range(2, n + 1):

#         if tab[i]:

#             res.append(i)
#             for j in range(i, n + 1, i):
#                 tab[j] = False 

#     return res


# print(generateAllPrimes(n1))
# print(generateAllPrimes(n2))