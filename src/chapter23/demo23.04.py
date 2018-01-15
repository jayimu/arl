# NumPy数组：改变数组的维度
from numpy import *
b = arange(24).reshape(2,3,4)
print(b)
print('------------------')
# reshape、resize、ravel、flatten、transpose、元组
# 方法1：使用ravel
b1 = b.ravel()
print(b1)
print('------------------')
# 方法2：使用flatten
b2 = b.flatten()
print(b2)
print('------------------')


b.shape = (6,4)
print(b)
print('------------------')
# 方法3：transpose
b3 = b.transpose()
print(b3)
print('------------------')

# 方法4：resize方法
# resize和reshape
b.resize((2,12))
print(b)
