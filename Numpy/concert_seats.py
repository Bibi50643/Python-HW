import numpy as np

list=np.array([[1,2,3],[2,3,4],[5,6,9]])
list=list.T
seats=[]
bool=True
for i in list:
    for j in range(1,len(i)):
        if i[j]<=i[j-1]:
            bool=False
            break
print(bool)