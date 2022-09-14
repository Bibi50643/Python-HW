m=str(input("Input the name of Month:"))

if m =="February":
    print("Number of days: 28/29 days")
elif m=="April" or m=="June" or m=="September" or m=="November":
    print("Number of days:30 days") 
elif  m=="March" or m=="July" or m=="May" or m=="August" or m=="October" or m=="December" or m=="January" :
    print("Number of days:31")
else:
    print("It is not month name")