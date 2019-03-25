dct = {}

while True:
    inp = input()
    if inp == 'Over':
        break

    n = inp.split(" : ")
    name, phone = n[0], n[1]

    if name.isdigit():
        dct[phone] = name
    else:
        dct[name] = phone

for key in sorted(dct):
    print('{} -> {}'. format(key, dct[key]))
