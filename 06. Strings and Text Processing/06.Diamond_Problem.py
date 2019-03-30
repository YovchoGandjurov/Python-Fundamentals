def get_number(string):
    list_numbers = []
    for x in string:
        if x.isdigit():
            list_numbers.append(int(x))
    return list_numbers

text = input()
result = []
start_index = -1
end_index = -1

for index, char in enumerate(text):

    if char == "<":
        start_index = index

    elif char == ">" and start_index != -1:
        end_index = index
        result.append(text[start_index + 1: end_index])
        start_index = -1

if len(result) == 0:
    print("Better luck next time")
else:
    for diamond_str in result:
        curr_sum = get_number(diamond_str)
        print(f"Found {sum(curr_sum)} carat diamond")
