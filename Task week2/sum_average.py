sum=0
avr=0
while True:
    n=int(input())
    if n==0:
        break
    sum+=n
    avr+=1
print("Sum of n integers is:",sum)
print("Average of n integers is:",sum/(avr))

