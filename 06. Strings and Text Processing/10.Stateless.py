states = input()
fiction = input()
result = []

while True:

    while True:
        if fiction == '':
            result.append(states.strip())
            break
        states = states.replace(fiction, '')
        fiction = fiction[1:-1]

    states = input()
    if states == 'collapse':
        break
    fiction = input()

for item in result:
    if item == '':
        print("(void)")
    else:
        print(item)
