# 在同一个窗口绘制直方图和盒状图

import numpy as np
import matplotlib.pyplot as plt


data = np.random.randn(100)
print(data)
print(np.average(data))

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(8,8))
ax1.hist(data,100)
ax2.boxplot(data)

plt.show()








