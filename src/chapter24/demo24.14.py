import numpy
import matplotlib.pyplot as plt
X = numpy.linspace(-4,4,1024)
Y = .25 * (X + 4) * (X + 1) * (X - 2)
# 设置LaTex格式的标题
plt.title(r'$f(x) = \frac{1}{4}(x+4)(x+1)(x-2)$')
#  绘制蓝色的曲线
plt.plot(X,Y, c='b')
plt.show()
