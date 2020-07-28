#Apply the bisection method to fnd an interval containing the minimizer of f starting with the interval [a,b]
import scipy
from scipy import optimize
import numpy as np
import math

def bisection( a, b, eps):
    if a > b: 
        temp = a
        a = b
        b = temp
    f = lambda x:math.exp(x-2)-x
    ya = scipy.optimize.approx_fprime(np.array([a]), f, epsilon=1e-6) 
    yb = scipy.optimize.approx_fprime(np.array([b]), f, epsilon=1e-6) 
    if ya == 0: 
        b = a
    if yb == 0:
        a = b
    while b - a > eps:
        x = (a+b)/2
        y= scipy.optimize.approx_fprime(np.array([x]), f, epsilon=1e-6)
        if y == 0:
            a = x
            b = x
        elif y*ya >0:
            a = x
        else:
            b = x
    return (a,b)
    


print(bisection(-2, 6, 0.001))
