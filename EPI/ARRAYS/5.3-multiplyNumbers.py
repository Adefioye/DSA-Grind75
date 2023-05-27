num1_1 = [9, 8, 7]; num2_1 = [1, 2, 3 ]
num1_2 = [-9, 8, 7]; num2_2 = [1, 2, 3 ]

def multiply(num1, num2):

    sign = -1 if (num1[0] * num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    res = [0] * (len(num1) + len(num2)) 

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):

            res[i + j + 1] += num1[i] * num2[j]
            res[i + j] += res[i + j + 1] // 10 
            res[i + j + 1] %= 10 

    res = res[next(i for i, num in enumerate(res) if num != 0):]

    return [sign * res[0]] + res[1:]

print(multiply(num1_1, num2_1))
print(multiply(num1_2, num2_2))