# NumPy常用函数：读写CSV文件
from numpy import *

a = arange(20).reshape(4,5)
print(a)
savetxt('a.txt', a, fmt='%d', delimiter=',')
print('---------------')
b = loadtxt('a.txt', dtype=int, delimiter=',', usecols=(1,3,4))
print(b)
print('---------------')
x,y = loadtxt('a.txt', dtype=int, delimiter=',',usecols=(1,4),unpack=True)
print(x)
print('---------------')
print(y)
