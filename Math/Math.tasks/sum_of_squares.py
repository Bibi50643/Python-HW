import math
n=int(input())

def is_prime(n):
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True
list=[]
if is_prime(n) == True and (n-1)%4==0 and n<150:
    m=int(pow(n,0.5))
    for x in range(m+1):
        y1=n-x*x
        y=int(pow(y1,0.5))
        if y*y == y1:
            list.append(x)
            list.append(y)
else:
    print("Enter another number that matches the condition")

list.sort()
a=list[0]+list[2]
print(a)


