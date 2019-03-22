n = [int(x) for x in input().split(' ')]
count = -1

for x in range(len(n) // 2):
    n[x], n[count] = n[count], n[x]
    count -= 1

print(' '.join([str(x) for x in n]))
