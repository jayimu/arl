# NumPy数组--获取单个数组值和数组的分片
from numpy import *

a = array([[1,2,3],[4,5,6],[7,8,9]])

print(a[0,0])
print("a[0,1] = {}, a[2,1] = {}".format(a[0,1],a[2,1]))

# 分片

print(a[0:1])
print(a[0:1][0])
print(a[0:2])
b = a[0:]
#b[0,0] = 100
print(a)

print(a[0::2])
print(a[-3:-1])
