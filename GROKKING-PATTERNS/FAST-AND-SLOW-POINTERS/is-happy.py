num1 = 19   #`True
num2 = 2    # false

def square(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** 2
        n = n // 10

    return total


def is_happy(num):

    slow, fast = num, num

    while True:
        slow = square(slow)
        fast = square(square(fast))

        if slow == fast:
            break 

    return True if slow == 1 else False

print(is_happy(num1))
print(is_happy(num2))