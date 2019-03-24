dct = {}
inp = input()

while inp != "ready":

    city = inp.split(":")[0]
    vehicle_capacity = [x for x in inp.split(":")[1].split(",")]

    if city not in dct:
        dct[city] = {}

    for x in vehicle_capacity:
        vehicle = x.split("-")[0]
        capacity = x.split("-")[1]

        dct[city][vehicle] = capacity
    inp = input()

result = []

n = input()
while n != "travel time!":

    city = n.split(" ")[0]
    capacity = n.split(" ")[1]

    lst_values = [int(x) for x in dct[city].values()]
    total = sum(lst_values)

    if total >= int(capacity):
        print("{} -> all {} accommodated".format(city, capacity))
    else:
        print("{} -> all except {} accommodated".format(city, int(capacity) -
                                                        total))

    n = input()
