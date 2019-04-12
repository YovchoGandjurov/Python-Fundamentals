import re

pattern = r"(?P<name>(?<=name is )[A-Z][a-z]+\s[A-Z][a-z]+).*(?P<age>(?<=\s)\d{2}(?=\syears)).*(?P<date>(?<=on\s)\d{2}-\d{2}-\d{4}).$"

data = input()
final_result = []

while data != "make migrations":
    result = {}
    for match in re.finditer(pattern, data):
        groups = match.groupdict()
        result["name"] = groups["name"]
        result["age"] = groups["age"]
        result["date"] = groups["date"]

    
    if bool(result):
        person_info = f"Name of the person: {result['name']}.\nAge of the person: {result['age']}.\nBirthdate of the person: {result['date']}."
        final_result.append(person_info)

    data = input()

if len(final_result) == 0:
    print("DB is empty")
else:
    print("\n".join(final_result))
