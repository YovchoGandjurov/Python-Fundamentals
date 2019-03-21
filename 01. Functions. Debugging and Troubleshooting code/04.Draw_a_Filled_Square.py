dash = '-'
slash = '\\/'


def lines(n):
    return (n*2) * dash


def middle(n):
    row = dash + (slash * (n-1)) + dash
    for x in range(n - 2):
        print(row)

n = int(input())
print(lines(n))
middle(n)
print(lines(n))
