import re


sentance_pattern = r"^([A-Z])(.*)(\.|\!|\?)$"

output_words = []

filter_word = input()
data = input()
while data != "end":
    if re.match(sentance_pattern, data):
        matches = re.finditer(r"\b(?:[^" +
                              re.escape(filter_word[0]) +
                              r"\s]*" +
                              re.escape(filter_word[0]) + r")" +
                              r"{" + re.escape(filter_word[1]) +
                              r"}[^{" + re.escape(filter_word[0]) +
                              r"}\s]*\b", data)
        for x in matches:
            output_words.append(x.group())
    data = input()

print(", ".join(output_words))
