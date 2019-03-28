import re


data = input()
pattern = r"""
    \b(?P<day>\d{2})([-\/.])
    (?P<month>[A-Z][a-z]{2})\2
    (?P<year>\d{4})\b"""

matches = re.finditer(pattern, data, re.X)

for x in matches:
    day = x.group("day")
    month = x.group("month")
    year = x.group("year")
    print(f"Day: {day}, Month: {month}, Year: {year}")
