dct = {}

while True:
    inp = input()
    if inp == "end":
        break
    name = inp.split(" -> ")[0]
    vals = inp.split(" -> ")[1]

    if vals.isalpha() and vals not in dct:
        continue

    if name not in dct:
        if vals.isalpha() and vals in dct:
            dct[name] = dct[vals]
        else:
            dct[name] = vals
    else:
        dct[name] = dct[name] + ", " + vals


for key, values in dct.items():
    print("{} === {}".format(key, values))
