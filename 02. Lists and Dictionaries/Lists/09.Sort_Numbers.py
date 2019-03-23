n = [float(x) for x in input().split(' ')]
n.sort()

print(' <= '.join('{0:g}'.format(x) for x in n))
