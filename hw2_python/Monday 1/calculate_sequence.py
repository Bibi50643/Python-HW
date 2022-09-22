n = int(input())
l = 1
sum = 0
for i in range(1, n + 1):
      i = l
      x = 1
      for j in range(i, 2*i+1):
             x *= j
             l = j
      sum += x
print(sum)