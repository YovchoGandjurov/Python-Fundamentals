class Passenger:
    def __init__(self, first_name, last_name, destination, card_number):
        self.first_name = first_name
        self.last_name = last_name
        self.card_number = card_number
        self.destination = {}
        self.total_price = 0

    def update_destin(self, new_destin):
        return self.destination.update(new_destin)

    @property
    def names(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return 'user - {} {} / destination - {} / total - {}'.format(
                self.first_name,
                self.last_name,
                self.destination,
                self.total_price)


def get_price(destination):
    price = list(map(ord, destination))
    return sum(price) / 100


def check_card(card_number):
    card_number = list(map(int, card_number))
    if sum(card_number) % 7 == 0:
        return True
    else:
        return False


def pass_name(first, last):
    return first + ' ' + last


n = int(input())
users = {}
first_result = []
passengers = []

for x in range(n):
    data = input().split()
    name = data[0] + ' ' + data[1]
    number = data[2]

    if name not in users:
        users[name] = [number]
    else:
        if number not in users[name]:
            users[name].append(number)

data = input()

while data != 'time to leave!':
    data = data.split()
    command = data[0]
    first_name = data[1]
    last_name = data[2]
    destin = data[3]
    card_number = data[4]
    names = pass_name(first_name, last_name)

    passenger = Passenger(first_name, last_name, destin, card_number)

    if names in users and card_number in users[names]:
        passenger.destination[destin] = (get_price(destin) / 2,
                                         passenger.card_number)

    else:
        if check_card(card_number):
            curr_users = []
            for i in users.values():
                curr_users.extend(i)
            if card_number in curr_users:
                passenger.destination[destin] = (get_price(destin), None)
                first_result.append(
                    f'card {card_number} already exists for another passenger!'
                    )

            else:
                passenger.destination[destin] = (get_price(destin) / 2,
                                                 passenger.card_number)
                first_result.append(f'issuing card {card_number}')
                if names in users:
                    users[names].append(card_number)
                else:
                    users[names] = [card_number]
        else:
            first_result.append(f'card {card_number} is not valid!')
            passenger.destination[destin] = (get_price(destin), None)

    if passenger.names not in [x.names for x in passengers]:
        passenger.total_price = passenger.destination[destin][0]
        passengers.append(passenger)
    else:
        for item in passengers:
            if item.names == passenger.names:
                item.total_price += passenger.destination[destin][0]
                item.update_destin(passenger.destination)

    data = input()


print('\n'.join(first_result))

sorted_by_total = sorted(passengers, key=lambda x: x.total_price, reverse=True)

for item in sorted_by_total:
    print(f'{item.names}:')
    sorted_by_ticket = sorted(item.destination.items(), key=lambda x: -x[1][0])

    for y in sorted_by_ticket:

        price = y[1][0]
        card_num = y[1][1]

        if card_num is not None:
            print(f"--{y[0]}: {price:.2f}lv (using card {card_num})")
        else:
            print(f"--{y[0]}: {price:.2f}lv")

    print(f'total: {item.total_price:.2f}lv')

print("="*50)

for x in passengers:
    print(x)
