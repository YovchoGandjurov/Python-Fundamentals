dct = {}

while True:
    inp = input()
    if inp == 'end':
        break
    try:
        n = inp.split(' = ')
    except:
        continue

    first, second = n[0], n[1]

    dct[first] = second

    for key, value in dct.copy().items():
        if second == key:
            dct[first] = value

for key, value in dct.items():
    if str(value).isalpha() and value not in dct:
        continue
    else:
        print('{} === {}'.format(key, value))
