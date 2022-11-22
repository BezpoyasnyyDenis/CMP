import math
x1=73 
x2=7/15 
x1_1 = 8.54 
x2_2 = 0.467 
def f (x1, x1_1, x2, x2_2):
    dx1 = abs((math.sqrt(x1) - x1_1)/ math.sqrt (x1))
    dx2 = abs((x2 - x2_2)/x2)
    if (dx1>dx2):
        print ("Друга рівність точніше")
    else:
        print("Перша рівність точніше")
f(x1,x1_1,x2,x2_2)