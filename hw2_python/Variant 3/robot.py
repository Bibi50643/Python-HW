from math import sqrt
def robot(x):
    pos = [0,0]
    for i in x:
        y = i.split()
        upper=y[0].upper()
        z=int(y[1])
        if upper == "UP":
            pos[0] += z
        elif upper == "DOWN":
            pos[0] -= z
        elif upper == "RIGHT":
            pos[1] += z
        elif upper == "LEFT":
            pos[1] -= z
     
    return round(sqrt(pos[0]**2+pos[1]**2))

x = ("UP 5", "DOWN 3", "LEFT 3", "RIGHT 2")
print(robot(x))
