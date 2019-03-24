n = map(float, input().split(' '))

counts = {}

for x in n:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

for x in sorted(counts):
    print("{} -> {} times".format(x, counts[x]))
