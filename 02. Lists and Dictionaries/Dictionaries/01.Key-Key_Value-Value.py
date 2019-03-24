key_search = input()
value_search = input()
n = int(input())

result = {}

for x in range(n):
    inp = input().split(' => ')
    values = inp[1].split(';')
    if key_search in inp[0]:
        filt = list(filter(lambda x: value_search in x, values))
        result[inp[0]] = filt


for key, val in result.items():
    if len(val) >= 1:
        print('{}:'.format(key))
        for x in val:
                print('-{}'.format(x))
