import matplotlib.pyplot as plt
import numpy as np
plt.title("Population Density Index")
Total=400
US=74.4
UK=98.4
India=110.8
Germany=66
Australia=13.6
South=36.8
country=[US,South,Australia,Germany,India,UK]
labels=['US','South Korea','Australia','Germany','India','UK']
explode=(.2,0,0,0,0,0)
plt.pie(country,labels=labels,shadow=True,startangle=300,autopct='%.2f %%',pctdistance=0.8,explode=explode)
plt.show()   