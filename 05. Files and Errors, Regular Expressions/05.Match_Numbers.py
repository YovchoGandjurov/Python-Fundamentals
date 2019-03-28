import re

data = input()
pattern = r"(^|(?<=\s))-?\d+(\.?\d+)?($|(?=\s))"
matches = re.finditer(pattern, data)

for x in matches:
    print(x.group(), end=" ")
