import matplotlib.pyplot as plt
import numpy as np
import random
from mpl_toolkits import mplot3d
x = [random.triangular() for i in range(500)]
y = [random.triangular() for i in range(500)]
z = [random.triangular() for i in range(500)]
ax=plt.axes(projection='3d')
ax.scatter(x,y,0.8,s=2,color='r',alpha=1)
ax.scatter(0.7,x,z,s=2,color='b',alpha=1)
ax.scatter(y,0.2,z,s=2,color='y',alpha=1)
plt.show()