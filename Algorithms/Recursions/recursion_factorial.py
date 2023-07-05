def findFactorialRecursive(number):
    if number == 0:
        return 1
    elif number == 2:
        return 2
    else:
        return number * findFactorialRecursive(number - 1)


def findFactorialIterative(number):
    fact = 1
    for i in range(2, number + 1):
        fact *= i
    print(fact)

# findFactorialIterative(1)

result = findFactorialRecursive(5)
print(result)