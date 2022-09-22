def findall(list):
    return [x for x in range(len(list)) if list[x] == "a"]

word = input()
print(findall(word)) 