import random 
import string 

res=[]
allchar=string.ascii_letters+string.digits
for i in range(4): 
    res.append(random.choice(string.digits)) 
for i2 in range(6): 
    res.append(random.choice(allchar))
random.shuffle(res)
print(''.join(res))
