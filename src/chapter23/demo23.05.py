# NumPy数组：组合数组(水平组合）
from numpy import *

# A
# B 
# A B  A和B行数相同，列数可以不同
# hstack可以水平组合任意多个数组，但这些数组必须行数相同，否则会抛出异常
a = arange(9).reshape(3,3)
b = a * 3
print(a)
print('----------------')
print(b)
print('----------------')
c = a * 5

print(hstack((a,b)))
print('----------------')
print(hstack((a,b,c)))
