import matplotlib.pyplot as plt
import numpy as np
import random
x=np.linspace(0,0.6,30) 
y=np.array([i+np.random.uniform(-0.06,0.06) for i in x]) 
plt.scatter(x,y,color='green')
plt.plot(x,x,color='black')

plt.title('Best fit line using regression method')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
