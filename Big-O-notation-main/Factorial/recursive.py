"""
This function calculates the factorial of a number using recursive functions
"""


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
