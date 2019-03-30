import re


def get_number(string):
    list_numbers = []
    for x in string:
        if x.isdigit():
            list_numbers.append(int(x))
    return list_numbers

text = input()
pattern = r"(?<=<)\w*(?=>)"
matches = re.findall(pattern, text)

if len(matches) == 0:
    print("Better luck next time")
else:
    for diamond_str in matches:
        curr_sum = get_number(diamond_str)
        print(f"Found {sum(curr_sum)} carat diamond")
