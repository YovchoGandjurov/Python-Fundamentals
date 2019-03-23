n = [int(x) for x in input().split(' ')]
lst = []
for x in n:
    if x >= 0:
        if x ** 0.5 == int(x ** 0.5):
            lst.append(x)

lst.sort()

for num in lst[::-1]:
    print(num, end=" ")
