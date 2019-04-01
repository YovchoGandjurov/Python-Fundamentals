def left(string, times):
    result = string
    for x in range(times):
        result = result[1:] + result[0]
    return result


def right(string, times):
    result = string
    for x in range(times):
        result = result[-1] + result[:-1]
    return result


def insert_chars(string, index, chars):
    result = string
    result = result[0:index] + chars + result[index:]
    return result


def delete_chars(string, start_index, end_index):
    result = string
    result = result[:start_index] + result[end_index + 1:]
    return result


manipulate_str = input()
comands = input()

while comands != "end":
    curr_comand = comands.split()

    if curr_comand[0] == 'Left':
        manipulate_str = left(manipulate_str, int(curr_comand[1]))
    elif curr_comand[0] == 'Right':
        manipulate_str = right(manipulate_str, int(curr_comand[1]))
    elif curr_comand[0] == 'Insert':
        manipulate_str = insert_chars(manipulate_str, int(curr_comand[1]),
                                      curr_comand[2])
    elif curr_comand[0] == 'Delete':
        manipulate_str = delete_chars(manipulate_str, int(curr_comand[1]),
                                      int(curr_comand[2]))

    comands = input()

print(manipulate_str)
