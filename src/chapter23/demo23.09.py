# NumPy数组：数组转换
from numpy import *

a = array([1,2,3,4,5,6])
b1 = a.tolist()
print(b1)
print(type(b1))
print('---------------')
b2 = a.reshape(2,3)
print(b2)
print(type(b2))
b2 = b2.tolist()
print(b2)
print(type(b2))


