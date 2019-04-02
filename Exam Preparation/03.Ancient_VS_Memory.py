import re


data = input()
list_items = []
result = []

while data != 'DEBUG':
    pattern = r"32656\s19759\s32763\s0\s\d+\s0\s(?P<items>.*?)\s($|0)"
    matches = re.finditer(pattern, data)

    for item in matches:
        list_items.append(item.group('items'))

    data = input()


def convert_to_char(string):
    string = string.split(' ')
    result = []

    for x in string:
        result.append(chr(int(x)))
    return ''.join(result)

for x in list_items:
    curr_word = convert_to_char(x)
    result.append(curr_word)

print('\n'.join(result))
