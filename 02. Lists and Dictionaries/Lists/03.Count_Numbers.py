n = [int(x) for x in input().split(' ')]
unique = set(n)


for x in sorted(unique):
    if x not in range(0, 1000):
        continue
    else:
        print('{} -> {}'.format(x, n.count(x)))
