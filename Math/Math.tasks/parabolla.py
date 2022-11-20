import math as m 
K=int(input("K: ")) 
X=int(input("X: ")) 
amount=0
for k in range(1,K+1): 
    for a in range((-1)*X,X): 
        for b in range((-1)*X,X): 
            for c in range((-1)*X,X+1): 
                if a<b<c:
                    A_coordinate=[] 
                    B_coordinate=[] 
                    C_coordinate=[] 
                    A_coordinate.append(a) 
                    A_coordinate.append((a**2)/k ) 
                    B_coordinate.append(b) 
                    B_coordinate.append((b**2)/k ) 
                    C_coordinate.append(c) 
                    C_coordinate.append((c**2)/k )  
                    BC=m.dist(B_coordinate,C_coordinate) 
                    AC=m.dist(A_coordinate,C_coordinate) 
                    AB=m.dist(A_coordinate,B_coordinate) 
                    angles=[]
                    angle1=int(m.degrees(m.acos((AC**2+AB**2-BC**2)/(2*AC*AB))))
                    angle2=int(m.degrees(m.acos((BC**2+AB**2-AC**2)/(2*BC*AB))))
                    angle3=int(m.degrees(m.acos((AC**2+BC**2-AB**2)/(2*AC*BC))))
                    angles.append(angle1) 
                    angles.append(angle2) 
                    angles.append(angle3) 
                    amount=amount+angles.count(45)
print(amount)


