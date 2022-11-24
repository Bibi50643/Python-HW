import matplotlib.pyplot as plt
import numpy as np
x=np.array([43,47,63,68,68,8,82,20,36,88,70,88,88,11,59,65,39,88,45,88,80,38,25,78,71,10,20,80,70,80])
plt.plot(x,color='blue',marker='^',label='a')
plt.title('This is the Title')
plt.xlabel('This is X axis')
plt.ylabel('This is Y axis')
plt.legend()
plt.grid()
plt.show()