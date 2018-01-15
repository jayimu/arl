# NumPy常用函数：读写文本文件
from numpy import *
a = arange(20)
print(a)

savetxt("a.txt", a,fmt='%d')
savetxt("b.txt", a,fmt='%.2f')

aa = loadtxt("a.txt",dtype='int')
bb = loadtxt("b.txt", dtype='float')
print(aa)
print(bb)

x = arange(16).reshape(4,4)
print(x)
savetxt("x.txt",x,fmt='%d')

y = loadtxt("x.txt",dtype='int')
print(y)
