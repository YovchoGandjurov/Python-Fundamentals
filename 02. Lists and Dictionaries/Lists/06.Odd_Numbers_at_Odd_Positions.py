n = [int(x) for x in input().split(' ')]

for x, y in enumerate(n):
    if x % 2 == 1 and y % 2 == 1:
        print('Index {} -> {}'.format(x, y))
