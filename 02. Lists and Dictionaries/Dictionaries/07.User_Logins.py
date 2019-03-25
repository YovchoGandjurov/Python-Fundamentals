logins = {}
output = []
count_attempt = 0

login = 0
while True:
    inp = input()

    if inp == 'end':
        break
    if inp == 'login':
        login = 1
        continue

    n = inp.split(' -> ')
    name, pas = n[0], n[1]

    if login == 0:
        logins[name] = pas

    if login == 1:
        for key, value in logins.items():
            if name == key and pas == value:
                output.append(key + ': logged in successfully')
                break
        else:
            output.append(name + ': login failed')
            count_attempt += 1


for x in output:
    print(x)

if count_attempt > 0:
    print('unsuccessful login attempts: {}'.format(count_attempt))
