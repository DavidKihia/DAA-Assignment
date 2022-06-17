# A program to compare two factorial functions and determine the efficient one


import time

for i in range(0, 2):

    start_1 = time.time()


    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n - 1)


    num_input = int(input('Enter number to find factorial: '))
    print(fact(num_input))

    time.sleep(3)

    stop_1 = time.time()

    execution_time = stop_1 - start_1

    print("Execution time: ", execution_time)

    start = time.time()


    def fact(n):
        product = 1

        for i in range(n):
            product = product * (i + 1)
            return product


    num_input = int(input('Enter number to find factorial: '))
    print(fact(num_input))

    time.sleep(3)

    stop = time.time()

    execution_time_2 = stop - start

    print("Execution time: ", execution_time_2)

    if execution_time_2 < execution_time:
        print("Student 2 algorithm is more efficient.")
    else:
        print("Student 1 algorithm is more efficient.")
