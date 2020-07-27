# Fibonacci search with n function evaluations to minimize an univariate objective function in the interval [a,b] 

import math

def fibonacci_search(a, b, n):
  
    for i in range(n,1,-1):
        phi =1.61808
        p = (int(round((phi**i - (1-phi)**i) / 5**0.5)))/(int(round((phi**(i+1) - (1-phi)**(i+1)) / 5**0.5))) # find the ration of consecutive fibonacci element .... golden ratio = 1.61803
        print(p)
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
print(fibonacci_search(-2, 6, 50))
