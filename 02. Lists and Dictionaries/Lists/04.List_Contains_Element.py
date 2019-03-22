n = [x for x in input().split(' ')]
n2 = input()

isFound = 0

for x in n:
    if x == n2:
        isFound = 1
        break

if isFound == 1:
    print('yes')
else:
    print('no')
