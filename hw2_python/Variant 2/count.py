word=str(input())
for i in sorted(set(word)):
    print(f'{i}, {word.count(i)}')