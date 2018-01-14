from numpy import arange

def sum(n):
    a = arange(n) ** 2   # 数组的每个元素2次方
    b = arange(n) ** 4   # 数组的每个元素4次方
    c = a + b
    return c
print(arange(5))
print(arange(5) ** 2)     # [ 0  1  4  9 16]
print(arange(5) ** 4)     # [  0   1  16  81 256]
print(sum(5))
