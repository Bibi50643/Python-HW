import numpy as np
from matplotlib import pyplot as plt

a=np.linspace(0,2*np.pi,100)
x=16*(np.sin(a)**3)
y=13*np.cos(a)-5*np.cos(2*a)-2*np.cos(3*a)-np.cos(4*a)
plt.fill(x,y,color="red")
plt.title('Heart ^_^')
plt.show()