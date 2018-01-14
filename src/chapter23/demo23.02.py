# NumPy数组--创建多维数组

from numpy import *

a = arange(5)
print(a)
print(a.shape)
print(a.shape[0])

m1 = array([arange(3),arange(3),arange(3)])
print(m1)

m2 = array([arange(3),arange(3)])
print(m2)

m3 = array([["a","b",4],[1,2,3],[5.3,5,3]])
print(m3)

print(m2.shape)
print("{}是{}维数组".format("m2", len(m2.shape)))

print(m2.shape[0])
print(m2.shape[1])