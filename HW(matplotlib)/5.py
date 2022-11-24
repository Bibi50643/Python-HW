import matplotlib.pyplot as plt
import numpy as np

x=[21,30.3,17.7,10.7,10.2,10.2]
labels=["Australia", "Italy", "Ireland", "Iceland", "Greece", "Germany" ]
plt.pie(x, autopct='%.0f%%',labels=labels)
plt.legend()
plt.show()
