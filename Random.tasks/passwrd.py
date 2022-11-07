import random 
import string 

passwrd=[] 
allchar=string.ascii_letters+string.digits+string.punctuation 
for i in range(2): 
    passwrd.append(random.choice(string.ascii_uppercase)) 
for i1 in range(1): 
    passwrd.append(random.choice(string.digits)) 
for i2 in range(1): 
    passwrd.append(random.choice(string.punctuation)) 
for i3 in range(6): 
    passwrd.append(random.choice(allchar))

random.shuffle(passwrd) 
print("".join(passwrd))
