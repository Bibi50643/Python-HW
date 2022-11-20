count=0
list=[]
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i==j and j==k:
                list.append(3)
            elif i==j or j==k:
                list.append(2)
            else:
                list.append(1)
            print(i,j,k)
res=0
for i in list:
    res+=i
print(res)