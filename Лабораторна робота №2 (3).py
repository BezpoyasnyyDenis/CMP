from scipy.misc import derivative 

def f(x): 
    return 3*x**4 + 4*x**3 - 12*x**2 -5 

a = -3 
b = -2 
eps = 0.0001 
 
def hord (a, b, eps): 
    if abs(b - a) < eps: 
        print('Корнея намає') 
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
hord (a, b, eps) 