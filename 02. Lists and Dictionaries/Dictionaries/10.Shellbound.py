dct = {}
while True:
    inp = input()
    if inp == "Aggregate":
        break

    region = inp.split()[0]
    shell = inp.split()[1]

    if region not in dct:
        dct[region] = [shell]
    else:
        dct[region].append(shell)


for x in dct.keys():
    used = []
    lst = [used.append(y) for y in dct[x] if y not in used]

    sum_shells = sum([int(i) for i in used])
    count_shells = len(used)
    total = sum_shells - (sum_shells / count_shells)
    print("{} -> {} ({:.0f})".format(x, ", ".join(used), total))
