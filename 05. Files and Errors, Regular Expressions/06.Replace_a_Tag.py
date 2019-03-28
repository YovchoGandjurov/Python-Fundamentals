import re

data = input()
result = ""
lst_result = []

while data != "end":

    result = re.sub(r"<ahref|<a href", r"[URL href", data)
    result = re.sub(r'">', r'"]', result)
    result = re.sub(r"</a>", r"[/URL]", result)
    lst_result.append(result)

    data = input()

for x in lst_result:
    print(x)
