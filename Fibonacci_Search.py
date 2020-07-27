# Fibonacci search with n function evaluations to minimize an univariate objective function in the interval [a,b] 

import math

def fibonacci_search(a, b, n):
    s = (1-5**0.5)/(1+5**0.5)
    p = 1 / (1.61803*(1-s**(n+1))/(1-s**n)) # find the ration of consecutive fibonacci element .... golden ratio = 1.61803
  
    for i in range(n):
        x1 = (a+(b-a)*(1-p))
        x2 = (a+(b-a)*p)
        yx1 = f(x1)
        yx2 = f(x2)
        if yx1<yx2:
            a = a
            b = x2
        else:
            a = x1
            b = b
        print([a,b])
    return [a,b]

 
def f(x):
    return math.exp(x-2)-x 
print(fibonacci_search(-2, 6, 40))
