# Given a number N return the index value of Fibonacci sequence

def FibonacciIterative(index): # O(n) linear time
    if index < 2:
        return index
    a = 0
    b = 1
    series = 0
    for i in range(index - 1):
        series = a + b
        a = b
        b = series
    return series

result = FibonacciIterative(40)
print(result)


def FibonacciRecursion(index): # O(2^n) it is exponential
    if index < 2:
        return index
    return FibonacciRecursion(index - 1) + FibonacciRecursion(index - 2) # Every term in fibonacci sequence = sum of previous two terms

# result = FibonacciRecursion(40)
# print(result)




#                                 _______________________7____________________________
#                                 |                                                  |
#                                 6                                                  5
#                    _____________|____________                         _____________|____________
#                   |                         |                         |                        |
#                   5                         4                         4                        3
#         __________|______                ___|_____                ____|____                 ___|___
#         |               |                |       |                |        |                |     |
#         4               3                3       2                3        2                2     1
#     ____|___        ____|____         ___|___                  ___|___
#     |       |       |        |        |     |                  |     |
#     3       2       2        1        2     1                  2     1
# ____|____
# |       |
# 2       1