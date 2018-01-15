from numpy import *
a = arange(20).reshape(5,4)
a = hsplit(a,2)
print(a)
savetxt('a.txt', a[0],fmt='%d',delimiter=';')
savetxt('b.txt', a[1],fmt='%d',delimiter=';')

