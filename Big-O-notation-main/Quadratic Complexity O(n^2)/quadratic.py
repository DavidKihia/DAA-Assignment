"""
An algorithm is said to be quadratic if the number of steps used are a quadratic function of
the number of items in the inputs.
"""


def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item2)


print(quadratic_algo([2, 4, 6, 8, 10]))
