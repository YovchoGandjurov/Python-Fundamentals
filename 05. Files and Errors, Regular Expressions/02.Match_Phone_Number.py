import re

phones = input()
pattern = r"\+359(\-| )2?\1\d{3}\1\d{4}\b"

matches = re.finditer(pattern, phones)

for x in matches:
    print(x.group(), end=" ")
