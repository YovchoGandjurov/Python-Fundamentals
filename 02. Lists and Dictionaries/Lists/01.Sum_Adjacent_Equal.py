n = [float(x) for x in input().split(' ')]
flag = 1

while flag == 1:
    flag = 0

    for index in range(len(n) - 1):
        if index + 1 > len(n) - 1:
            break
        if n[index] == n[index+1]:
            n[index] = n[index] * 2
            n.pop(index+1)
            flag = 1

n = ['{0:g}'.format(x) for x in n]
print(n)
