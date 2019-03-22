def replace_sep(inpt):
    strn = ''
    for x in inpt:
        if x in [',', ';', ':', '.', '!', '(', ')', '"', "'", '\\', '/', '[',
                 ']']:
            continue
        else:
            strn += x
    return strn

text = replace_sep(input())
lst = text.split(' ')

low = []
up = []
mixed = []


def count_lower(word):
    return sum(1 for x in word if x.islower())


def count_upper(word):
    return sum(1 for x in word if x.isupper())


for x in lst:
    if count_lower(x) == len(x):
        low.append(x)
    elif count_upper(x) == len(x):
        up.append(x)
    else:
        mixed.append(x)


print('Lower-case:', ', '.join(low))
print('Mixed-case:', ', '.join(mixed))
print('Upper-case:', ', '.join(up))
