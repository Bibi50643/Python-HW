import re
from string import punctuation
data = open('wordlist.txt','r').read().split("\n")
#a
ime =[]
for i in range(len(data)):
    if len(data[i]) >3:
        words = re.sub(f"[{punctuation}]", " ", data[i]).split()
        for each in words:
            if each[-3:] == "ime":
                ime.append(each)
print(ime)
# c)
letters =["r", "s", "t", "l", "n", "e"]
count =[]
for i in range(len(data)):
     for dt in letters:
         if data[i] not in count:
            if dt in data[i]:
               count.append(data[i])
print(len(count))

#d)
print(len(count)/len(data) * 100)

