n = input().lower().split()

dct = {}
order = []
result = []

for x in n:
    if x not in dct:
        dct[x] = n.count(x)
        order.append(x)

for x in order:
    if dct[x] % 2 == 1:
        result.append(x)

print(', '.join(result))
