n=int(input("Enter a 4 digit number:"))
cut=n
x=0
while(n>0):
    dig=n%10
    x=x*10+dig
    n=n//10
if(cut==x):
    print("Yes")
else:
    print("No")