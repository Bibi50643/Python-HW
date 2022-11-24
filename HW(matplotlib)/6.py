import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

d3= plt.axes(projection='3d')
z=np.linspace(0, 15, 2000)
x=np.sin(z)
y=np.cos(z)
d3.plot3D(x,y,z,color='black')
z1=15*np.random.random(100)
b=0.1*np.random.randn(100)
x1=np.sin(z1)+b
y1=np.cos(z1)+b
d3.scatter3D(x1,y1,z1,c=z1,cmap='Reds')
plt.show()
