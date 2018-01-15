# NumPy数组：分割数组
from numpy import *
a = arange(8).reshape(4,2)

c = vsplit(a,4)
print(c)
print("---------")
print(c[0].shape)
print("---------")
print(c[0])
print("---------")
print(c[2])

