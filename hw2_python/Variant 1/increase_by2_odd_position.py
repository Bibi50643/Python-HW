#given not a string 5 digit number increase by 2 times the numbers in odd position
number=int(input())
first_pos=int((number/1000)%10)
third_pos=int(((number%1000)%100)/10)

c=first_pos*1000+third_pos*10
print(number+c)