"""
In this program, there are two for loops that iterate the list items. The complexity of the algorithm
therefore becomes O(2n). Linear complexity goes to infinity so in this case it's double infinity
but infinity is still infinity so the constant is ignored. The graph also remains the same.
"""


def linear_algo(items):
    for item in items:
        print(item)

    for item in items:
        print(item)


print(linear_algo([2, 4, 6, 8, 10]))
