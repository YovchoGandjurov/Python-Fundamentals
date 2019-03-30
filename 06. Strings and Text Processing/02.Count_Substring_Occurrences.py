def count_substring(text, loopuk_text):
    counter = 0
    index = 0

    while index != -1:
        index = text.casefold().find(loopuk_text.casefold(), index)
        if index is not -1:
            counter += 1
            index += 1
    return counter

print(count_substring(input(), input()))
