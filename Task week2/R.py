for i in range(7):
    for j in range(5):
        if( (i==0 and j!=4) or(j==0 and i!=0)or(i==7//2 and j!=4)or(j==4 and i!=0 and i<7//2)or(i==4 and j==2) or(i==5 and j==3)or(i==6 and j==4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()