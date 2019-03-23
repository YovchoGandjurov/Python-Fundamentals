n = [x for x in input().split(' ')]
counter = 0

for x in n:
    if int(x) % 2 == 1:
        counter += 1

print(counter)
