import re
data = input()

def even_increase(elem):
    result = elem
    if elem % 2 == 0:
        result += 2
    return result

def odd_increase(elem):
    result = elem
    if elem % 2 == 1:
        result += 3
    return result

while data != "stop playing":
    data = data.strip()
    data = re.split(r'\s+', data)
    data = [int(x) for x in data]
    
    if len(set(data)) == len(data):
        result = list(map(even_increase, data))
        result = sorted(result)
        print(f"Unique list: {','.join(list(map(str, result)))}")
        print(f"Output: {sum(result) / len(result):.2f}")
    else:
        result = list(map(odd_increase, data))
        result = sorted(result)
        print(f"Non-unique list: {':'.join(list(map(str, result)))}")
        print(f"Output: {sum(result) / len(result):.2f}")

    data = input()