import numpy as np 
from scipy import optimize 
from scipy.misc import derivative 
import math 

x0 = 3.5 
y0 = -0.5 
delta = 0.1 

def f1(y): 
    return math.cos(y) + 3 
def f2 (x): 
    return 0.5 - math.cos(x - 1)  
 
def iter (x,y,e): 
    xn = x 
    yn = y 
    xn1 = f2(x) 
    yn1 = f1(y) 
    n = 1 
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)): 
        xn = xn1 
        yn = yn1 
        xn1 = f2(yn)   
        yn1 = f1(xn) 
        n += 1 
    print ('Simple iteration:') 
    print ('x=', xn, '\ny=',yn,'\nThe amount of iteration = ',n) 
iter(x0,y0,0.0001) 

def f3(x):  
    return math.cos(x[0] - 1) + x[1] - 0.5 , x[0] + math.cos(x[1]) - 3 
s = optimize.root(f3, [0.,0.], method = 'hybr') 
print ('Check',s.x) 