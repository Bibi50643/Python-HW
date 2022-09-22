n=int(input())
f=int(n/100)
m=int((n%100)/10)
l=n%10
if f<m and m<l and f<l:
    print("Yes")
else:
    print("No")