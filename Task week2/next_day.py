import datetime
year=int(input("Input a year:"))
month=int(input("Input a month [1-12]:"))
day=int(input("Input a day [1-31]:"))

d = datetime.date(year,month,day)
next_day= d + datetime.timedelta(days=1)

print(next_day.strftime('%Y-%m-%d'))


