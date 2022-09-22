# a*x^2+b*x+c=0 find roots//// and consider exceptions,like no roots
import math  
a=int(input())
b=int(input())
c=int(input())
print(a,"x^2 +",b,"x +",c,"= 0")
discriminant=b**2-4*a*c

if discriminant>0:
    root1=(-b+ math.sqrt(discriminant))/2*a
    root2=(-b- math.sqrt(discriminant))/2*a
    print(root1,root2)

if discriminant==0:
    root1=root2=-b/(2*a)
    print(root1)

if discriminant<0:
    print("no roots")