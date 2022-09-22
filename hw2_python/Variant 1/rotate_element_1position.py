num = int(input())
list = []
for i in range(num):
    word = input()
    list.append(word)
print(list)
new_list = list[num-1]
for i in range(num-1,0,-1):
    list[i] = list[i-1]
list[0] = new_list
print( list)