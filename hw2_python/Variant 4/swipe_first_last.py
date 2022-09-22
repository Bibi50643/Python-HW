#341=>143
number=int(input())
first=int(number/100)
last=number%10
swap=(((last*100)+(number%100))-last)+first
print(swap)
