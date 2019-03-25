n = int(input())
dct = {}

for x in range(n):
    inp = input().split(' -> ')

    clothes = inp[1].split(',')
    color = inp[0]

    for x in clothes:
        if color in dct:
            if x in dct[color]:
                dct[color][x] += 1
            else:
                dct[color][x] = 1
        else:
            dct[color] = {x: 1}


final_input = input().split()

for i in dct:
    print('{} clothes:'.format(i))

    for key, value in dct[i].items():
        if final_input[0] == i and final_input[1] == key:
            print('* {} - {} {}'.format(key, value, '(found!)'))
        else:
            print('* {} - {}'.format(key, value))
