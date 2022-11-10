import numpy as np
field1=[
  ["-", "-", "-", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"]]
def num_grid(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]=='-':
                a[i][j]=0

    for i in range(len(a)):
        for j in range(len(a[0])):
                if a[i][j]=='#':
                    if i>0 and j>0:
                        for x in range(i-1,i+2):
                            for y in range(j-1,j+2):
                                # if x==i and y==j:
                                if a[x][y] == "#":
                                    continue
                                a[x][y]+=1
                    elif i==0 and j>0:
                        for x in range(i,i+2):
                            for y in range(j-1,j+2):
                                if a[x][y] == "#":
                                    continue
                                a[x][y]+=1
                    elif i>0  and j>0:
                        for x in range(i-1,i+1):
                            for y in range(j,j+1):
                                if a[x][y] == "#":
                                    continue
                                a[x][y]+=1
                    elif i==0 and j==0:
                        for x in range(i,i+2):
                            for y in range(j,j+2):
                                if a[x][y] == "#":
                                    continue
                                a[x][y]+=1
                    elif i==len(a)-1 and j==0:
                        try:
                            for x in range(i-1,i):
                                for y in range(j,j+1):
                                    if a[x][y] == "#":
                                        continue
                                    a[x][y]+=1
                        except: pass

    res=np.array(a)
    return res
print(num_grid(field1))
