from numpy import *

a = arange(15).reshape(5,3)
b = arange(10).reshape(5,2)
print(a)
print(b)
print(hstack((a,b)))