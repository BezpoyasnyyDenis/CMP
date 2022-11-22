import numpy as np 
import math 
from scipy.misc import derivative 

def f(x): 
    return 3*pow(x,4) + 4*pow(x,3) - 12*pow(x,2) - 5 

a = 1  
b = 2 
eps = 0.0001 

def nuton(a,b,eps): 
    df2 = derivative(f, b, n = 2) 
    if (f(b)*df2>0): 
        xi = b 
    else: 
        xi = a 
    df = derivative(f, xi, n = 1) 
    xi_1 = xi - f(xi)/df 
    while (abs(xi_1 - xi)>eps): 
        xi = xi_1 
        xi_1 = xi - f(xi)/df 
    return print ('Solving the equation by Newton*s method x = ', xi_1) 

nuton (a, b, eps) 