n = [x for x in input().split(' ')]

new_lst = [n[-1]]

for x in n[:-1]:
    new_lst.append(x)

print(' '.join(new_lst))
