import numpy as np
s=str(input("Enter secret password:"))
p1=s[0:3] 
p2=s[3:6] 
p3=s[6:9] 
a=list(p1)
b=list(p2)
b=list(p3)
def secret_password(s):
    if s==s.lower() and len(s)==9:
        res1=p2[::-1]
        res3=[]
        for i in range(0,len(a)):
            if i==0 or i==2:
                res3.append(ord(a[i])-96)
            else:
                res3.append(a[i])
        pa3="".join(str(x) for x in res3) 
        res2=[]
        for i in range(0,len(b)):
            if b[i]=='z':
                res2.append('a')
            else:
                res2.append(chr(ord(b[i])+1))
        pa2="".join(str(x) for x in res2)
        pa1="".join(str(x) for x in res1)
        print(pa1+pa2+pa3)
    else:
        print("BANG!BANG!BANG!")
    return 0
secret_password(s)
