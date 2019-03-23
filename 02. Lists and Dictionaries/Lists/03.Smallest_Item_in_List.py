n = [int(x) for x in input().split(' ')]
print(min(n))

n = [int(x) for x in input().split(' ')]
result = n[0]

for number in n:
    if number < result:
        result = number

print(result)
