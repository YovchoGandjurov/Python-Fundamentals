n = [float(x) for x in input().split(' ')]
n2 = input()
new_lst = [x * float(n2) for x in n]

for x in new_lst:
    if x == int(x):
        print(int(x), end=' ')
    else:
        print(x, end=' ')
