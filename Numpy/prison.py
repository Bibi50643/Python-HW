import numpy as np
import random 
def random_prisoner():
    len=random.randint(3, 8)
    prisoners=[random.choice([0, 1]) for i in range(len)]
    return prisoners

def cnt(prisoners):
    res=0
    x=1
    if prisoners[0]==0:
        return 0
    else: 
        for i in range(len(prisoners)):
            if prisoners[i]==x: 
                continue
            else: 
                x=0 if x==1 else 1
                res+=1
    return res+1
a=random_prisoner()
print(a)
print(cnt(a))
print(cnt([1, 1, 1]))
print(cnt([0, 0, 0]))

