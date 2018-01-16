import numpy
import matplotlib.pyplot as plt
X = numpy.linspace(-6,6,1024)

colors =['red','yellow','b','c','#FF00FF','0.75']
for i in range(20):
    plt.plot(X,-X**2 + (i+1)*2,color=colors[i % len(colors)])
plt.show()