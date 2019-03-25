dct = {}


def output_print(name, placeholder1, placeholder2):
    print("Name: {}\n{}: {}\n====================".format(name, placeholder1,
                                                          placeholder2))


def set_dictionary(name):
    dct[name] = {
        'age': '',
        'position': '',
        'salary': ''}

flag = 0
age_order = []
position_order = []
salary_order = []

while flag == 0:
    age = ''
    position = ''
    salary = ''

    inp = input()
    if inp == 'filter base':
        filter = input()
        flag = 1

    if flag == 0:
        n = inp.split(' -> ')
        name, second_elem = n[0], n[1]
        try:
            if '.' in second_elem:
                salary = float(second_elem)
                salary_order.append(name)
            else:
                age = int(second_elem)
                age_order.append(name)
        except:
            position = second_elem
            position_order.append(name)

    if name not in dct:
        set_dictionary(name)

    if age != '':
        dct[name]['age'] = age
    if position != '':
        dct[name]['position'] = position
    if salary:
        dct[name]['salary'] = salary


equals = 20*"="

if filter == 'Age':
    for x in age_order:
        print("Name: {}\n{}: {}\n{}".format(x, 'Age', dct[x]['age'], equals))

elif filter == 'Position':
    for x in position_order:
        print("Name: {}\n{}: {}\n{}".format(x, 'Position', dct[x]['position'],
                                            equals))
elif filter == 'Salary':
    for x in salary_order:
        print("Name: {}\n{}: {}\n{}".format(x, 'Salary', dct[x]['salary'],
                                            equals))
