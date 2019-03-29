import re

data = input()
pattern = r"([2-9]|10|[JQKA])([SHDC])"
matches = re.finditer(pattern, data)

for x in matches:
    print(x.group(), end=" ")
