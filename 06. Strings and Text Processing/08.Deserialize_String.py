data = input()
result = ''

while data != "end":
    letter = data.split(':')[0]
    second_part = data.split(':')[1]
    indices = [int(x) for x in second_part.split('/')]

    if result == "":
        result = (max(indices) + 1) * '*'
    elif max(indices) > len(result):
            result = result + (((max(indices) + 1) - len(result)) * "*")

    for x in indices:
        result = result[0:x] + letter + result[x+1:]

    data = input()

print(result)
