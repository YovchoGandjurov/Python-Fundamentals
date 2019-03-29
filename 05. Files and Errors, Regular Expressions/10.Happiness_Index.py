import re


pattern = r"""
            (?P<happy>:\)|:D|;\)|:\*|:]|;]|:}|;}|\(:|\*:|c:|\[:|\[;)|
            (?P<sad>:\(|D:|;\(|:\[|;\[|:{|;{|\):|:c|]:|];)"""

happy_match = []
sad_match = []

data = input()
matches = re.finditer(pattern, data, re.X)

for item in matches:
    curr_happy = item.groupdict()['happy']
    curr_sad = item.groupdict()['sad']
    if curr_happy is not None:
        happy_match.append(curr_happy)
    else:
        sad_match.append(curr_sad)


len_happy = len(happy_match)
len_sad = len(sad_match)

happy_index = len_happy / len_sad

emoji = None
if happy_index >= 2:
    emoji = ":D"
elif happy_index > 1:
    emoji = ":)"
elif happy_index == 1:
    emoji = ":|"
else:
    emoji = ":("

print(f'Happiness index: {happy_index:.2f} {emoji}')
print(f"[Happy count: {len_happy}, Sad count: {len_sad}]")
