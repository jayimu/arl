# 在数据可视化过程中使用NumPy

# 绘制正弦曲线（sin）

import math
import matplotlib.pyplot as plt
import numpy

X = numpy.linspace(0, 2 * numpy.pi, 100)
print(type(X))

Y = numpy.cos(X)
plt.plot(X,Y)
plt.show()


