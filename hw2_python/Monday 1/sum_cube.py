'''153 = (1*1*1)+(5*5*5)+(3*3*3)
1*1*1=1
5*5*5=125
3*3*3=27
1+125+27=153'''

n=int(input())
x=int(n/100)
y=int((n%100)/10)
z=n%10
if x*x*x+y*y*y+z*z*z==n:
    print("Yes")
else:
    print("No")
