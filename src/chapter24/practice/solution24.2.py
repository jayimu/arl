import numpy as np
import matplotlib.pyplot as plt

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(16,8))
ax1.pie([100,200,60])
ax2.bar([100,200,300,400],[100,200,300,100],width = 6)
plt.show()








