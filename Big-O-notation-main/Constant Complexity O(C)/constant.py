"""
The complexity of an algorithm is said to be constant if the time required to complete the execution
of the algorithm is constant, irrespective of the number of inputs.
"""


def const_algo(items):
    prod = items[0] * items[0]
    return prod


print(const_algo([2, 5, 9, 1, 8, 7, 10]))
