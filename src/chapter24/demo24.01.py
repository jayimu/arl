import matplotlib.pyplot as plt

X = range(-100,101)

Y = [x ** 2 for x in X]

plt.plot(X,Y)
plt.savefig('result1.jpg')
plt.show()
