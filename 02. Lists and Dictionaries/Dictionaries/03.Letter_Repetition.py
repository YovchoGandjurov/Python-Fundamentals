n = input()
dct = {}

for x in n:
    if x in dct:
        dct[x] += 1
    else:
        dct[x] = 1

for key, value in dct.items():
    print('{} -> {}'.format(key, value))
