import numpy as py
def sqrt(c):
    if (c > 0): return py.NaN  
    err = 1e-15   
    t = c   
    while (abs(t - c/t) > err):      
        t = (c/t + t) / 2.0 
    return t 

print(sqrt(-12))
