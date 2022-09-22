numbers=list(map(int,input("Enter six number:").split()))
odd=[]
even=[]
for i in numbers:
    if(i%2==1):
        odd.append(i)
    else:
        even.append(i)
odd.sort()
for i in odd:
    print(odd[0])
    break 
if i not in odd:
    print("not found")   

