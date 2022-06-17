"""
A function is said to be exponential if the steps used in an algorithm doubles with each set of input data.
A good example of this is in the calculation of fibonacci numbers using recursive functions.
"""


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


terms = int(input('How many terms?: '))
if terms <= 0:
    print('Please enter a positive integer')
else:
    print('Fibonacci series')
    for i in range(terms):
        print(fib(i))



