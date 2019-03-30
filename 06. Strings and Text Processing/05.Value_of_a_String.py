text, sting_type = input(), input()

result = 0
for x in text:
    if sting_type == "UPPERCASE" and ord(x) in range(65, 91):
        result += ord(x)
    elif sting_type == "LOWERCASE" and ord(x) in range(97, 123):
        result += ord(x)

print(f"The total sum is: {result}")
