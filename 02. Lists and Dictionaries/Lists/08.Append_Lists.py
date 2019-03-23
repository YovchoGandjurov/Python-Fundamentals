n = [x for x in input().split('|')]
n.reverse()
lst = ' '.join(n)
result = [x for x in lst.split(' ')]

for x in result:
    if x != '':
        print(x, end=" ")
