n=int(input("Input first number:"))
k=int(input("Input second number:"))
t=int(input("Input third number:"))

list=[]
list.append(n)
list.append(k)
list.append(t)
list.sort()
sorted(list)
print("The median is:",list[1])