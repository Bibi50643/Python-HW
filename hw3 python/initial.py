with open("namelist.txt") as names:
    a = names.read().split("\n")
    data = []
    for line in a:
        data.append(line.split())


initial=input("Enter Initial: ")
for name in data:
    if len(initial) >=2:
        if initial[0] == name[0][:1] and initial[1] == name[1][:1]:
           print(" ".join(name))
    else:
        print("Error")
        break




