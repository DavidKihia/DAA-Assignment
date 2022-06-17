"""
A function is said to cubic if the number of steps used triples for every item in the
inputs
"""


def cubic_algo(items):
    for item in items:
        for item2 in items:
            for item3 in items:
                print(item, ' ', item2, ' ', item3)


print(cubic_algo([4, 5, 6, 7, 8]))
