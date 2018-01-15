# NumPy常用函数：成交量加权平均价格
from numpy import *

price, weights=loadtxt('data.csv', delimiter=',', usecols=(6,7),unpack=True)
print(price)
print(weights)

vwap = average(price, weights = weights)
print('vwap','=', vwap)
