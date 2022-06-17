# This is a program to calculate roots of a function using Bisection method
# f = function
# n = Number of iterations
# a = Upper_bound
# b = Lower_bound


def roots(f, a, b, N):
    if f(a)*f(b) >= 0:
        print("Error!")
        return None
    a_n = a
    b_n = b

    for n in range(1, N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if(f(a_n)*f_m_n<0):
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Solution found.")
            return m_n
        else:
            print("Error")
            return None
    return (a_n + b_n)/2


a = int(input('Input Upper-bound: '))
b = int(input('Input Lower-bound: '))
N = int(input('Input number of iterations: '))
f = lambda x: x**2-x-1
print(roots(f, a, b, N))
    
