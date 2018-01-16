import math
import matplotlib.pyplot as plt
import numpy
X = numpy.linspace(0.01, numpy.pi/2, 100)
Y = numpy.tan(X)
print(Y)
Y = 1/Y
plt.plot(X,Y)
plt.show()