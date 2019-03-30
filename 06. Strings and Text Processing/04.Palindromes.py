data = input().split()
result = []
for word in data:
    if word == word[::-1] and word not in result:
        result.append(word)

sorted_result = sorted(result, key=str.lower)
print(", ".join(sorted_result))
