import re


def convert_letter(letter):
    result = letter
    if ord(letter) in range(97, 110):
        result = chr(ord(letter) + 13)
    elif ord(letter) in range(110, 123):
        result = chr(ord(letter) - 13)
    return result


pattern = r"(?<=<p>).*?(?=</p>)"

data = input()
clean_data = re.findall(pattern, data)

clean_result = ''

for x in clean_data:
    clean_result += re.sub(r"[^a-z0-9]", " ", x)

result = ''

for char in clean_result:
    result += convert_letter(char)

result = re.sub(r"\s+", " ", result)
print(result)
