n = int(input())
sequence = 3
for i in range(3, n + 1):
    x = 1
    for j in range(1, i + 1):
        x *= j
    sequence += i * 2 * x
print(sequence)

