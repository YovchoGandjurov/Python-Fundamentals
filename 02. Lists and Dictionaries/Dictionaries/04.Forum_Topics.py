dct = {}

while True:
    inp = input()
    if inp == "filter":
        break

    topic = inp.split(" -> ")[0]
    second_part = inp.split(" -> ")[1]
    tags = [x for x in second_part.split(", ")]

    if topic not in dct:
        dct[topic] = tags
    else:
        dct[topic] = dct[topic] + tags

n = input().split(", ")

for key in dct.keys():
    used = []
    lst = [used.append(y) for y in dct[key] if y not in used]
    dct[key] = used

    if n[0] in dct[key]:
        print("{} | #{}".format(key, ", #".join(used)))
