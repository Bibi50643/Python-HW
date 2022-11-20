import random 
n=50
list=[]
for a in range(1,n+1):
    for b in range(1,a+1):
        for c in range(1,b+1):
            if b+c>a:
                m=0.5*pow(2* b**2+2* c**2-a**2,0.5)
                if m==int(m):
                    list.append(a)
print(len(list))

