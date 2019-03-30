def reverse_string(string):
    result = ""
    for i in string[::-1]:
        result += i
    return result

print(reverse_string(input()))
