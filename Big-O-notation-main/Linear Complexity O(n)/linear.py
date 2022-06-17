"""
The complexity of an algorithm is said to be linear if the time required to complete the execution
increases or decreases linearly with the number of inputs.
"""


def linear_algo(items):
    for item in items:
        print(item)


print(linear_algo([2, 4, 6, 8, 10]))
