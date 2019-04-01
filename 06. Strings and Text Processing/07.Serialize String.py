text = input()
dict_chars = {}

for index, char in enumerate(text):
    if char not in dict_chars:
        dict_chars[char] = [str(index)]
    else:
        dict_chars[char].append(str(index))

for key, value in dict_chars.items():
    print(f"{key}:{'/'.join(value)}")
