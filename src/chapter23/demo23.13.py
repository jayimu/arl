from numpy import *

h,l=loadtxt('data.csv', delimiter=',', usecols=(4,5),unpack=True)

print('highest', '=', max(h))
print('lowest','=', min(l))

print('范围','=',max(h) - min(h))
print('范围','=',ptp(h))

