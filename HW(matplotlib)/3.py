import matplotlib.pyplot as plt
import math 
import numpy as np
x=np.linspace(-math.pi,math.pi,256)

plt.plot(x,np.sin(x),c='green')
plt.plot(x,np.cos(x),c='red')
plt.plot(x,-np.sin(x),c='blue')
plt.plot(x,-np.cos(x),c='orange')
plt.grid(True)

plt.show()


