import numpy as np
g1=np.array([("001"),("002"),("003")])
g2=np.array([("00000"),("01006"),("02000"),("30050"),("00004")])
g3=np.array([("00020000"),("01000000")])

def shortest_path(grid):
    max_elment=1
    for i in grid:
        for j in i:
            if max_elment<int(j):
                max_elment=int(j)
    coord=1
    if max_elment==1:
        return 0
    else:
        shag=0
        for coord in range(1,max_elment):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if int(grid[i][j])==coord:
                        x1=i
                        y1=j
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if int(grid[i][j])==coord+1:
                        x2=i
                        y2=j
            sub=abs(x1-x2)+abs(y1-y2)
            shag+=sub                        
        return shag

print(shortest_path(g1))
print(shortest_path(g2))
print(shortest_path(g3))
