n=int(input())
k=int(input())

for i in range(n):
    for j in range(k):
        if i==j or i!=j:
            print("A",end=" ")
    print()
