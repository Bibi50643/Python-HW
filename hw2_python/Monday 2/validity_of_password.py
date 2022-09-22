r4 =  r1 = r2 = r3 = False
s = "6sdf@$Ae"
for i in s:
        if (i.islower()):
            r4 = True         
        if (i.isupper()):
            r1 = True      
        if (i.isdigit()):
            r3 = True      
        if(i=='@'or i=='$' or i=='_'):
            r2 = True          
if(r4 and r1 and r2 and r3 and 6 <= len(s) <= 12):
    print("Valid Password")
else:
    print("Invalid Password")