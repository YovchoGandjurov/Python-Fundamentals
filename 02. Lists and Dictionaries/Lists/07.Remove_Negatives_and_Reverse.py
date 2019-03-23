n = [int(x) for x in input().split(' ')]
lst = []

for x in n:
    if x >= 0:
        lst.append(x)
lst.reverse()
if len(lst) == 0:
    print('empty')
else:
    for x in lst: 
        print(x, end=" ")
