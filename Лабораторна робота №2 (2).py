import numpy as пр 
import math 
 
def f(x) : 
    return 3*pow(x,4) + 4*pow(x,3) - 12*pow(x,2) - 5 
eps = 0.0001 

def rec_dyhotomy(a,b,eps): 
    if abs(f(b) - f(a)) < eps: 
        print('Кореня немає') 
        return 
    mid = (a+b) / 2 
    if f(mid) == 0 or abs(f(mid)) < eps: 
        print(f'Корінь знаходиться в точці x = {mid}') 
    elif f(a)*f(mid) < 0: 
        rec_dyhotomy(a, mid, eps) 
    else: 
        rec_dyhotomy(mid, b, eps) 

rec_dyhotomy(-3, -2, eps) 
rec_dyhotomy(1, 2, eps) 

 