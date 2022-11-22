import numpy as numpy 
from scipy.misc import derivative 

def f(x): 
    return 3*pow(x,4) + 4*pow(x,3) - 12*pow(x,2) - 5 

a = -3 
b = -2 
eps = 0.0001 
df2 = derivative(f, b, n = 2) 
df = derivative(f, a, n = 1) 
g = df * df2 

def nuton(a, b, eps): 
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
    return print ('Solving the enquation by Newton*s method x = ', xi_1) 

def hord (a, b, eps): 
    if abs(b - a) < eps: 
        print('Кореня немає') 
        return 
    if (f(a)*derivative(f, a, n = 2)): 
        x0 = a 
        xi = b 
    else: 
        x0 = b 
        xi = a 
    xi_1 = xi - (xi - x0) * f(xi)/(f(xi) - f(x0)) 
    while (abs(xi_1 - xi) > eps): 
        xi = xi_1 
        xi_1 = xi - (xi - x0) * f(xi)/(f(xi) - f(x0)) 
    else: 
        print(f'Корінь знаходиться в точці х = ', xi_1) 
         
def combine (a, b, eps): 
    if (g > 0): 
        hord (a, b, eps) 
    else: 
        nuton (a, b, eps) 
            
combine(a, b, eps) 